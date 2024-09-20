import React from 'react';
import { AppBar, Toolbar, Button, Typography, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function Navbar({ user, onLogout }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    onLogout();
    navigate('/signin'); // Redirect to sign-in after logout
  };

  return (
    <AppBar
      position="static"
      sx={{
        background: 'linear-gradient(to right, #6a11cb, #2575fc)', // Consistent gradient
        mb: 4,
      }}
    >
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1, fontWeight: 'bold' }}>
          VOCALIZEPRO : {user?.role === 'admin' ? 'Admin' : 'User'}
        </Typography>
        {user && (
          <Button
            variant="outlined"
            sx={{
              color: '#fff',
              borderColor: '#fff',
              '&:hover': {
                borderColor: '#ddd', // Subtle change on hover
              },
            }}
            onClick={handleLogout}
          >
            Logout
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
