import React, { useEffect, useState } from 'react';
import { Carousel, Container, Row, Col, Button } from 'react-bootstrap';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import authService from '../services/authService';
import getRandomImageUrls from '../services/getRandomImageUrls'

const API_URL = 'http://0.0.0.0:8000/api/';

const PropertyDetails = () => {
  const { id } = useParams(); // Get property ID from URL parameters
  const [property, setProperty] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Fetch property details
    const fetchPropertyDetails = async () => {
      try {
        const response = await axios.get(`${API_URL}properties/${id}/`);
        setProperty(response.data);
      } catch (error) {
        console.error('Error fetching property details:', error);
      }
    };

    fetchPropertyDetails();
  }, [id]);

  const handleInterestClick = async () => {
    setIsLoading(true);
    try {
      const currentUser = authService.getCurrentUser();
      if (!currentUser) {
        console.error('Current user not found');
        return;
      }

      const requestData = {
        propertyId: property.id,
        userId: currentUser.id,
      };

      const response = await axios.post(API_URL + 'interest-map/', requestData);
      if (response.status === 200 || response.status === 201) {
        console.log('Interest map entry created');
      } else {
        console.error('Failed to create interest map entry');
      }
    } catch (error) {
      console.error('Error creating interest map entry:', error);
    }
    setIsLoading(false);
  };

//   const getRandomImageUrls = () => {
//     const images = [];
//     for (let i = 0; i < 5; i++) {
//       images.push(`https://picsum.photos/800/400?random=${Math.random()}`);
//     }
//     return images;
//   };

  return (
    <Container>
      {property ? (
        <>
          <Carousel>
            {getRandomImageUrls(3, 800, 400).map((url, index) => (
              <Carousel.Item key={index}>
                <img
                  className="d-block w-100"
                  src={url}
                  alt={`Slide ${index}`}
                />
              </Carousel.Item>
            ))}
          </Carousel>
          <Row className="mt-4">
            <Col md={8}>
              <h2>{property.title}</h2>
              <p>{property.description}</p>
              <p><strong>Address:</strong> {property.address}, {property.city}, {property.state}, {property.zip_code}, {property.country}</p>
              <p><strong>Rent Price:</strong> ${property.rent_price}</p>
              <p><strong>Bedrooms:</strong> {property.bedrooms}</p>
              <p><strong>Bathrooms:</strong> {property.bathrooms}</p>
              <p><strong>Square Feet:</strong> {property.square_feet} sqft</p>
              <p><strong>Furnished:</strong> {property.furnished ? 'Yes' : 'No'}</p>
              <p><strong>Pet Friendly:</strong> {property.pet_friendly ? 'Yes' : 'No'}</p>
              <p><strong>Available From:</strong> {property.available_from}</p>
              <p><strong>Lease Term:</strong> {property.lease_term}</p>
              <Button variant="success" onClick={handleInterestClick} disabled={isLoading}>
                {isLoading ? 'Loading...' : 'I am Interested'}
              </Button>
            </Col>
          </Row>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </Container>
  );
};

export default PropertyDetails;

