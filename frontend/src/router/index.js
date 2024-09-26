// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: "/landing",
  },
  {
    path: "/inicio-sesion",
    name: "Login",
    component: () => import("@/views/LoginView.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/inicio",
    name: "Home",
    component: () => import("@/views/HomeView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/categorias",
    name: "Categories",
    component: () => import("@/views/CategoriesView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/users",
    name: "Users",
    component: () => import("@/views/userView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/EducationCenter",
    name: "EducationCenter",
    component: () => import("@/views/EducationCenterView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/RewardsCenter",
    name: "RewardsCenter",
    component: () => import("@/views/RewardsCenterView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/RecyclingMap",
    name: "RecyclingMap",
    component: () => import("@/views/RecyclingMapView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/SaveRecycling",
    name: "SaveRecycling",
    component: () => import("@/views/SaveRecycling.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/Profile",
    name: "Profile",
    component: () => import("@/views/ProfileView.vue"),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/landing",
    name: "Landing",
    component: () => import("@/views/LandingView.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    redirect: (to) => ({ name: "Landing", query: { redirect: to.fullPath } }),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("jwt");

  if (to.name === "Login" && isAuthenticated) {
    // Si el usuario está autenticado y trata de ir a la página de login,
    // redirigirlo al home
    next({ name: "Home" });
  } else if (to.matched.some((record) => record.meta.requiresAuth)) {
    // Verificar si la ruta requiere autenticación
    if (!isAuthenticated) {
      // Si no está autenticado, redirigir al landing
      next({ name: "Landing" });
    } else {
      // Si está autenticado, permitir la navegación
      next();
    }
  } else {
    // Para rutas que no requieren autenticación, permitir la navegación
    next();
  }
});

export default router;