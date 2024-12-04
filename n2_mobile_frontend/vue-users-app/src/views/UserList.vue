<template>
  <div class="flex">
    <Sidebar />
    <div class="flex-1 container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4 text-purple-700">All Users</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="user in users"
          :key="user.id"
          class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 cursor-pointer border border-gray-200"
          @click="goToUserProfile(user.id)"
        >
          <div class="flex items-center mb-4">
            <img
              :src="'https://via.placeholder.com/150?text=' + user.name.charAt(0)"
              alt="Profile"
              class="w-16 h-16 rounded-full mr-4"
            />
            <div>
              <h2 class="text-lg font-semibold">{{ user.name }}</h2>
              <p class="text-gray-600 text-sm">{{ user.email }}</p>
              <p class="text-gray-600 text-sm">{{ user.phone }}</p>
            </div>
          </div>
          <div class="flex items-center mb-2">
            <i class="ti ti-map-pin mr-2 text-purple-700"></i>
            <span class="font-semibold text-sm">Location</span>
          </div>
          <p class="text-gray-600 text-sm mb-4">{{ user.address.city }}, {{ user.address.street }}</p>
          <div class="flex items-center mb-2">
            <i class="ti ti-building mr-2 text-purple-700"></i>
            <span class="font-semibold text-sm">Company</span>
          </div>
          <p class="text-gray-600 text-sm mb-4">{{ user.company.name }}</p>
          <div class="flex items-center mb-2">
            <i class="ti ti-world mr-2 text-purple-700"></i>
            <span class="font-semibold text-sm">Website</span>
          </div>
          <p class="text-gray-600 text-sm">{{ user.website }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from './Sidebar.vue'

export default {
  name: 'UserList',
  components: { Sidebar },
  data() {
    return {
      users: []
    }
  },
  created() {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => response.json())
      .then(data => {
        this.users = data;
      });
  },
  methods: {
    goToUserProfile(userId) {
      this.$router.push({ name: 'user-detail', params: { id: userId } });
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}
</style>