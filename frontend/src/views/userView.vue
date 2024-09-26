<template>
  <div class="Users bg-green-50 min-h-screen w-screen p-8">
    <h1 class="text-3xl font-bold mb-6 text-green-800">User Management</h1>
    
    <!-- Search and filter bar -->
    <div class="bg-white rounded-lg shadow p-4 mb-6 flex items-center space-x-4">
      <div class="flex-grow">
        <input 
          v-model="searchQuery"
          type="text" 
          placeholder="Search users..." 
          class="w-full px-4 py-2 rounded-md border border-green-300 focus:outline-none focus:ring-2 focus:ring-green-500"
          @input="fetchUsers"
        >
      </div>
      <select 
        v-model="filterStatus"
        class="px-4 py-2 rounded-md border border-green-300 focus:outline-none focus:ring-2 focus:ring-green-500"
        @change="fetchUsers"
      >
        <option value="all">All Users</option>
        <option value="active">Active</option>
        <option value="inactive">Inactive</option>
      </select>
      <button @click="openCreateModal" class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition duration-300">
        Add User
      </button>
    </div>
    
    <!-- User list -->
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-green-200">
        <thead class="bg-green-100">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-green-800 uppercase tracking-wider">Name</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-green-800 uppercase tracking-wider">Email</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-green-800 uppercase tracking-wider">Type</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-green-800 uppercase tracking-wider">Eco Points</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-green-800 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-green-200">
          <tr v-for="user in users" :key="user.id">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-10 w-10">
                  <img class="h-10 w-10 rounded-full" :src="`https://ui-avatars.com/api/?name=${user.name}`" :alt="user.name" />
                </div>
                <div class="ml-4">
                  <div class="text-sm font-medium text-gray-900">{{ user.name }}</div>
                </div>
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ user.email }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                {{ user.type }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              {{ user.eco_points }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
              <button @click="openEditModal(user)" class="text-indigo-600 hover:text-indigo-900 mr-3">Edit</button>
              <button @click="deleteUser(user.id)" class="text-red-600 hover:text-red-900">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination component here (unchanged) -->

    <!-- Create/Edit User Modal -->
    <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
              {{ editingUser ? 'Edit User' : 'Create New User' }}
            </h3>
            <div class="mt-2">
              <form @submit.prevent="editingUser ? updateUser() : createUser()">
                <input v-model="userForm.name" type="text" placeholder="Name" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                <input v-model="userForm.email" type="email" placeholder="Email" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                <select v-model="userForm.type" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                  <option value="admin">Admin</option>
                  <option value="employee">Employee</option>
                  <option value="vulnerable">Vulnerable</option>
                  <option value="non_vulnerable">Non-Vulnerable</option>
                </select>
                <input v-if="!editingUser" v-model="userForm.password" type="password" placeholder="Password" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                <div class="mt-4">
                  <button type="submit" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    {{ editingUser ? 'Update' : 'Create' }}
                  </button>
                  <button type="button" @click="closeModal" class="ml-3 inline-flex justify-center py-2 px-4 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'

const users = ref([])
const searchQuery = ref('')
const filterStatus = ref('all')
const showModal = ref(false)
const editingUser = ref(null)
const userForm = reactive({
  name: '',
  email: '',
  type: 'employee',
  password: '',
  eco_points: 0
})

const fetchUsers = async () => {
  try {
    const response = await axios.get('/api/users', {
      params: {
        search: searchQuery.value,
        status: filterStatus.value
      }
    })
    users.value = response.data
  } catch (error) {
    console.error('Error fetching users:', error)
  }
}

const openCreateModal = () => {
  editingUser.value = null
  Object.assign(userForm, {
    name: '',
    email: '',
    type: 'employee',
    password: '',
    eco_points: 0
  })
  showModal.value = true
}

const openEditModal = (user) => {
  editingUser.value = user
  Object.assign(userForm, { ...user, password: '' })
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  editingUser.value = null
}

const createUser = async () => {
  try {
    const response = await axios.post('/api/users', userForm)
    users.value.push(response.data)
    closeModal()
  } catch (error) {
    console.error('Error creating user:', error)
  }
}

const updateUser = async () => {
  try {
    const response = await axios.put(`/api/users/${editingUser.value.id}`, userForm)
    const index = users.value.findIndex(u => u.id === editingUser.value.id)
    if (index !== -1) {
      users.value[index] = response.data
    }
    closeModal()
  } catch (error) {
    console.error('Error updating user:', error)
  }
}

const deleteUser = async (userId) => {
  if (confirm('Are you sure you want to delete this user?')) {
    try {
      await axios.delete(`/api/users/${userId}`)
      users.value = users.value.filter(u => u.id !== userId)
    } catch (error) {
      console.error('Error deleting user:', error)
    }
  }
}

onMounted(fetchUsers)
</script>