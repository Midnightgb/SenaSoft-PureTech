<!--
Autor: Asistente IA Claude
Fecha de creación: 26 de septiembre de 2024
Descripción: Este componente Vue.js muestra un mapa interactivo de puntos de reciclaje en Colombia,
             con geolocalización del usuario y marcadores personalizados.
-->
<template>
  <div class="flex flex-col h-screen w-screen">
    <header class="p-4 bg-green-500 text-white">
      <h1 class="text-xl font-bold">Puntos de Reciclaje en Colombia</h1>
    </header>
    <main class="flex-1 relative">
      <div id="map" class="absolute inset-0"></div>
    </main>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import axios from 'axios';
import L from 'leaflet';

export default {
  name: 'RecyclingMapView',
  setup() {
    let map = null;
    const userLocation = ref(null);

    const fetchRecyclingPoints = async () => {
      try {
        const response = await axios.get('https://puretech-api.javm.tech/recycling_point/?skip=0&limit=100');
        return response.data;
      } catch (error) {
        console.error('Error fetching recycling points:', error);
        return [];
      }
    };

    const initMap = () => {
      map = L.map('map').setView([4.5709, -74.2973], 6); // Centrado en Colombia inicialmente
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(map);
    };

    const customIcon = L.icon({
      iconUrl: '/img/marker.svg',
      iconSize: [32, 32],
      iconAnchor: [16, 32],
      popupAnchor: [0, -32]
    });

    const addMarkers = (points) => {
      points.forEach(point => {
        L.marker([point.latitude, point.longitude], { icon: customIcon })
          .addTo(map)
          .bindPopup(`
            <b>${point.name}</b><br>
            Capacidad actual: ${point.current_capacity}<br>
            Capacidad máxima: ${point.max_capacity}
          `);
      });
    };

    const getUserLocation = () => {
      return new Promise((resolve, reject) => {
        if ("geolocation" in navigator) {
          navigator.geolocation.getCurrentPosition(
            position => resolve([position.coords.latitude, position.coords.longitude]),
            error => reject(error)
          );
        } else {
          reject(new Error("Geolocation is not supported by this browser."));
        }
      });
    };

    const findNearestPoint = (points, userLoc) => {
      return points.reduce((nearest, point) => {
        const distance = Math.sqrt(
          Math.pow(point.latitude - userLoc[0], 2) + 
          Math.pow(point.longitude - userLoc[1], 2)
        );
        return distance < nearest.distance ? { point, distance } : nearest;
      }, { point: null, distance: Infinity }).point;
    };

    const centerMapOnNearestPoint = (userLoc, nearestPoint) => {
      const centerLat = (userLoc[0] + nearestPoint.latitude) / 2;
      const centerLng = (userLoc[1] + nearestPoint.longitude) / 2;
      map.setView([centerLat, centerLng], 12); // Zoom level 12 for closer view
    };

    onMounted(async () => {
      initMap();
      const points = await fetchRecyclingPoints();
      addMarkers(points);

      try {
        userLocation.value = await getUserLocation();
        const nearestPoint = findNearestPoint(points, userLocation.value);
        if (nearestPoint) {
          centerMapOnNearestPoint(userLocation.value, nearestPoint);
          // Añadir un marcador para la ubicación del usuario
          L.marker(userLocation.value, {
            icon: L.divIcon({
              className: 'user-location-marker',
              html: '🔵', // Emoji como marcador
              iconSize: [25, 25],
              iconAnchor: [12, 25],
            })
          }).addTo(map).bindPopup("Tu ubicación");
        }
      } catch (error) {
        console.error("Error getting user location:", error);
        // Si no se puede obtener la ubicación del usuario, se mantiene la vista inicial
      }
    });

    onUnmounted(() => {
      if (map) {
        map.remove();
      }
    });

    return {
      userLocation
    };
  }
};
</script>

<style>
@import "leaflet/dist/leaflet.css";

.user-location-marker {
  font-size: 25px;
  text-align: center;
}
</style>