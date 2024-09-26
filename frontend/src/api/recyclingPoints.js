import axios from 'axios';

export const getRecyclingPoints = async (skip = 0, limit = 10) => {
  try {
    const response = await axios.get(`https://puretech-api.javm.tech/recycling_point/?skip=${skip}&limit=${limit}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching recycling points:', error);
    throw error;
  }
};