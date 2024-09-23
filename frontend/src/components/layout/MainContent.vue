<template>
  <main class="flex-1 relative overflow-y-auto focus:outline-none">
    <div class="py-6">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
        <h1 class="text-2xl font-semibold text-gray-900 dark:text-white">
          Dashboard
        </h1>
      </div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
        <!-- Cuadrícula de tarjetas de estadísticas -->
        <div class="mt-8 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
          <!-- Tarjeta de estadística -->
          <div
            class="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg"
          >
            <div class="p-5">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <UsersIcon class="h-6 w-6 text-gray-400" />
                </div>
                <div class="ml-5 w-0 flex-1">
                  <dl>
                    <dt class="text-sm font-medium text-gray-500 truncate">
                      Total de usuarios
                    </dt>
                    <dd>
                      <div
                        class="text-lg font-medium text-gray-900 dark:text-white"
                      >
                        71,897
                      </div>
                    </dd>
                  </dl>
                </div>
              </div>
            </div>
          </div>
          <!-- Más tarjetas de estadísticas aquí -->
        </div>

        <!-- Gráfico o tabla grande -->
        <div class="mt-8">
          <div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
            <h2
              class="text-lg leading-6 font-medium text-gray-900 dark:text-white mb-4"
            >
              Rendimiento mensual
            </h2>
            <!-- Aquí iría el componente del gráfico -->
            <div class="h-64 bg-gray-200 dark:bg-gray-700 rounded-lg"></div>
          </div>
        </div>

        <!-- Dos filas de tarjetas más grandes -->
        <div class="mt-8 grid grid-cols-1 gap-5 sm:grid-cols-2">
          <!-- Tarjeta grande -->
          <div
            class="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg"
          >
            <div class="p-5">
              <h3
                class="text-lg leading-6 font-medium text-gray-900 dark:text-white"
              >
                Actividad reciente
              </h3>
              <!-- Contenido de la tarjeta -->
            </div>
          </div>
          <!-- Más tarjetas grandes aquí -->
          <div
            class="bg-white dark:bg-gray-800 overflow-hidden shadow rounded-lg"
          >
            <div class="p-5">
              <h3
                class="text-lg leading-6 font-medium text-gray-900 dark:text-white"
              >
                Actividad reciente
              </h3>
              <!-- Contenido de la tarjeta -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<script setup>
import { UsersIcon } from "@heroicons/vue/24/outline";
</script>
