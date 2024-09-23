<!-- src/components/layout/Sidebar.vue -->
<template>
  <!-- Barra lateral izquierda -->
  <transition
    enter-active-class="transition-opacity ease-linear duration-300"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="transition-opacity ease-linear duration-300"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div
      v-if="isSidebarOpen"
      @click="closeSidebar"
      class="fixed inset-0 bg-gray-600 bg-opacity-75 z-20 lg:hidden"
    ></div>
  </transition>

  <aside
    :class="[
      isSidebarOpen ? 'translate-x-0' : '-translate-x-full',
      'fixed inset-y-0 left-0 z-30 w-64 transition duration-300 transform bg-white dark:bg-gray-800 overflow-y-auto lg:translate-x-0 lg:static lg:inset-0',
    ]"
  >
    <div class="flex flex-col h-full">
      <div class="flex-1 flex flex-col pt-5 pb-4">
        <nav class="mt-5 flex-1 px-2 space-y-1">
          <!-- Ítems del menú -->
          <a
            href="#"
            class="group flex items-center px-2 py-2 text-sm font-medium rounded-md text-gray-900 dark:text-white bg-gray-100 dark:bg-gray-900"
          >
            <HomeIcon class="mr-3 h-6 w-6 text-gray-500" />
            Inicio
          </a>
          <a
            href="#"
            class="group flex items-center px-2 py-2 text-sm font-medium rounded-md text-gray-900 dark:text-white hover:bg-gray-50 dark:hover:bg-gray-700"
          >
            <UsersIcon
              class="mr-3 h-6 w-6 text-gray-400 group-hover:text-gray-500"
            />
            Usuarios
          </a>
        </nav>
      </div>
      <div
        class="flex-shrink-0 flex border-t border-gray-200 dark:border-gray-700 p-4"
      >
        <button class="flex items-center" @click="handleLogout">
          <div>
            <ArrowLeftEndOnRectangleIcon class="h-6 w-6 text-gray-500" />
          </div>
          <div class="ml-3">
            <p
              class="text-xs font-medium text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-300"
            >
              Cerrar Sesión
            </p>
          </div>
        </button>
      </div>
    </div>
  </aside>
</template>

<script setup>
import {
  HomeIcon,
  UsersIcon,
  ArrowLeftEndOnRectangleIcon,
} from "@heroicons/vue/24/outline";
import { useSidebar } from "@/composables/useSidebar";
import { logout } from "@/services/api";
import { useRouter } from "vue-router";

const router = useRouter();

const { isSidebarOpen, closeSidebar } = useSidebar();
const handleLogout = async () => {
  const result = await logout();
  console.log(result);
  
  if (result.success) {
    console.log('Sesión cerrada');
    localStorage.removeItem('jwt')
    router.push('/inicio-sesion')
    closeSidebar();
  } else {
    console.error(result.error)
  }
};
</script>
