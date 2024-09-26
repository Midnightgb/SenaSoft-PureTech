<template>
  <div class="Users bg-green-50 dark:bg-gray-900 min-h-screen w-screen p-8">
    <h1 class="text-3xl font-bold mb-6 text-green-800 dark:text-green-400">
      User Management
    </h1>

    <!-- Search and filter bar -->
    <div
      class="bg-white dark:bg-gray-800 rounded-lg shadow p-4 mb-6 flex items-center space-x-4"
    >
      <div class="flex-grow">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search users..."
          class="w-full px-4 py-2 rounded-md border border-green-300 dark:border-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 dark:bg-gray-700 dark:text-white"
          @input="handleSearch"
        />
      </div>
      <select
        v-model="filterStatus"
        class="px-4 py-2 rounded-md border border-green-300 dark:border-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 dark:bg-gray-700 dark:text-white"
        @change="handleFilterChange"
      >
        <option value="all">All Users</option>
        <option value="active">Active</option>
        <option value="inactive">Inactive</option>
      </select>
      <button
        @click="openCreateModal"
        class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition duration-300 dark:bg-green-700 dark:hover:bg-green-600"
      >
        Add User
      </button>
    </div>

    <!-- User list -->
    <div class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-green-200 dark:divide-green-700">
        <thead class="bg-green-100 dark:bg-green-900">
          <tr>
            <th
              class="px-6 py-3 text-left text-xs font-medium text-green-800 dark:text-green-300 uppercase tracking-wider"
            >
              Name
            </th>
            <th
              class="px-6 py-3 text-left text-xs font-medium text-green-800 dark:text-green-300 uppercase tracking-wider"
            >
              Email
            </th>
            <th
              class="px-6 py-3 text-left text-xs font-medium text-green-800 dark:text-green-300 uppercase tracking-wider"
            >
              Type
            </th>
            <th
              class="px-6 py-3 text-left text-xs font-medium text-green-800 dark:text-green-300 uppercase tracking-wider"
            >
              Eco Points
            </th>
            <th
              class="px-6 py-3 text-left text-xs font-medium text-green-800 dark:text-green-300 uppercase tracking-wider"
            >
              Actions
            </th>
          </tr>
        </thead>
        <tbody
          class="bg-white dark:bg-gray-800 divide-y divide-green-200 dark:divide-green-700"
        >
          <tr v-for="user in users" :key="user.id">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex items-center">
                <div class="flex-shrink-0 h-10 w-10">
                  <img
                    class="h-10 w-10 rounded-full"
                    :src="`https://ui-avatars.com/api/?name=${user.name}&background=random`"
                    :alt="user.name"
                  />
                </div>
                <div class="ml-4">
                  <div
                    class="text-sm font-medium text-gray-900 dark:text-gray-100"
                  >
                    {{ user.name }}
                  </div>
                </div>
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900 dark:text-gray-100">
                {{ user.email }}
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300"
              >
                {{ getUserTypeLabel(user.type) }}
              </span>
            </td>
            <td
              class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400"
            >
              {{ user.eco_points }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
              <button
                @click="openEditModal(user)"
                class="text-indigo-600 hover:text-indigo-900 dark:text-indigo-400 dark:hover:text-indigo-300 mr-3"
              >
                Edit
              </button>
              <button
                @click="deleteUser(user.id)"
                class="text-red-600 hover:text-red-900 dark:text-red-400 dark:hover:text-red-300"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div
      class="bg-white dark:bg-gray-800 px-4 py-3 flex items-center justify-between border-t border-gray-200 dark:border-gray-700 sm:px-6"
    >
      <div class="flex-1 flex justify-between sm:hidden">
        <button
          @click="previousPage"
          :disabled="currentPage === 1"
          class="relative inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700"
        >
          Previous
        </button>
        <button
          @click="nextPage"
          :disabled="!hasMorePages"
          class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-600 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700"
        >
          Next
        </button>
      </div>
      <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
        <div>
          <p class="text-sm text-gray-700 dark:text-gray-300">
            Showing
            <span class="font-medium">{{
              (currentPage - 1) * itemsPerPage + 1
            }}</span>
            to  
            <span class="font-medium">{{
              Math.min(currentPage * itemsPerPage, totalItems)
            }}</span>
            of <span class="font-medium">{{ totalItems }}</span> results
          </p>
        </div>
        <div>
          <nav
            class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px"
            aria-label="Pagination"
          >
            <button
              @click="previousPage"
              :disabled="currentPage === 1"
              class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700"
            >
              Previous
            </button>
            <button
              @click="nextPage"
              :disabled="!hasMorePages"
              class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700"
            >
              Next
            </button>
          </nav>
        </div>
      </div>
    </div>

    <!-- Create/Edit User Modal -->
    <div
      v-if="showModal"
      class="fixed z-10 inset-0 overflow-y-auto"
      aria-labelledby="modal-title"
      role="dialog"
      aria-modal="true"
    >
      <div
        class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 dark:bg-gray-900 dark:bg-opacity-75 transition-opacity"
          aria-hidden="true"
        ></div>
        <span
          class="hidden sm:inline-block sm:align-middle sm:h-screen"
          aria-hidden="true"
          >&#8203;</span
        >
        <div
          class="inline-block align-bottom bg-white dark:bg-gray-800 rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
        >
          <div class="bg-white dark:bg-gray-800 px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <h3
              class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100"
              id="modal-title"
            >
              {{ editingUser ? "Edit User" : "Create New User" }}
            </h3>
            <div class="mt-2">
              <form @submit.prevent="editingUser ? updateUser() : createUser()">
                <input
                  v-model="userForm.name"
                  type="text"
                  placeholder="Name"
                  class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 dark:bg-gray-700 dark:text-white"
                />
                <input
                  v-model="userForm.email"
                  type="email"
                  placeholder="Email"
                  class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 dark:bg-gray-700 dark:text-white"
                />
                <select
                  v-model="userForm.type"
                  class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 dark:bg-gray-700 dark:text-white"
                >
<!--                   <option value="1">Admin</option>
                  <option value="2">Employee</option> -->
                  <option value="3" selected>Vulnerable</option>
                  <option value="4">Non-Vulnerable</option>
                </select>
                <input
                  v-if="!editingUser"
                  v-model="userForm.password"
                  type="password"
                  placeholder="Password"
                  class="mt-1 block w-full rounded-md border-gray-300 dark:border-gray-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 dark:bg-gray-700 dark:text-white"
                />
                <div class="mt-4">
                  <button
                    type="submit"
                    class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 dark:bg-indigo-700 dark:hover:bg-indigo-600"
                  >
                    {{ editingUser ? "Update" : "Create" }}
                  </button>
                  <button
                    type="button"
                    @click="closeModal"
                    class="ml-3 inline-flex justify-center py-2 px-4 border border-gray-300 dark:border-gray-600 shadow-sm text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
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
import { ref, reactive, onMounted, computed } from "vue";
import { apiClient, fetchUsers as apiFetchUsers } from "@/services/api";
import { API_ENDPOINTS } from "@/constants/api";

const users = ref([]);
const searchQuery = ref("");
const filterStatus = ref("all");
const showModal = ref(false);
const editingUser = ref(null);
const userForm = reactive({
  name: "",
  email: "",
  type: "employee",
  password: "",
  eco_points: 0,
});

const getUserTypeLabel = (type) => {
  const typeMap = {
    1: "Admin",
    2: "Employee",
    3: "Vulnerable",
    4: "Non Vulnerable",
  };
  return typeMap[type] || "Unknown";
};

// Pagination
const currentPage = ref(1);
const itemsPerPage = ref(10);
const totalItems = ref(0);

const hasMorePages = computed(() => {
  return currentPage.value * itemsPerPage.value < totalItems.value;
});

const fetchUsers = async () => {
  try {
    const result = await apiFetchUsers();
    if (result.success) {
      users.value = result.data;
      totalItems.value = result.data.length;
    } else {
      console.error("Error fetching users:", result.error);
    }
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};

const handleSearch = () => {
  fetchUsers();
};

const handleFilterChange = () => {
  fetchUsers();
};

const nextPage = () => {
  if (hasMorePages.value) {
    currentPage.value++;
    fetchUsers();
  }
};

const previousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    fetchUsers();
  }
};

