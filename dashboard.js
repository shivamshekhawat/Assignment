import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    fetchDishes();
  }, []);

  const fetchDishes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/dishes');
      setDishes(response.data);
    } catch (error) {
      console.error('Error fetching dishes:', error);
    }
  };

  const toggleDish = async (dishId) => {
    try {
      const response = await axios.post(`http://localhost:5000/dishes/${dishId}/toggle`);
      setDishes(dishes.map(dish =>
        dish.dishId === dishId ? { ...dish, isPublished: response.data.isPublished } : dish
      ));
    } catch (error) {
      console.error('Error toggling dish:', error);
    }
  };

  return (
    <div>
      <h1>Dish Dashboard</h1>
      <ul>
        {dishes.map(dish => (
          <li key={dish.dishId}>
            <img src={dish.imageUrl} alt={dish.dishName} width="100" />
            <h2>{dish.dishName}</h2>
            <p>{dish.isPublished ? 'Published' : 'Unpublished'}</p>
            <button onClick={() => toggleDish(dish.dishId)}>
              {dish.isPublished ? 'Unpublish' : 'Publish'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default dashboard;
