import React, { useEffect, useState } from 'react';
import { Carousel, Container, Row, Col, Button, Card } from 'react-bootstrap';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import authService from '../services/authService';
import getRandomImageUrls from '../services/getRandomImageUrls';
import { API_URL } from '../environment/prodEnviron';

// const API_URL = 'http://0.0.0.0:8000/api/';

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

  return (
    <Container className="mt-5">
      {property ? (
        <>
          <Carousel className="mb-4">
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
          <Row className="justify-content-md-center">
            <Col md={10}>
              <Card>
                <Card.Body>
                  <Card.Title as="h2" className="text-center mb-4">{property.title}</Card.Title>
                  <Card.Text className="mb-4">{property.description}</Card.Text>
                  <Row>
                    <Col md={6}>
                      <ul className="list-unstyled">
                        <li><strong>Address:</strong> {property.address}, {property.city}, {property.state}, {property.zip_code}, {property.country}</li>
                        <li><strong>Rent Price:</strong> ${property.rent_price}</li>
                        <li><strong>Security Deposit:</strong> ${property.security_deposit}</li>
                        <li><strong>Lease Term:</strong> {property.lease_term}</li>
                        <li><strong>Available From:</strong> {property.available_from}</li>
                      </ul>
                    </Col>
                    <Col md={6}>
                      <ul className="list-unstyled">
                        <li><strong>Property Type:</strong> {property.property_type}</li>
                        <li><strong>Bedrooms:</strong> {property.bedrooms}</li>
                        <li><strong>Bathrooms:</strong> {property.bathrooms}</li>
                        <li><strong>Square Feet:</strong> {property.square_feet} sqft</li>
                        <li><strong>Furnished:</strong> {property.furnished ? 'Yes' : 'No'}</li>
                        <li><strong>Pet Friendly:</strong> {property.pet_friendly ? 'Yes' : 'No'}</li>
                      </ul>
                    </Col>
                  </Row>
                  <div className="text-center mt-4">
                    <Button variant="success" onClick={handleInterestClick} disabled={isLoading}>
                      {isLoading ? 'Loading...' : 'I am Interested'}
                    </Button>
                  </div>
                </Card.Body>
              </Card>
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
