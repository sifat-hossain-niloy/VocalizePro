import React, { useState } from 'react';
import { Button, Box, Typography, Snackbar, Alert } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

function UploadPDF({ onUploadComplete }) {
  const [files, setFiles] = useState(null);
  const [snackbarOpen, setSnackbarOpen] = useState(false);

  const handleFileChange = (e) => {
    setFiles(e.target.files);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append('files', files[i]);
    }
    await fetch(`${process.env.REACT_APP_API_URL}/api/admin/upload_pdf`, {
      method: 'POST',
      body: formData,
    });
    setSnackbarOpen(true);
    setFiles(null);  // Clear file selection after upload
    onUploadComplete();  // Trigger parent function to refresh file list
  };

  const handleSnackbarClose = () => {
    setSnackbarOpen(false);
  };

  return (
    <Box 
      component="form" 
      onSubmit={handleSubmit} 
      sx={{ mt: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}
    >
      <Button
        variant="contained"
        component="label"
        color="primary"
        startIcon={<CloudUploadIcon />}
        sx={{ mb: 2 }}
      >
        Choose PDFs
        <input
          type="file"
          multiple
          hidden
          onChange={handleFileChange}
          accept="application/pdf"
        />
      </Button>

      {files && (
        <Box sx={{ mb: 2 }}>
          <Typography variant="body2">
            {files.length} file(s) selected
          </Typography>
        </Box>
      )}

      <Button 
        type="submit" 
        variant="contained" 
        color="secondary" 
        sx={{ mt: 2 }}
      >
        Upload PDFs
      </Button>

      <Snackbar
        open={snackbarOpen}
        autoHideDuration={3000}
        onClose={handleSnackbarClose}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert onClose={handleSnackbarClose} severity="success" sx={{ width: '100%' }}>
          Files uploaded successfully!
        </Alert>
      </Snackbar>
    </Box>
  );
}

export default UploadPDF;
