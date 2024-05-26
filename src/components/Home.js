

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Property from '../components/Property';
import { Container, Row, Col, Pagination } from 'react-bootstrap';

const API_URL = 'http://0.0.0.0:8000/api/';

const Home = () => {
  const [properties, setProperties] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    axios.get(API_URL + `properties/?page=${currentPage}`)
      .then(response => {
        setProperties(response.data.results);
        setTotalPages(Math.ceil(response.data.count / 9)); 
      })
      .catch(error => console.error('Error fetching properties:', error));
  }, [currentPage]);

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  return (
    <Container>
      <h1>Properties</h1>
      <Row>
        {properties.map(property => (
          <Col key={property.id} md={4} className="mb-4">
            <Property property={property} />
          </Col>
        ))}
      </Row>
      <Pagination>
        {Array.from({ length: totalPages }, (_, index) => (
          <Pagination.Item
            key={index + 1}
            active={currentPage === index + 1}
            onClick={() => handlePageChange(index + 1)}
          >
            {index + 1}
          </Pagination.Item>
        ))}
      </Pagination>
    </Container>
  );
};

export default Home;









