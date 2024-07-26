import pandas as pd
import numpy as np
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
import dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load environment variables from .env file
dotenv.load_dotenv()
env_vars = dotenv.dotenv_values()

# Set up OpenAI
openai_api_key = env_vars["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

# Set up Pinecone
pinecone_api_key = env_vars["PINECONE_API_KEY"]
pinecone_environment = env_vars["PINECONE_ENVIRONMENT"]

pc = Pinecone(api_key=pinecone_api_key)

# Create or connect to a Pinecone index
index_name = 'iam-chatbot'
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name, 
        dimension=1536, 
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region=pinecone_environment
        )
    )
index = pc.Index(index_name)

# Load and preprocess data
df = pd.read_excel('incidents.xlsx')
incident_no_col = 'Incident Number'
description_col = 'Description'
class_col = 'Class'
resolution_col = 'Resolution'
df['combined_text'] = df[class_col] + " " + df[description_col]

# Embed text using OpenAI
def embed_text(text):
    response = client.embeddings.create(input=[text], model="text-embedding-ada-002")
    return response.data[0].embedding

# Embed all combined texts
df['embeddings'] = df['combined_text'].apply(embed_text)

# Upsert embeddings to Pinecone
vectors = [(str(i), np.array(emb).tolist()) for i, emb in enumerate(df['embeddings'].tolist())]
index.upsert(vectors)

# Function to find similar incidents
def find_similar_incidents(new_incident_description):
    new_embedding = embed_text(new_incident_description)
    new_embedding_list = np.array(new_embedding).tolist()
    query_response = index.query(vector=new_embedding_list, top_k=3, include_values=True)
    similar_incidents = query_response['matches']
    return [int(match['id']) for match in similar_incidents]

# Function to suggest resolutions based on similar incidents
def suggest_resolutions(new_incident_description):
    similar_incident_ids = find_similar_incidents(new_incident_description)
    similar_resolutions = df.loc[similar_incident_ids, resolution_col].tolist()
    return similar_resolutions

@app.route('/suggest', methods=['POST'])
def get_suggestions():
    data = request.json
    incident_description = data.get('description')
    if not incident_description:
        return jsonify({"error": "No incident description provided"}), 400
    
    suggested_resolutions = suggest_resolutions(incident_description)
    return jsonify({"resolutions": suggested_resolutions})

if __name__ == '__main__':
    app.run(debug=True)