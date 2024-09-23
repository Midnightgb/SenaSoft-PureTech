<!-- src/components/common/SearchBar.vue -->
<template>
  <form @submit.prevent="handleSearch" class="hidden md:block md:pl-2">

      <div class="max-w-lg w-full lg:max-w-xs">
        <label for="search" class="sr-only">Buscar</label>
        <div class="relative">
          <div
            class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
          >
            <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" />
          </div>
          <input
            id="search"
            name="search"
            class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white dark:bg-gray-700 placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Buscar"
            type="search"
          />
        </div>
      </div>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { MagnifyingGlassIcon } from "@heroicons/vue/24/outline";
const searchQuery = ref("");

const handleSearch = () => {
  // Implement search functionality
  console.log("Searching for:", searchQuery.value);
};
</script>
