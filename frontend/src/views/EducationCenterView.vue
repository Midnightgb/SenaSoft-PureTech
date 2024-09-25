<template>
    <div class="flex flex-col h-screen w-screen bg-green-50">
      <header class="p-4 bg-green-500 text-white flex items-center">
        <h1 class="text-xl font-bold">Education Center</h1>
      </header>
      <main class="flex-1 overflow-auto p-4">
        <div class="mb-4 relative">
          <input
            type="search"
            placeholder="Search materials..."
            class="w-full p-2 pl-10 border border-green-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
          />
          <SearchIcon class="absolute left-3 top-2.5 h-5 w-5 text-green-400" />
        </div>
        <ul class="bg-white rounded-lg shadow divide-y divide-green-100">
          <li v-for="material in materials" :key="material" class="p-4 flex items-center justify-between hover:bg-green-50 cursor-pointer">
            <span>{{ material }}</span>
            <ChevronRightIcon class="h-5 w-5 text-green-400" />
          </li>
        </ul>
        <div class="mt-4 bg-white rounded-lg p-4 shadow border border-green-200">
          <h2 class="text-lg font-semibold mb-2 text-green-800">Recycling Quiz</h2>
          <p class="text-sm mb-2 text-green-600">Test your knowledge and earn points!</p>
          <button class="w-full bg-green-500 hover:bg-green-600 text-white p-2 rounded-md font-medium flex items-center justify-center transition duration-300">
            <BookOpenIcon class="h-5 w-5 mr-2" />
            Start Quiz
          </button>
        </div>
      </main>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { ArrowLeftIcon, SearchIcon, ChevronRightIcon, BookOpenIcon } from 'lucide-vue-next'
  
  const materials = ref(['Paper', 'Plastic', 'Glass', 'Metal'])
  </script>
  
  <style scoped>
  /* Add any additional component-specific styles here */
  </style>