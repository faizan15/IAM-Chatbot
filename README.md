
# Incident Resolution Chat

Incident Resolution Chat is a full-stack application that uses AI to suggest resolutions for IT incidents based on historical data. It combines a React frontend with a Flask backend, utilizing OpenAI's embeddings and Pinecone for similarity search.

This application is built for easy incident management/troubleshooting in the domain of Identity and Access Management (IAM). However, it can be easily extended to other domains by training the AI model with relevant data.

## Features

- Chat interface for describing incidents
- AI-powered resolution suggestions based on similar past incidents
- Dark/Light mode toggle
- Real-time response streaming
- Secure API key management

## Tech Stack

![React](https://img.shields.io/badge/React-v17+-blue.svg) ![Flask](https://img.shields.io/badge/Flask-v2+-blue.svg) ![OpenAI](https://img.shields.io/badge/OpenAI-API-lightgrey.svg) ![Pinecone](https://img.shields.io/badge/Pinecone-API-orange.svg)


## Prerequisites

![Node.js](https://img.shields.io/badge/Node.js-v14+-green.svg) ![npm](https://img.shields.io/badge/npm-v6+-blue.svg) ![Python](https://img.shields.io/badge/Python-v3.7+-blue.svg) ![OpenAI](https://img.shields.io/badge/OpenAI-API-lightgrey.svg) ![Pinecone](https://img.shields.io/badge/Pinecone-API-orange.svg)

Incident Resolution Chat is a full-stack application that uses AI to suggest resolutions for IT incidents based on historical data. It combines a React frontend with a Flask backend, utilizing OpenAI's embeddings and Pinecone for similarity search.


## Installation

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   ```

5. Ensure you have an `incidents.xlsx` file in the backend directory with your incident data.

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

## Running the Application

1. Start the backend server:
   ```
   cd backend
   python backend.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Enter a description of an IT incident in the chat input.
2. The AI will process your input and suggest resolutions based on similar past incidents.
3. You can toggle between dark and light modes using the theme button in the header.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


- OpenAI for their powerful embeddings API
- Pinecone for their vector database solution
- React and Flask communities for their excellent documentation and resources
