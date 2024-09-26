<template>
  <div class="flex flex-col h-screen w-screen bg-green-50 dark:bg-gray-900">
    <header class="p-4 bg-green-500 dark:bg-green-700 text-white flex items-center">
      <h1 class="text-xl font-bold">Your EcoConnect Impact</h1>
    </header>
    <main class="flex-1 overflow-auto p-4 scrollbar-hide">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow mb-4">
        <h2 class="text-lg font-semibold mb-2 dark:text-white">Total Impact</h2>
        <div class="grid grid-cols-2 gap-4">
          <div class="text-center">
            <p class="text-3xl font-bold text-green-500 dark:text-green-400">127.5 kg</p>
            <p class="text-sm text-gray-500 dark:text-gray-400">CO2 Avoided</p>
          </div>
          <div class="text-center">
            <p class="text-3xl font-bold text-green-500 dark:text-green-400">8</p>
            <p class="text-sm text-gray-500 dark:text-gray-400">Trees Saved</p>
          </div>
        </div>
      </div>
      <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow mb-4">
        <h2 class="text-lg font-semibold mb-2 dark:text-white">Recycling Breakdown</h2>
        <div class="flex justify-around items-center h-40">
          <div v-for="material in materials" :key="material.type" class="text-center">
            <svg class="h-10 w-10 mb-2" :class="material.iconColor" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
            <p class="font-semibold dark:text-white">{{ material.amount }} kg</p>
            <p class="text-sm text-gray-500 dark:text-gray-400">{{ material.type }}</p>
          </div>
        </div>
      </div>
      <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow mb-4">
        <h2 class="text-lg font-semibold mb-2 dark:text-white">Environmental Impact</h2>
        <div class="flex justify-around items-center h-40">
          <div v-for="impact in environmentalImpact" :key="impact.type" class="text-center">
            <component :is="impact.icon" :class="['h-10 w-10 mb-2', impact.iconColor]" />
            <p class="font-semibold dark:text-white">{{ impact.amount }} {{ impact.unit }}</p>
            <p class="text-sm text-gray-500 dark:text-gray-400">{{ impact.type }}</p>
          </div>
        </div>
      </div>
      <button class="w-full bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700 text-white p-2 rounded-md font-medium flex items-center justify-center">
        <svg class="h-5 w-5 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
        </svg>
        Share Your EcoConnect Impact
      </button>
    </main>
  </div>
</template>

<script>
export default {
  name: 'YourImpactView',
  components: {
    TreeIcon: {
      template: `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M7 18v-5.25A2.75 2.75 0 019.75 10h4.5A2.75 2.75 0 0117 12.75V18m0 0h4v-4a3 3 0 00-3-3h-1M7 18H3v-4a3 3 0 013-3h1m0 0V3.75A2.75 2.75 0 019.75 1h4.5A2.75 2.75 0 0117 3.75V11" />
        </svg>
      `
    },
    WaterDropIcon: {
      template: `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M20 14.66V20a2 2 0 01-2 2H4a2 2 0 01-2-2v-5.34a2 2 0 01.23-.92l4-7.1a2 2 0 013.54 0l4 7.1a2 2 0 01.23.92zM6.7 18h10.6" />
        </svg>
      `
    }
  },
  data() {
    return {
      materials: [
        { type: 'Plastic', amount: 45, iconColor: 'text-blue-500 dark:text-blue-400' },
        { type: 'Paper', amount: 30, iconColor: 'text-yellow-500 dark:text-yellow-400' },
        { type: 'Metal', amount: 20, iconColor: 'text-gray-500 dark:text-gray-400' }
      ],
      environmentalImpact: [
        { type: 'Land Preserved', amount: 50, unit: 'm²', icon: 'TreeIcon', iconColor: 'text-green-500 dark:text-green-400' },
        { type: 'Water Saved', amount: 1000, unit: 'L', icon: 'WaterDropIcon', iconColor: 'text-blue-500 dark:text-blue-400' }
      ]
    };
  }
};
</script>
<style>
/* Estilos para ocultar la barra de desplazamiento */
.scrollbar-hide {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;  /* Chrome, Safari and Opera */
}
</style>