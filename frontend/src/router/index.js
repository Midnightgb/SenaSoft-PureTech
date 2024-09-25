// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: "/inicio-sesion",
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
      requiresAuth: false,
    },
  },

  {
    path: "/users",
    name: "Users",
    component: () => import("@/views/userView.vue"),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: "/EducationCenter",
    name: "EducationCenter",
    component: () => import("@/views/EducationCenterView.vue"),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: "/EducationCenter",
    name: "EducationCenter",
    component: () => import("@/views/EducationCenterView.vue"),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: "/RewardsCenter",
    name: "RewardsCenter",
    component: () => import("@/views/RewardsCenterView.vue"),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: "/RecyclingMap",
    name: "RecyclingMap",
    component: () => import("@/views/RecyclingMapView.vue"),
    meta: {
      requiresAuth: false,
    },
  },
  
  {
    path: "/YourImpact",
    name: "YourImpact",
    component: () => import("@/views/YourImpactView.vue"),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: "/userView",
    name: "userView",
    component: () => import("@/views/userView.vue"),
    meta: {
      requiresAuth: false,
    },
  },


  {
    path: "/test",
    name: "Test",
    component: () => import("@/views/TestView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    redirect: (to) => ({ name: "Login", query: { redirect: to.fullPath } }),
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
      // Si no está autenticado, redirigir al login
      next({ name: "Login" });
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
