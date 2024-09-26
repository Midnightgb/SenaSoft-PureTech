import { API_ENDPOINTS } from "@/cons-tants/api";
import publicApi from './api';

export const sendRecyclingMapData = async (mapData) => {
  try {
    const response = await publicApi.post(API_ENDPOINTS.RECYCLING_MAP, mapData);
    return response.data;
  } catch (error) {
    console.error('Error sending recycling map data:', error);
    throw error;
  }
};

export const getRecyclingPoints = async () => {
  try {
    const response = await axios.get(API_ENDPOINTS.RECYCLING_MAP);
    return response.data;
  } catch (error) {
    console.error('Error fetching recycling points:', error);
    throw error;
  }
};