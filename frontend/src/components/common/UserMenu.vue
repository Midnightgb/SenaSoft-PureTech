<!-- src/components/common/UserMenu.vue -->
<template>
  <div>
    <button
      @click="toggleUserMenu"
      class="max-w-xs bg-white dark:bg-gray-800 flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      id="user-menu"
      aria-expanded="false"
      aria-haspopup="true"
    >
      <span class="sr-only">Abrir menú de usuario</span>
      <img
        class="h-8 w-8 rounded-full"
        src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
        alt=""
      />
    </button>
  </div>
  <!-- Menú desplegable del usuario -->
  <transition
    enter-active-class="transition ease-out duration-100"
    enter-from-class="transform opacity-0 scale-95"
    enter-to-class="transform opacity-100 scale-100"
    leave-active-class="transition ease-in duration-75"
    leave-from-class="transform opacity-100 scale-100"
    leave-to-class="transform opacity-0 scale-95"
  >
    <div
      v-if="isUserMenuOpen"
      class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white dark:bg-gray-700 ring-1 ring-black ring-opacity-5"
      role="menu"
      aria-orientation="vertical"
      aria-labelledby="user-menu"
    >
      <button @click="openProfile"
        href="#"
        class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-600"
        role="menuitem"
        >Tu Perfil</button
      >
      <a
        href="#"
        class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-600"
        role="menuitem"
        >Configuración</a
      >
      <a
        href="#"
        class="block px-4 py-2 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-600"
        role="menuitem"
        >Cerrar sesión</a
      >
    </div>
  </transition>
</template>

<script setup>
import { ref } from "vue";

const isUserMenuOpen = ref(false);

const toggleUserMenu = () => {
  isUserMenuOpen.value = !isUserMenuOpen.value;
};

const openProfile = () => {
  router.push("/Profile");
  closeSidebar();
};
</script>
