import React from 'react';
import { Navbar, Nav, Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import authService from '../services/authService';

const CustomNavbar = () => {
  const navigate = useNavigate();
  const currentUser = authService.getCurrentUser();

  const handleLogout = () => {
    authService.logout();
    navigate('/login');
  };

  const handleManageProfile = () => {
    // Redirect to the Django admin URL
    window.location.href = 'http://localhost/api/admin/';
  };

  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Brand as={Link} to="/">MyApp</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto">
          {currentUser ? (
            <>
              <Nav.Link as={Link} to="/">Home</Nav.Link>
              <Button variant="outline-primary" onClick={handleManageProfile}>
                Manage Profile
              </Button>
              <Button variant="outline-danger" onClick={handleLogout} className="ml-2">
                Logout
              </Button>
            </>
          ) : (
            <>
              <Nav.Link as={Link} to="/login">Login</Nav.Link>
              <Nav.Link as={Link} to="/register">Register</Nav.Link>
            </>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default CustomNavbar;
