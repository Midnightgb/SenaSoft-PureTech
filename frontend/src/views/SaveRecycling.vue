<template>
  <div class="flex flex-col h-screen w-screen bg-green-50">
    <header class="p-4 bg-green-500 text-white flex items-center">
      <h1 class="text-xl font-bold">Recycling Submission</h1>
    </header>
    <main class="flex-1 overflow-auto p-4">
      <form @submit.prevent="submitForm" class="bg-white rounded-lg p-6 shadow">
        <h2 class="text-lg font-semibold mb-4">Submit Recycling Data</h2>
        
  
        <div class="mb-4">
          <label for="weight" class="block text-sm font-medium text-gray-700">Weight</label>
          <input type="number" id="weight" v-model="formData.weight" step="0.01" required
                 class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500">
        </div>
        
        <div class="mb-4">
          <label for="date" class="block text-sm font-medium text-gray-700">Date</label>
          <input type="date" id="date" v-model="formData.date" required
                 class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500">
        </div>            
        
        <div class="mb-6">
          <label for="recycling_point_id" class="block text-sm font-medium text-gray-700">Recycling Point ID</label>
          <input type="number" id="recycling_point_id" v-model="formData.recycling_point_id" required
                 class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-green-500 focus:ring-green-500">
        </div>
        
        <div class="flex items-center justify-end">
          <button type="submit"
                  class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Submit Recycling Data
          </button>
        </div>
      </form>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        user_id: null,
        material_id: null,
        weight: null,
        date: new Date().toISOString().split('T')[0],
        earned_points: null,
        recycling_point_id: null
      }
    }
  },
  methods: {
    submitForm() {
      // Here you would typically send the formData to your backend API
      console.log('Form submitted:', this.formData);
      // Reset form after submission
      this.formData = {
        user_id: null,
        material_id: null,
        weight: null,
        date: new Date().toISOString().split('T')[0],
        earned_points: null,
        recycling_point_id: null
      };
      // You could also add some feedback to the user here
    }
  }
}
</script>