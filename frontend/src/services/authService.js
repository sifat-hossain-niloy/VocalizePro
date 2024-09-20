const API_URL = process.env.REACT_APP_API_URL;

export const login = async (credentials) => {
  const response = await fetch(`${API_URL}/auth/signin`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(credentials),
  });
  
  if (!response.ok) {
    throw new Error('Login failed');
  }
  
  return await response.json();
};

export const signup = async (userDetails) => {
  const response = await fetch(`${API_URL}/auth/signup`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userDetails),
  });
  
  if (!response.ok) {
    throw new Error('Signup failed');
  }
  
  return await response.json();
};

export const validateUser = async (userId) => {
  const response = await fetch(`${API_URL}/admin/validate/${userId}`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
  });
  
  if (!response.ok) {
    throw new Error('User validation failed');
  }
  
  return await response.json();
};
