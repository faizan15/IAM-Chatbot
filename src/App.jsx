import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import { useTheme } from './ThemeContext';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const { isDarkMode, toggleTheme } = useTheme();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('http://backend:5000/suggest', { description: input });
      const botMessages = response.data.resolutions.map(resolution => ({
        text: resolution,
        sender: 'bot'
      }));
      setMessages(prev => [...prev, ...botMessages]);
    } catch (error) {
      console.error('Error fetching resolutions:', error);
      setMessages(prev => [...prev, { text: 'Sorry, I encountered an error.', sender: 'bot' }]);
    }
    setLoading(false);
  };

  return (
    <div className={`chat-container ${isDarkMode ? 'dark-mode' : 'light-mode'}`}>
      <div className="chat-header">
        <h1>Incident Resolution Chat</h1>
        <button onClick={toggleTheme} className="theme-toggle">
          {isDarkMode ? '☀️' : '🌙'}
        </button>
      </div>
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            {message.text}
          </div>
        ))}
        {loading && <div className="message bot">Thinking...</div>}
        <div ref={messagesEndRef} />
      </div>
      <form className="chat-input-form" onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Describe the incident..."
          className="chat-input"
        />
        <button type="submit" className="chat-submit" disabled={loading}>
          Send
        </button>
      </form>
    </div>
  );
}

export default App;