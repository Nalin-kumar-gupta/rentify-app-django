import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import authService from '../services/authService';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [permanentAddress, setPermanentAddress] = useState('');
  const [idProof, setIdProof] = useState(null);
  const [profilePhoto, setProfilePhoto] = useState(null);
  const [role, setRole] = useState('tenant');
  const navigate = useNavigate();

  const handleRegister = (e) => {
    e.preventDefault();
    authService.register(username, email, password, phoneNumber, permanentAddress, idProof, profilePhoto, role).then(
      () => {
        navigate('/login');
      },
      (error) => {
        console.log(error);
        alert('Registration failed');
      }
    );
  };

  return (
    <form onSubmit={handleRegister}>
      <div>
        <label>Username:</label>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </div>
      <div>
        <label>Phone Number:</label>
        <input type="text" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} required />
      </div>
      <div>
        <label>Permanent Address:</label>
        <textarea value={permanentAddress} onChange={(e) => setPermanentAddress(e.target.value)} required />
      </div>
      <div>
        <label>ID Proof:</label>
        <input type="file" onChange={(e) => setIdProof(e.target.files[0])} required />
      </div>
      <div>
        <label>Profile Photo:</label>
        <input type="file" onChange={(e) => setProfilePhoto(e.target.files[0])} />
      </div>
      <div>
        <label>Role:</label>
        <select value={role} onChange={(e) => setRole(e.target.value)} required>
          <option value="tenant">Tenant</option>
          <option value="owner">Owner</option>
        </select>
      </div>
      <button type="submit">Register</button>
    </form>
  );
};

export default Register;
