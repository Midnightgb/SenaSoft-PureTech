<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-50 to-blue-100 flex flex-col items-center justify-center p-4">
    <div class="w-full max-w-md space-y-8 bg-white p-6 rounded-xl shadow-lg">
      <div class="flex flex-col items-center">
        <LayoutIcon class="h-12 w-12 text-purple-600" />
        <h1 class="mt-2 text-3xl font-bold text-gray-900">Inicio de sesión</h1>
      </div>
      <form @submit.prevent="handleLogin" class="mt-8 space-y-6">
        <div class="space-y-4">
          <div class="relative">
            <UserIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
            <input
              v-model="username"
              type="text"
              placeholder="Nombre de usuario"
              class="pl-10 w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-600"
              required
            />
          </div>
          <div class="relative">
            <LockIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Contraseña"
              class="pl-10 pr-10 w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-600"
              required
            />
            <button
              type="button"
              class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
              @click="togglePasswordVisibility"
              :aria-label="showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'"
            >
              <EyeIcon v-if="!showPassword" class="h-5 w-5" />
              <EyeOffIcon v-else class="h-5 w-5" />
            </button>
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-opacity-50 flex items-center justify-center"
          >
            <LogInIcon class="mr-2 h-4 w-4" /> Iniciar sesión
          </button>
        </div>
      </form>
      <div v-if="error" class="text-red-500 text-center mt-2">{{ error }}</div>
      <div class="flex items-center justify-between hidden">
        <a href="/forgot-password" class="text-sm text-purple-600 hover:underline">
          ¿Olvidaste tu contraseña?
        </a>
        <a href="/signup" class="text-sm text-purple-600 hover:underline flex items-center">
          <UserPlusIcon class="mr-1 h-4 w-4" /> Registrarse
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
const username = ref('')
const password = ref('')
const showPassword = ref(false)
const error = ref('')

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

const handleLogin = async () => {
  error.value = ''
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
