<template>
  <div class="min-h-screen bg-gray-100 dark:bg-gray-900 flex flex-col">
    <!-- Barra de navegación superior -->
    <Navbar />

    <div class="flex-1 flex overflow-hidden pt-16">
      <!-- Barra lateral izquierda -->
      <Sidebar />
      <!-- Área de contenido principal -->
      <MainContent/>
    </div>
  </div>
</template>

<script setup>
import Sidebar from "@/components/layout/Sidebar.vue";
import Navbar from "@/components/layout/Navbar.vue";
import MainContent from "@/components/layout/MainContent.vue";
X
</script>

<style scoped>
@media (max-width: 1024px) {
  .sidebar-open {
    overflow: hidden;
  }
}
</style>
