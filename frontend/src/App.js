import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import SignIn from './components/Auth/SignIn';
import AdminDashboard from './pages/AdminDashboard';
import UserChat from './pages/UserChat';
import Navbar from './components/Navbar'; // Import the Navbar component

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Check if a user is already logged in from localStorage
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const handleSetUser = (userData) => {
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData)); // Store user data in localStorage
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem('user'); // Clear localStorage on logout
  };

  return (
    <Router>
      {/* Conditionally render the Navbar only when a user is logged in */}
      {user && <Navbar user={user} onLogout={handleLogout} />}
      <Routes>
        <Route path="/signin" element={<SignIn setUser={handleSetUser} />} />

        {/* Protected routes based on user role */}
        <Route 
          path="/admin" 
          element={user?.role === 'admin' ? <AdminDashboard /> : <Navigate to="/signin" />} 
        />
        <Route 
          path="/chat" 
          element={user?.role === 'user' ? <UserChat /> : <Navigate to="/signin" />} 
        />

        {/* Default route redirect to Sign In */}
        <Route path="/" element={<Navigate to="/signin" />} />
        <Route path="/signup" element={<Navigate to  = "/signup"/>} />

      </Routes>
    </Router>
  );
}

export default App;
