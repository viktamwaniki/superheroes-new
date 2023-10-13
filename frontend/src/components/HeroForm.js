import React from 'react';
import { useFormik } from 'formik';
import axios from 'axios';

const HeroForm = () => {
  const formik = useFormik({
    initialValues: {
      name: '',
      powers: ''
    },
    onSubmit: values => {
      // Submit the form data to the backend API
      axios.post('http://localhost:5000/superheroes', values)
        .then(response => {
          console.log('Hero submitted successfully:', response.data);
        })
        .catch(error => console.error('Error submitting hero:', error));
    }
  });

  return (
    <div>
      <h2>Add a Hero</h2>
      <form onSubmit={formik.handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            onChange={formik.handleChange}
            value={formik.values.name}
          />
        </div>
        <div>
          <label htmlFor="powers">Powers:</label>
          <input
            type="text"
            id="powers"
            name="powers"
            onChange={formik.handleChange}
            value={formik.values.powers}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default HeroForm;
