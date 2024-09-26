import axios from "axios";
import { API_ENDPOINTS } from "@/constants/api";

export const publicApi = axios.create({
  baseURL: API_ENDPOINTS.BASE_URL,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

export const apiClient = axios.create({
  baseURL: API_ENDPOINTS.BASE_URL,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer`,
  },
});

export const login = async (credentials) => {
  const urlEncodedCredentials = new URLSearchParams();
  for (const key in credentials) {
    urlEncodedCredentials.append(key, credentials[key]);
  }
  try {
    const response = await publicApi.post(
      API_ENDPOINTS.LOGIN,
      urlEncodedCredentials,
      {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }
    );
    return {
      success: true,
      data: response.data,
    };
  } catch (error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      return { success: false, error: error.response.data.detail || "Error de autenticación" };
    } else if (error.request) {
      // The request was made but no response was received
      return { success: false, error: "No se recibió respuesta del servidor" };
    } else {
      // Something happened in setting up the request that triggered an Error
      return { success: false, error: "Error al realizar la solicitud" };
    }
  }
};

export const logout = async () => {
  try {
    const response = await apiClient.post(API_ENDPOINTS.LOGOUT);
    return {
      success: true,
      data: response.data,
    };
  } catch (error) {
    return { success: false, error: "Error al cerrar sesión" };
  }
}
