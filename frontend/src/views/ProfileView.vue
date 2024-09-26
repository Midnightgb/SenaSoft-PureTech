<template>
  <div
    class="flex flex-col h-screen w-screen bg-green-50 dark:bg-gray-900 transition-colors duration-200"
  >
    <main class="flex-1 overflow-auto p-4">
      <div
        class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow mb-4 text-center transition-colors duration-200"
      >
        <img
          src="/img/placeholder.svg"
          alt="Profile"
          class="w-24 h-24 rounded-full mx-auto mb-2"
        />
        <h2 class="text-xl font-semibold dark:text-white">Jane Doe</h2>
        <p class="text-gray-500 dark:text-gray-400">Eco Warrior</p>
      </div>
      <div
        class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow mb-4 transition-colors duration-200"
      >
        <h3
          class="text-lg font-semibold mb-2 flex items-center dark:text-white"
        >
          <AwardIcon class="h-5 w-5 mr-2 text-yellow-500" />
          Achievements
        </h3>
        <div class="flex flex-wrap gap-2">
          <div
            class="bg-gray-100 dark:bg-gray-700 p-2 rounded-md text-sm dark:text-gray-300 transition-colors duration-200"
          >
            Paper Master
          </div>
          <div
            class="bg-gray-100 dark:bg-gray-700 p-2 rounded-md text-sm dark:text-gray-300 transition-colors duration-200"
          >
            Plastic Pro
          </div>
          <div
            class="bg-gray-100 dark:bg-gray-700 p-2 rounded-md text-sm dark:text-gray-300 transition-colors duration-200"
          >
            Glass Guru
          </div>
        </div>
      </div>
      <div
        class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow transition-colors duration-200"
      >
        <h3
          class="text-lg font-semibold mb-2 flex items-center dark:text-white"
        >
          <HistoryIcon class="h-5 w-5 mr-2 text-blue-500" />
          Recycling History
        </h3>
        <ul class="space-y-2">
          <li class="flex justify-between items-center">
            <span class="dark:text-white">Paper (2kg)</span>
            <span class="text-sm text-gray-500 dark:text-gray-400"
              >2 days ago</span
            >
          </li>
          <li class="flex justify-between items-center">
            <span class="dark:text-white">Plastic (1kg)</span>
            <span class="text-sm text-gray-500 dark:text-gray-400"
              >5 days ago</span
            >
          </li>
          <li class="flex justify-between items-center">
            <span class="dark:text-white">Glass (3kg)</span>
            <span class="text-sm text-gray-500 dark:text-gray-400"
              >1 week ago</span
            >
          </li>
        </ul>
      </div>
    </main>
  </div>
</template>
