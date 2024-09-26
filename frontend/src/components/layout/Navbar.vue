<!-- src/components/layout/Navbar.vue -->
<template>
  <nav class="bg-white dark:bg-gray-800 shadow-sm fixed w-full z-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <!-- Botón de hamburguesa para móviles -->
          <button
            @click="toggleSidebar"
            class="lg:hidden p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
          >
            <span class="sr-only">Abrir menú lateral</span>
            <Bars3Icon v-if="!isSidebarOpen" class="h-6 w-6" />
            <XMarkIcon v-else class="h-6 w-6" />
          </button>
          <!-- Logo -->
          <div class="flex-shrink-0 flex items-center">
            <img class="h-8 w-auto" src="/img/connect.png" alt="Logo de la empresa" />
          </div>
        </div>
        
        <!-- Iconos de la derecha -->
        <div class="flex items-center">
          <!-- Notificaciones -->
          <button
            @click="toggleNotifications"
            class="p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <span class="sr-only">Ver notificaciones</span>
            <BellIcon class="h-6 w-6" />
          </button>

          <!-- Alternar modo oscuro -->
          <DarkMode />

          <!-- Perfil de usuario -->
          <div class="ml-3 relative">
            <UserMenu />
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";

import { BellIcon, Bars3Icon, XMarkIcon } from "@heroicons/vue/24/outline";
import SearchBar from "@/components/common/SearchBar.vue";
import UserMenu from "@/components/common/UserMenu.vue";
import DarkMode from "@/components/common/DarkMode.vue";
import { useSidebar } from "@/composables/useSidebar";

const { isSidebarOpen, toggleSidebar } = useSidebar();
const isNotificationsOpen = ref(false);

const toggleNotifications = () => {
  isNotificationsOpen.value = !isNotificationsOpen.value;
};
</script>
