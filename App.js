import React, { useState } from 'react';
import './App.css';
import QueryForm from './components/QueryForm';
import ImageResults from './components/ImageResults';

function App() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const handleQuerySubmit = async (userQuery) => {
    setLoading(true);
    setError('');

    try {
      const response = await fetch('http://localhost:5000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userQuery }),
      });

      if (!response.ok) {
        throw new Error('Error fetching data from the server');
      }

      const data = await response.json();
      setResults(data.images);
    } catch (err) {
      setError('Failed to fetch results');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Multi-Modal Image Retrieval</h1>
      <QueryForm onSubmit={handleQuerySubmit} />
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      <ImageResults images={results} />
    </div>
  );
}

export default App;
