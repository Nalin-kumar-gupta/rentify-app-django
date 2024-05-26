import React from 'react';
import './styles.scss'; // Import SCSS file
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from './components/Navbar';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import PropertyDetails from './components/propertyDetail';

import authService from './services/authService';

function App() {
    return (
        <BrowserRouter>
            <div>
                <Navbar />
                <Routes>
                    {/* <Route path = "/" element={<PrivateRoute exact path="/" component={Home} />}/> */}
                    <Route
                        path="/"
                        element={
                            authService.getCurrentUser() ? (
                                <Home />
                            ) : (
                                <Navigate to="/login" />
                            )
                        }
                    />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/properties/:id" element={<PropertyDetails />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
