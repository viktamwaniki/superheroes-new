import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SuperheroList = () => {
  const [superheroes, setSuperheroes] = useState([]);

  useEffect(() => {
    // Fetch superheroes from the backend
    axios.get('http://localhost:5000/superheroes')
      .then(response => {
        setSuperheroes(response.data.superheroes);
      })
      .catch(error => console.error('Error fetching superheroes:', error));
  }, []);

  return (
    <div>
      <h2>Superheroes List</h2>
      <ul>
        {superheroes.map((hero) => (
          <li key={hero.id}>{hero.name} - Powers: {hero.powers}</li>
        ))}
      </ul>
    </div>
  );
};

export default SuperheroList;
