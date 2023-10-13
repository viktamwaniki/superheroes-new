import React, { useState, useEffect } from 'react';
import axios from 'axios';
import SuperheroList from './components/SuperHeroList';

function App() {
  const [superheroes, setSuperheroes] = useState([]);

  useEffect(() => {
    // Fetch superhero data from the backend
    axios.get('http://localhost:5000/superheroes')
      .then(response => {
        setSuperheroes(response.data.superheroes);
      })
      .catch(error => console.error('Error fetching superheroes:', error));
  }, []);

  return (
    <div className="App">
      <h1>Superheroes App</h1>
      <SuperheroList superheroes={superheroes} />
    </div>
  );
}

export default App;
