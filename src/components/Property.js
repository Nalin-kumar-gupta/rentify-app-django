import React, { useState } from 'react';
import { Card, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import axios from 'axios';
import authService from '../services/authService';
import getRandomImageUrls from '../services/getRandomImageUrls';

const API_URL = 'http://0.0.0.0:8000/api/';

const Property = ({ property }) => {
  const [isLoading, setIsLoading] = useState(false);

  const handleInterestClick = async () => {
    setIsLoading(true);
    try {
      // Get the current user
      const currentUser = authService.getCurrentUser();
      if (!currentUser) {
        console.error('Current user not found');
        return;
      }
      
      // Append the user ID to the request body
      const requestData = {
        propertyId: property.id,
        userId: currentUser.id,
      };

      const response = await axios.post(API_URL + 'interest-map/', requestData);
      if (response.status === (200 || 201)) {
        // Interest map entry created successfully
        console.log('Interest map entry created');
      } else {
        // Handle error response
        console.error('Failed to create interest map entry');
      }
    } catch (error) {
      console.error('Error creating interest map entry:', error);
    }
    setIsLoading(false);
  };



  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={getRandomImageUrls(1, 300, 200)[0]} alt={property.title} />
      <Card.Body>
        <Card.Title>{property.title}</Card.Title>
        <Card.Text>{property.description.substring(0, 100)}...</Card.Text>
        <Link to={`/properties/${property.id}`}>
          <Button variant="primary">View Details</Button>
        </Link>
        <Button variant="success" onClick={handleInterestClick} disabled={isLoading}>
          {isLoading ? 'Loading...' : 'I am Interested'}
        </Button>
      </Card.Body>
    </Card>
  );
};

export default Property;
