<template>
  <div class="w-64 h-screen  flex flex-col">
    <div class="p-4 flex items-center">
      <img v-if="user" :src="user.profilePicture" alt="Profile" class="rounded-full w-12 h-12 mr-2" />
      <span v-if="user" class="text-lg font-semibold text-purple-700">{{ user.name }}</span>
    </div>
    <router-link to="/" class="p-4 flex items-center hover:bg-gray-200" :class="{ 'bg-gray-200': isActive('/') }">
      <i class="ti ti-users mr-2 text-purple-700"></i>
      <span class="text-purple-700">Users</span>
    </router-link>
    <template v-if="user">
      <router-link :to="{ name: 'user-todos', params: { id: user.id }}" class="p-4 flex items-center hover:bg-gray-200" :class="{ 'bg-gray-200': isActive('/users/' + user.id + '/todos') }">
        <i class="ti ti-list-check mr-2 text-purple-700"></i>
        <span class="text-purple-700">Todos</span>
      </router-link>
      <router-link :to="{ name: 'user-posts', params: { id: user.id }}" class="p-4 flex items-center hover:bg-gray-200" :class="{ 'bg-gray-200': isActive('/users/' + user.id + '/posts') }">
        <i class="ti ti-file-text mr-2 text-purple-700"></i>
        <span class="text-purple-700">Posts</span>
      </router-link>
      <router-link :to="{ name: 'user-albums', params: { id: user.id }}" class="p-4 flex items-center hover:bg-gray-200" :class="{ 'bg-gray-200': isActive('/users/' + user.id + '/albums') }">
        <i class="ti ti-photo mr-2 text-purple-700"></i>
        <span class="text-purple-700">Albums</span>
      </router-link>
    </template>
  </div>
</template>

<script>
export default {
  name: 'Sidebar',
  props: {
    user: Object
  },
  methods: {
    isActive(route) {
      return this.$route.path === route;
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