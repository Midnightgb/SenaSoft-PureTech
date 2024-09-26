<template>
  <div class="flex flex-col h-screen w-screen bg-green-50">
    <header class="p-4 bg-green-500 text-white flex items-center">
      <h1 class="text-xl font-bold">Recycling Submission</h1>
    </header>
    <main class="flex-1 overflow-auto p-4">
      <form @submit.prevent="submitForm" class="bg-white rounded-lg p-6 shadow">
        <h2 class="text-lg font-semibold mb-4">Submit Recycling Data</h2>

        <div v-if="errorMessage" class="mb-4 p-2 bg-red-100 text-red-700 rounded">
          {{ errorMessage }}
        </div>

        <div v-if="successMessage" class="mb-4 p-2 bg-green-100 text-green-700 rounded">
          {{ successMessage }}
        </div>

        <div class="mb-4">
          <label for="material_id" class="block text-sm font-medium text-gray-700">Material</label>
          <select
            id="material_id"
            v-model="formData.material_id"
            required
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500"
          >
            <option value="" selected disabled>Select a material</option>
            <option v-for="material in materials" :key="material.id" :value="material.id">
              {{ material.name }} ({{ material.points_per_kg }} points/kg)
            </option>
          </select>
        </div>

        <div class="mb-4">
          <label for="weight" class="block text-sm font-medium text-gray-700">Weight (kg)</label>
          <input
            type="number"
            id="weight"
            v-model="formData.weight"
            step="0.01"
            required
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500"
          />
        </div>

        <div class="mb-4">
          <label for="date" class="block text-sm font-medium text-gray-700">Date</label>
          <input
            type="date"
            id="date"
            v-model="formData.date"
            required
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500"
          />
        </div>

        <div class="mb-6 hidden">
          <label for="recycling_point_id" class="block text-sm font-medium text-gray-700">Recycling Point ID</label>
          <input
            type="number"
            id="recycling_point_id"
            v-model="formData.recycling_point_id"
            required
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500"
          />
        </div>

        <div class="mb-4">
          <p class="text-sm font-medium text-gray-700">Estimated Points: {{ calculatePoints }}</p>
        </div>

        <div class="flex items-center justify-end">
          <button
            type="submit"
            class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Submit Recycling Data
          </button>
        </div>
      </form>
    </main>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { apiClient } from '@/services/api';
import { API_ENDPOINTS } from "@/constants/api";

export default {
  setup() {
    const materials = ref([]);
    const formData = ref({
      user_id: 9,
      material_id: null,
      weight: null,
      date: new Date().toISOString().split("T")[0],
      earned_points: 0,
      recycling_point_id: 7,
    });
    
    const errorMessage = ref('');
    const successMessage = ref('');

    const fetchMaterials = async () => {
      try {
        const response = await apiClient.get(API_ENDPOINTS.MATERIALS);
        materials.value = response.data;
        console.log('Materials fetched:', materials.value);
        
      } catch (error) {
        console.error('Error fetching materials:', error);
        errorMessage.value = 'Failed to fetch materials. Please try again.';
      }
    };

    const calculatePoints = computed(() => {
      if (formData.value.material_id && formData.value.weight) {
        const selectedMaterial = materials.value.find(m => m.id === formData.value.material_id);
        if (selectedMaterial) {
          return Math.floor(formData.value.weight * selectedMaterial.points_per_kg);
        }
      }
      return 0;
    });

    const submitForm = async () => {
      try {
        formData.value.user_id = 9;
        formData.value.earned_points = calculatePoints.value;
        console.log('formData:', formData.value);

        const response = await apiClient.post(API_ENDPOINTS.REGISTER_RECYCLING, formData.value);
        console.log('Recycling submitted:', response.data);
        successMessage.value = 'Recycling data submitted successfully!';
        // Reset form after successful submission
        formData.value = {
          user_id: null,
          material_id: null,
          weight: null,
          date: new Date().toISOString().split("T")[0],
          earned_points: 0,
          recycling_point_id: null,
        };
      } catch (error) {
        console.error('Error submitting recycling data:', error);
        errorMessage.value = error.response?.data?.detail || 'An error occurred while submitting the data';
      }
    };

    onMounted(() => {
      fetchMaterials();
    });

    return {
      formData,
      materials,
      errorMessage,
      successMessage,
      submitForm,
      calculatePoints,
    };
  },
};
</script>
