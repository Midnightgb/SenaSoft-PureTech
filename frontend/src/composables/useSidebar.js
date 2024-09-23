// src/composables/useSidebar.js
import { ref } from "vue";

const isSidebarOpen = ref(false);

export function useSidebar() {
  const toggleSidebar = () => {
    isSidebarOpen.value = !isSidebarOpen.value;
  };

  const closeSidebar = () => {
    isSidebarOpen.value = false;
  };

  return {
    isSidebarOpen,
    toggleSidebar,
    closeSidebar,
  };
}
