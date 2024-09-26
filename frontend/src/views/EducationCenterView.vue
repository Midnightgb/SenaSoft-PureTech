<template>
  <div class="flex flex-col h-screen w-screen bg-green-50 dark:bg-gray-900">
    <header class="p-4 bg-green-500 dark:bg-green-700 text-white flex items-center">
      <h1 class="text-xl font-bold">Education Center</h1>
    </header>
    <main class="flex-1 overflow-auto p-4 scrollbar-hide">
      <div class="mb-4 relative">
        <input
          type="search"
          placeholder="Search materials..."
          class="w-full p-2 pl-10 border border-green-300 dark:border-green-700 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 dark:focus:ring-green-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
        />
        <SearchIcon class="absolute left-3 top-2.5 h-5 w-5 text-green-400 dark:text-green-500" />
      </div>
      <ul class="bg-white dark:bg-gray-800 rounded-lg shadow divide-y divide-green-100 dark:divide-green-800">
        <li 
          v-for="material in materials" 
          :key="material" 
          class="p-4 flex items-center justify-between hover:bg-green-50 dark:hover:bg-green-900 cursor-pointer text-gray-900 dark:text-white"
        >
          <span>{{ material }}</span>
          <ChevronRightIcon class="h-5 w-5 text-green-400 dark:text-green-500" />
        </li>
      </ul>         
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ArrowLeftIcon, SearchIcon, ChevronRightIcon, BookOpenIcon } from 'lucide-vue-next'

const materials = ref(['Paper', 'Plastic', 'Glass', 'Metal'])
</script>

<style scoped>
/* Styles for hiding scrollbar */
.scrollbar-hide {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;  /* Chrome, Safari and Opera */
}
</style>