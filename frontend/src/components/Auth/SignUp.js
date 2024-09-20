import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Box, Paper } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function SignUp() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/signup`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password }),
      });

      const data = await response.json();
      if (data.success) {
        alert('Sign up successful! Please wait for admin approval.');
        navigate('/signin');
      } else {
        alert('Sign up failed.');
      }
    } catch (error) {
      console.error("Error during sign-up", error);
    }
  };

  return (
    <Container maxWidth="sm" sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'linear-gradient(to right, #6a11cb, #2575fc)', borderRadius: 2 }}>
      <Paper elevation={10} sx={{ padding: 4, borderRadius: 3, width: '100%', background: '#f7f9fc' }}>
        <Box sx={{ mb: 4, textAlign: 'center' }}>
          <Typography variant="h4" component="h1" gutterBottom sx={{ color: '#6a11cb' }}>
            Create Your Account
          </Typography>
          <Typography variant="subtitle1">
            Fill out the details to get started
          </Typography>
        </Box>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Full Name"
            fullWidth
            margin="normal"
            variant="outlined"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            sx={{ backgroundColor: '#fff', borderRadius: 2 }}
          />
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
            Sign Up
          </Button>
        </form>
        <Typography variant="body2" sx={{ mt: 3, textAlign: 'center' }}>
          Already have an account? <a href="/signin" style={{ color: '#6a11cb', textDecoration: 'none' }}>Sign In</a>
        </Typography>
      </Paper>
    </Container>
  );
}

export default SignUp;
