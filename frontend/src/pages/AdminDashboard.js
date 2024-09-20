import React, { useEffect, useState } from 'react';
import { 
  Container, Box, Typography, Button, Paper, List, 
  ListItem, ListItemText, Divider, IconButton, Card, 
  CardContent, CardActions, Grid 
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import UploadPDF from '../components/Admin/UploadPDF';

function AdminDashboard() {
  const [files, setFiles] = useState([]);

  const fetchFiles = async () => {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/admin/files`);
    const data = await response.json();
    setFiles(data.files);
  };

  useEffect(() => {
    fetchFiles();  // Fetch files on component mount
  }, []);

  const handleDelete = async (filename) => {
    await fetch(`${process.env.REACT_APP_API_URL}/api/admin/files/${filename}`, {
      method: 'DELETE',
    });
    fetchFiles();  // Refresh file list after deletion
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, background: 'linear-gradient(to right, #6a11cb, #2575fc)', p: 3, borderRadius: 3 }}>
      <Box textAlign="center" sx={{ mb: 4, color: '#fff' }}>
        <Typography variant="h3" component="h1" gutterBottom>
          Admin Dashboard
        </Typography>
        <Typography variant="h6" color="inherit">
          Manage uploaded PDFs
        </Typography>
      </Box>

      <Grid container spacing={3}>
        {/* Uploaded Files Section */}
        <Grid item xs={12} md={6}>
          <Paper elevation={6} sx={{ p: 3, borderRadius: 2, background: '#f7f9fc' }}>
            <Typography variant="h5" gutterBottom>
              Uploaded Files
            </Typography>
            <Divider sx={{ mb: 2 }} />
            <List>
              {files.length === 0 ? (
                <Typography variant="body1" color="textSecondary">
                  No files uploaded.
                </Typography>
              ) : (
                files.map((file, index) => (
                  <Card key={index} variant="outlined" sx={{ mb: 2 }}>
                    <CardContent>
                      <Typography variant="h6" color="textPrimary">
                        {file}
                      </Typography>
                    </CardContent>
                    <CardActions>
                      <Button
                        startIcon={<DeleteIcon />}
                        variant="outlined"
                        color="error"
                        onClick={() => handleDelete(file)}
                        fullWidth
                      >
                        Delete
                      </Button>
                    </CardActions>
                  </Card>
                ))
              )}
            </List>
          </Paper>
        </Grid>

        {/* Upload PDFs Section */}
        <Grid item xs={12} md={6}>
          <Paper elevation={6} sx={{ p: 3, borderRadius: 2, background: '#f7f9fc' }}>
            <Typography variant="h5" gutterBottom>
              Upload PDFs
            </Typography>
            <Divider sx={{ mb: 2 }} />
            <UploadPDF onUploadComplete={fetchFiles} />
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}

export default AdminDashboard;
