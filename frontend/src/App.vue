<!-- src/App.vue -->
<template>
  <div id="app">
    <nav v-if="showNavigation">
      <div class="min-h-screen bg-gray-100 dark:bg-gray-900 flex flex-col">
        <!-- Barra de navegación superior -->
        <Navbar />
        <div class="flex-1 flex overflow-hidden pt-16">
          <!-- Barra lateral izquierda -->
          <Sidebar />
          <!-- Área de contenido principal -->
          <RouterView/>
        </div>
      </div>
    </nav>
    <div v-else>
      <RouterView/>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import Sidebar from "@/components/layout/Sidebar.vue";
import Navbar from "@/components/layout/Navbar.vue";

const route = useRoute();
const showNavigation = computed(() => route.name !== "Login" && route.name !== "Landing");
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap");
#app {
  font-family: "Baloo 2", "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
@media (max-width: 1024px) {
  .sidebar-open {
    overflow: hidden;
  }
}
</style>
