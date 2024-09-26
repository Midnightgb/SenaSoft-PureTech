<script setup>
import { ref } from 'vue';
import EcoButton from '@/components/common/EcoButton.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const features = ref([
  { title: 'Gane increíbles recompensas', description: 'Recicle materiales y gane eco-puntos canjeables.', icon: '🏆' },
  { title: 'Ayúdanos a mantener limpio nuestro hogar', description: 'Cada acción cuenta para un planeta más limpio.', icon: '🌍' },
  { title: 'Conéctese con la comunidad', description: 'Únase a eventos locales de reciclaje y limpieza.', icon: '🤝' },
  { title: 'Educación ambiental', description: 'Aprenda sobre sostenibilidad y prácticas eco-amigables.', icon: '📚' },
]);

const handleNavigation = (path) => {
  router.push(path);
  closeSidebar();
};

</script>

<template>
  <div class="min-h-screen bg-gradient-to-b from-green-50 to-green-100">
    <header class="bg-white shadow-md">
      <div class="container mx-auto px-4 py-6 flex justify-between items-center">
        <div class="text-3xl font-bold text-green-600 flex items-center">
          <img src="https://placehold.co/50x50" alt="EcoConnect Logo" class="mr-2 rounded-full" />
          EcoConnect
        </div>
        <EcoButton variant="outline" class="bg-green-500 text-black hover:bg-green-600 hover:text-white" @click="handleNavigation('/inicio-sesion')">Login</EcoButton>
      </div>
    </header>

    <main class="container mx-auto px-4 py-12">
      <section class="text-center mb-16">
        <h1 class="text-5xl font-bold mb-6 text-green-800">Transforma el reciclaje en acción con EcoConnect</h1>
        <p class="text-xl mb-8 text-green-700">Unimos a recicladores, centros de acopio y empresas para un futuro más verde y sostenible.</p>
        <EcoButton size="lg" class="bg-green-500 hover:bg-green-600 text-white text-lg px-8 py-3">Únete ahora</EcoButton>
      </section>

      <div class="grid md:grid-cols-2 gap-12 mb-16">
        <div class="relative">
          <img src="https://placehold.co/600x400" alt="Reciclaje en acción" class="rounded-lg shadow-xl" />
          <div class="absolute inset-0 bg-green-500 opacity-20 rounded-lg"></div>
        </div>
        <div class="flex flex-col justify-center">
          <h2 class="text-3xl font-semibold mb-4 text-green-700">Haz la diferencia hoy</h2>
          <p class="text-lg mb-6 text-green-600">Cada botella, lata o papel que reciclas contribuye a un futuro más limpio y sostenible. Con EcoConnect, tus esfuerzos se multiplican.</p>
          <EcoButton variant="outline" class="self-start">Descubre cómo</EcoButton>
        </div>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
        <div v-for="feature in features" :key="feature.title" class="bg-white p-6 rounded-lg shadow-lg transition-transform duration-300 hover:scale-105">
          <div class="text-4xl mb-4">{{ feature.icon }}</div>
          <h3 class="text-xl font-semibold mb-2 text-green-700">{{ feature.title }}</h3>
          <p class="text-green-600">{{ feature.description }}</p>
        </div>
      </div>

      <section class="bg-green-600 text-white p-12 rounded-xl shadow-2xl mb-16 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10">
          <img src="https://placehold.co/1200x400" alt="Naturaleza" class="w-full h-full object-cover" />
        </div>
        <div class="relative z-10">
          <h2 class="text-4xl font-bold mb-6">Únete a la revolución verde</h2>
          <p class="text-xl mb-8">Sé parte del cambio. Juntos podemos crear un impacto positivo en nuestro planeta.</p>
          <EcoButton size="lg" class="bg-green-400 text-green-800 hover:bg-green-700 hover:text-white">Comienza ahora</EcoButton>
        </div>
      </section>

      <div class="grid md:grid-cols-3 gap-8 mb-16">
        <div class="bg-white p-6 rounded-lg shadow-md text-center">
          <img src="https://placehold.co/100x100" alt="Icono de árboles" class="mx-auto mb-4" />
          <h3 class="text-2xl font-semibold mb-2 text-green-700">1000+ árboles salvados</h3>
          <p class="text-green-600">Gracias a nuestros esfuerzos colectivos de reciclaje</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md text-center">
          <img src="https://placehold.co/100x100" alt="Icono de usuarios" class="mx-auto mb-4" />
          <h3 class="text-2xl font-semibold mb-2 text-green-700">10,000+ usuarios activos</h3>
          <p class="text-green-600">Una comunidad creciente comprometida con el cambio</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md text-center">
          <img src="https://placehold.co/100x100" alt="Icono de reciclaje" class="mx-auto mb-4" />
          <h3 class="text-2xl font-semibold mb-2 text-green-700">500 toneladas recicladas</h3>
          <p class="text-green-600">Materiales desviados de vertederos y reutilizados</p>
        </div>
      </div>
    </main>

    <footer class="bg-green-800 text-white py-12">
      <div class="container mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
          <div>
            <h4 class="text-xl font-semibold mb-4">Sobre EcoConnect</h4>
            <p>Transformando el reciclaje en una experiencia gratificante y sostenible para todos.</p>
          </div>
          <div>
            <h4 class="text-xl font-semibold mb-4">Enlaces rápidos</h4>
            <ul>
              <li><a href="#" class="hover:underline">Cómo funciona</a></li>
              <li><a href="#" class="hover:underline">Únete como reciclador</a></li>
              <li><a href="#" class="hover:underline">Para empresas</a></li>
              <li><a href="#" class="hover:underline">Blog</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-xl font-semibold mb-4">Contacto</h4>
            <p>info@ecoconnect.com</p>
            <p>+1 (555) 123-4567</p>
            <div class="flex mt-4 space-x-4">
              <a href="#" class="text-2xl">📘</a>
              <a href="#" class="text-2xl">🐦</a>
              <a href="#" class="text-2xl">📸</a>
              <a href="#" class="text-2xl">🔗</a>
            </div>
          </div>
        </div>
        <div class="mt-8 pt-8 border-t border-green-700 text-center">
          <p>&copy; 2024 EcoConnect. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>