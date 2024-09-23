<script setup>
import { ref, watch, onMounted } from "vue";
import { MoonIcon, SunIcon } from "@heroicons/vue/24/outline";

// Función para obtener la preferencia de color del sistema
const getColorScheme = () =>
  window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";

// Función para usar localStorage
const useLocalStorage = (key, defaultValue) => {
  const storedValue = ref(
    localStorage.getItem(key)
      ? JSON.parse(localStorage.getItem(key))
      : defaultValue
  );

  watch(storedValue, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue));
  });

  return storedValue;
};

// Usar localStorage para persistir la preferencia del usuario
const storedTheme = useLocalStorage("theme", getColorScheme());

// Estado reactivo para el modo oscuro
const isDarkMode = ref(storedTheme.value === "dark");

// Función para establecer el modo oscuro
const setDarkMode = (isDark) => {
  isDarkMode.value = isDark;
  storedTheme.value = isDark ? "dark" : "light";
};

// Función para alternar el modo oscuro
const toggleDarkMode = () => setDarkMode(!isDarkMode.value);

// Efecto para aplicar la clase 'dark' al elemento html
watch(
  isDarkMode,
  (newValue) => {
    if (newValue) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  },
  { immediate: true }
);

// Escuchar cambios en la preferencia del sistema
onMounted(() => {
  const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  mediaQuery.addEventListener("change", (e) => {
    if (storedTheme.value === "system") {
      setDarkMode(e.matches);
    }
  });
});

// Aplicar el modo inicial
setDarkMode(isDarkMode.value);
</script>

<template>
  <button
    @click="toggleDarkMode"
    class="ml-3 p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
  >
    <span class="sr-only">Alternar modo oscuro</span>
    <MoonIcon v-if="!isDarkMode" class="h-6 w-6" />
    <SunIcon v-else class="h-6 w-6" />
  </button>
</template>
