// src/constants/apiEndpoints.js
const BASE_URL = import.meta.env.VITE_API_URL;
const BASE_AUTH = `${BASE_URL}/auth`;
console.log('API URL:', import.meta.env.VITE_API_URL);
export const API_ENDPOINTS = {
  // Autenticación
  LOGIN: `${BASE_AUTH}/login`,
  LOGOUT: `${BASE_AUTH}/logout`,
};
