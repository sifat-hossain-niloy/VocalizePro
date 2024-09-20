import React from 'react';
import { Container, Box, Typography } from '@mui/material';
import Chat from '../components/User/Chat';

function UserChat() {
  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4 }}>
        {/* <Typography variant="h4" gutterBottom>
          Ask a Question
        </Typography> */}
        <Chat />
      </Box>
    </Container>
  );
}

export default UserChat;
