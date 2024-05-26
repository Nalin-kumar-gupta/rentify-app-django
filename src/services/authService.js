import axios from 'axios';

const API_URL = 'http://0.0.0.0:8000/api/';

const register = (username, email, password, phone_number, permanent_address, id_proof, profile_photo, role) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('email', email);
  formData.append('password', password);
  formData.append('phone_number', phone_number);
  formData.append('permanent_address', permanent_address);
  formData.append('id_proof', id_proof);
  if (profile_photo) {
    formData.append('profile_photo', profile_photo);
  }
  formData.append('role', role);

  return axios.post(API_URL + 'register/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

const login = (username, password) => {
  return axios
    .post(API_URL + 'token/', { username, password })
    .then((response) => {
      if (response.data.access) {
        localStorage.setItem('user', JSON.stringify(response.data));
      }
      return response.data;
    });
};

const logout = () => {
  localStorage.removeItem('user');
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem('user'));
};

const authService = {
  register,
  login,
  logout,
  getCurrentUser,
};

export default authService;
