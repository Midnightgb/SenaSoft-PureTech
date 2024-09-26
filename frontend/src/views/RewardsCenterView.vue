
<template>
  <div class="flex flex-col h-screen w-screen bg-green-50 dark:bg-gray-900 transition-colors duration-200">

    <main class="flex-1 overflow-auto p-4">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow mb-4 transition-colors duration-200">
        <h2 class="text-lg font-semibold mb-2 dark:text-white">Your Points</h2>
        <p class="text-3xl font-bold text-green-500 dark:text-green-400">1,250</p>
      </div>
      <h2 class="text-lg font-semibold mb-2 dark:text-white">Available Rewards</h2>
      <ul class="space-y-4">
        <li
          v-for="(reward, index) in [
            { name: '$5 Gift Card', description: 'Local Eco-Store', points: 500 },
            { name: 'Reusable Water Bottle', description: 'EcoConnect Branded', points: 750 },
            { name: 'Eco-Friendly T-Shirt', description: 'Made from Recycled Materials', points: 1000 },
            { name: 'Tree Planting Kit', description: 'Plant Your Own Tree', points: 1200 },
          ]"
          :key="index"
          class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow flex items-center justify-between transition-colors duration-200"
        >
          <div class="flex items-center">
            <GiftIcon class="h-8 w-8 text-green-500 dark:text-green-400 mr-3" />
            <div>
              <h3 class="font-semibold dark:text-white">{{ reward.name }}</h3>
              <p class="text-sm text-gray-500 dark:text-gray-400">{{ reward.description }}</p>
            </div>
          </div>
          <button class="bg-green-500 dark:bg-green-600 text-white px-3 py-1 rounded-md text-sm hover:bg-green-600 dark:hover:bg-green-700 transition-colors duration-200">
            {{ reward.points }} pts
          </button>
        </li>
      </ul>
    </main>
  </div>
</template>