<template>
  <div class="flex flex-col items-center justify-center min-h-screen p-4 bg-gradient-to-br from-green-50 to-blue-100">
    <div class="w-full max-w-md p-6 space-y-8 bg-white shadow-lg rounded-xl">
      <div class="flex flex-col items-center">
        <LayoutIcon class="w-12 h-12 text-green-600" />
        <h1 class="mt-2 text-3xl font-bold text-gray-900">Inicio de sesión</h1>
      </div>
      <form @submit.prevent="handleLogin" class="mt-8 space-y-6">
        <div class="space-y-4">
          <div class="relative">
            <UserIcon class="absolute text-gray-400 transform -translate-y-1/2 left-3 top-1/2" />
            <input
              v-model="username"
              placeholder="Correo Electrónico"
              type="text"
              class="w-full px-3 py-2 pl-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-600"
              required
            />
          </div>
          <div class="relative">
            <LockIcon class="absolute text-gray-400 transform -translate-y-1/2 left-3 top-1/2" />
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Contraseña"
              class="w-full px-3 py-2 pl-10 pr-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-600"
              required
            />
            <button
              type="button"
              class="absolute text-gray-400 transform -translate-y-1/2 right-3 top-1/2 hover:text-gray-600"
              @click="togglePasswordVisibility"
              :aria-label="showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'"
            >
              <EyeIcon v-if="!showPassword" class="w-5 h-5" />
              <EyeOffIcon v-else class="w-5 h-5" />
            </button>
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="flex items-center justify-center w-full px-4 py-2 font-bold text-white bg-green-600 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-600 focus:ring-opacity-50"
          >
            <LogInIcon class="w-4 h-4 mr-2" /> Iniciar sesión
          </button>
        </div>
      </form>
      <div v-if="error" class="mt-2 text-center text-red-500">{{ error }}</div>
      <div class="items-center justify-between hidden">
        <a href="/forgot-password" class="text-sm text-green-600 hover:underline">

          ¿Olvidaste tu contraseña?
        </a>
        <a href="/signup" class="flex items-center text-sm text-green-600 hover:underline">
          <UserPlusIcon class="w-4 h-4 mr-1" /> Registrarse
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '@/services/api'
import { LayoutIcon, UserIcon, LockIcon, EyeIcon, EyeOffIcon, LogInIcon, UserPlusIcon } from 'lucide-vue-next'

const router = useRouter()
const username = ref('user@example.com')
const password = ref('string')
const showPassword = ref(false)
const error = ref('')

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

const handleLogin = async () => {
  error.value = ''
  console.log('Login:', username.value, password.value);
  
  const credentials = {
    username: username.value,
    password: password.value,
  }
  const result = await login(credentials)
  if (result.success) {
    localStorage.setItem('jwt', result.data.access_token)
    router.push('/inicio')
  } else {
    error.value = result.error || 'Nombre de usuario o contraseña inválidos'
  }
}
</script>
