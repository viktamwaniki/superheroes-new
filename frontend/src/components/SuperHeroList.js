import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SuperheroList = () => {
  const [superheroes, setSuperheroes] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/superheroes')
      .then(response => {
        setSuperheroes(response.data.superheroes);
      })
      .catch(error => console.error('Error fetching superheroes:', error));
  }, []);

  return (
    <div>
      <h1>Superheroes List</h1>
      <ul>
        {superheroes.map((hero, index) => (
          <li key={index}>{hero.name} - Powers: {hero.powers}, Avenger: {hero.is_avenger ? 'Yes' : 'No'}</li>
        ))}
      </ul>
    </div>
  );
};

export default SuperheroList;
