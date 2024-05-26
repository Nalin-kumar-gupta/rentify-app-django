import React, { useState } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import authService from '../services/authService';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    authService.login(username, password).then(
      () => {
        navigate('/');
      },
      (error) => {
        setError(error.message);
        console.log(error);
      }
    );
  };

  return (
    <Container className="login-container">
      <Row className="justify-content-center">
        <Col md={4} lg={3} xl={2} className="login-form">
          <h2 className="text-center">Log in to Your Account</h2>
          <Form onSubmit={handleLogin}>
            <Form.Group controlId="formEmail">
              <Form.Label>Username</Form.Label>
              <Form.Control
                type="username"
                value={username}
                onChange={(event) => setUsername(event.target.value)}
                placeholder="Enter username"
              />
            </Form.Group>

            <Form.Group controlId="formPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                placeholder="Enter password"
              />
            </Form.Group>

            {error && (
              <div className="alert alert-danger" role="alert">
                {error}
              </div>
            )}

            <Button variant="primary" type="submit" block>
              Log in
            </Button>
          </Form>

          <p className="forgot-password text-right">
            <a href="#">Forgot password?</a>
          </p>

          <p className="create-account text-center">
            Don't have an account? <a href="#">Create one</a>
          </p>
        </Col>
      </Row>
    </Container>
  );
};

export default Login;



























// import React, { useState } from 'react';
// import { Container, Row, Col, Form, Button } from 'react-bootstrap';

// function LoginPage() {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState(null);

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     // Call API to authenticate user
//     // For demo purposes, just log in successfully
//     console.log('Logged in successfully!');
//   };

//   return (
//     <Container className="login-container">
//       <Row className="justify-content-center">
//         <Col md={4} lg={3} xl={2} className="login-form">
//           <h2 className="text-center">Log in to Your Account</h2>
//           <Form onSubmit={handleSubmit}>
//             <Form.Group controlId="formEmail">
//               <Form.Label>Username</Form.Label>
//               <Form.Control
//                 type="username"
//                 value={username}
//                 onChange={(event) => setUsername(event.target.value)}
//                 placeholder="Enter username"
//               />
//             </Form.Group>

//             <Form.Group controlId="formPassword">
//               <Form.Label>Password</Form.Label>
//               <Form.Control
//                 type="password"
//                 value={password}
//                 onChange={(event) => setPassword(event.target.value)}
//                 placeholder="Enter password"
//               />
//             </Form.Group>

//             {error && (
//               <div className="alert alert-danger" role="alert">
//                 {error}
//               </div>
//             )}

//             <Button variant="primary" type="submit" block>
//               Log in
//             </Button>
//           </Form>

//           <p className="forgot-password text-right">
//             <a href="#">Forgot password?</a>
//           </p>

//           <p className="create-account text-center">
//             Don't have an account? <a href="#">Create one</a>
//           </p>
//         </Col>
//       </Row>
//     </Container>
//   );
// }

// export default LoginPage;