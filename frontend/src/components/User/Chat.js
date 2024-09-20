import React, { useState } from 'react';
import { TextField, Button, Box, Typography, Paper, CircularProgress, Snackbar, Alert, IconButton } from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import PauseIcon from '@mui/icons-material/Pause';
import SendIcon from '@mui/icons-material/Send';

function Chat() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');
  const [audioUrl, setAudioUrl] = useState(null);
  const [audio, setAudio] = useState(null); // Store the audio object
  const [isPlaying, setIsPlaying] = useState(false); // Track if audio is playing
  const [loading, setLoading] = useState(false); // Loading state
  const [openSnackbar, setOpenSnackbar] = useState(false); // Snackbar state

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`${process.env.REACT_APP_API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setResponse(data.answer.text);
      setAudioUrl(data.answer.audio_url);
      setOpenSnackbar(true); // Show snackbar

      // Reset audio if a new question is asked
      if (audio) {
        audio.pause();
        setAudio(null);
        setIsPlaying(false);
      }
    } catch (error) {
      console.error("Error fetching response:", error);
    }
    setLoading(false);
  };

  const handlePlayAudio = () => {
    if (!isPlaying && audioUrl) {
      const audioObj = new Audio(audioUrl);
      audioObj.play();
      setAudio(audioObj);
      setIsPlaying(true);

      audioObj.onended = () => {
        setIsPlaying(false); // Reset state when audio ends
      };
    }
  };

  const handlePauseAudio = () => {
    if (audio) {
      audio.pause();
      setIsPlaying(false);
    }
  };

  const handleCloseSnackbar = () => {
    setOpenSnackbar(false);
  };

  return (
    <Box
      sx={{
        mt: 4,
        p: 3,
        borderRadius: 3,
        background: 'linear-gradient(to right, #6a11cb, #2575fc)',
        boxShadow: 3,
        maxWidth: '600px',
        mx: 'auto',
        textAlign: 'center',
        color: '#fff'
      }}
    >
      <Typography variant="h4" sx={{ mb: 3 }}>
        Ask Your Question
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Type your question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          fullWidth
          required
          margin="normal"
          variant="filled"
          sx={{ backgroundColor: '#fff', borderRadius: 2 }}
        />
        <Button
          type="submit"
          variant="contained"
          fullWidth
          sx={{
            mt: 2,
            py: 1.5,
            fontWeight: 'bold',
            fontSize: '16px',
            backgroundColor: '#f7f9fc',
            color: '#6a11cb', // Adjusted button text color
            '&:hover': {
              backgroundColor: '#e0e0e0', // Lighter hover effect
            },
          }}
          disabled={loading}
          endIcon={loading ? <CircularProgress size={24} color="inherit" /> : <SendIcon />}
        >
          {loading ? 'Asking...' : 'Ask'}
        </Button>
      </form>

      {response && (
        <Box sx={{ mt: 4 }}>
          <Paper elevation={3} sx={{ p: 3, background: '#f7f9fc', borderRadius: 3 }}>
            <Typography variant="h6" gutterBottom>
              Response:
            </Typography>
            <Typography sx={{ mb: 2 }}>{response}</Typography>

            {audioUrl && (
              <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
                <IconButton
                  onClick={handlePlayAudio}
                  color="secondary"
                  disabled={isPlaying}
                  sx={{ mr: 2 }}
                >
                  <PlayArrowIcon fontSize="large" />
                </IconButton>
                <IconButton
                  onClick={handlePauseAudio}
                  color="warning"
                  disabled={!isPlaying}
                >
                  <PauseIcon fontSize="large" />
                </IconButton>
              </Box>
            )}
          </Paper>
        </Box>
      )}

      <Snackbar
        open={openSnackbar}
        autoHideDuration={3000}
        onClose={handleCloseSnackbar}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert onClose={handleCloseSnackbar} severity="success">
          Response received!
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default Chat;
