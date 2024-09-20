import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Box, Paper } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function SignIn({ setUser }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  // Hardcoded demo credentials
  const adminEmail = 'admin@example.com';
  const adminPassword = 'adminpassword';
  const userEmail = 'user@example.com';
  const userPassword = 'userpassword';

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Check if the user is admin or regular user
    if (email === adminEmail && password === adminPassword) {
      setUser({ email, role: 'admin' });
      localStorage.setItem('user', JSON.stringify({ email, role: 'admin' }));
      navigate('/admin');
    } else if (email === userEmail && password === userPassword) {
      setUser({ email, role: 'user' });
      localStorage.setItem('user', JSON.stringify({ email, role: 'user' }));
      navigate('/chat');
    } else {
      alert('Invalid credentials');
    }
  };

  return (
    <Container maxWidth="sm" sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'linear-gradient(to right, #6a11cb, #2575fc)', borderRadius: 2 }}>
      <Paper elevation={10} sx={{ padding: 4, borderRadius: 3, width: '100%', background: '#f7f9fc' }}>
        <Box sx={{ mb: 4, textAlign: 'center' }}>
          <Typography variant="h4" component="h1" gutterBottom sx={{ color: '#6a11cb' }}>
            Welcome Back!
          </Typography>
          <Typography variant="subtitle1">
            Please sign in to continue
          </Typography>
        </Box>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Email"
            fullWidth
            margin="normal"
            variant="outlined"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            sx={{ backgroundColor: '#fff', borderRadius: 2 }}
          />
          <TextField
            label="Password"
            type="password"
            fullWidth
            margin="normal"
            variant="outlined"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            sx={{ backgroundColor: '#fff', borderRadius: 2 }}
          />
          <Button
            type="submit"
            variant="contained"
            color="primary"
            fullWidth
            sx={{ mt: 3, py: 1.5, fontSize: '1.1rem', fontWeight: 'bold', backgroundColor: '#6a11cb' }}
          >
            Sign In
          </Button>
        </form>
      </Paper>
    </Container>
  );
}

export default SignIn;