const openCreateModal = () => {
  editingUser.value = null;
  Object.assign(userForm, {
    name: "",
    email: "",
    type: "employee",
    password: "",
    eco_points: 0,
  });
  showModal.value = true;
};

const openEditModal = (user) => {
  editingUser.value = user;
  Object.assign(userForm, { ...user, password: "" });
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
  editingUser.value = null;
};

const createUser = async () => {
  try {
    console.log('API_ENDPOINTS.REGISTER:', API_ENDPOINTS.REGISTER);
    console.log('userForm:', userForm);
    
    
    const response = await apiClient.post(API_ENDPOINTS.REGISTER, userForm);
    console.log('Response:', response);
    
    users.value.push(response.data);
    closeModal();
    await fetchUsers();
  } catch (error) {
    console.error('Error creating user:', error);
    console.error('Error details:', error.response?.data || 'No response data');
    // Mostrar el error al usuario
    alert(`Error creating user: ${error.message}`);
  }
};

const updateUser = async () => {
  try {
    const response = await apiClient.put(
      `${API_ENDPOINTS.USERS}/${editingUser.value.id}`,
      userForm
    );
    const index = users.value.findIndex((u) => u.id === editingUser.value.id);
    if (index !== -1) {
      users.value[index] = response.data;
    }
    closeModal();
  } catch (error) {
    console.error("Error updating user:", error);
  }
};

const deleteUser = async (userId) => {
  if (confirm("Are you sure you want to delete this user?")) {
    try {
      await apiClient.delete(`${API_ENDPOINTS.USERS}/${userId}`);
      users.value = users.value.filter((u) => u.id !== userId);
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  }
};

onMounted(fetchUsers);
</script>
