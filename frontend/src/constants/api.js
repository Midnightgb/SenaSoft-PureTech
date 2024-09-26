// src/constants/apiEndpoints.js
const BASE_URL = import.meta.env.VITE_API_URL;
const BASE_AUTH = `${BASE_URL}/auth`;
console.log('API URL:', import.meta.env.VITE_API_URL);
export const API_ENDPOINTS = {
  // Autenticación
  LOGIN: `${BASE_AUTH}/token`,
  LOGOUT: `${BASE_AUTH}/logout`,


  // Usuarios
  USERS: `${BASE_AUTH}/users`,
  REGISTER: `${BASE_AUTH}/register`,
  RECYCLING_MAP: `${BASE_URL}/recycling-map`,
  REGISTER_RECYCLING: `${BASE_URL}/recycling/register`,
  MATERIALS: `${BASE_URL}/material`,

};
