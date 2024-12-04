<template>
  <div class="flex">
    <Sidebar :user="user" />
    <div class="flex-1 container mx-auto p-4">
      <router-view />
    </div>
  </div>
</template>

<script>
import Sidebar from './Sidebar.vue'

export default {
  name: 'UserProfileLayout',
  components: { Sidebar },
  data() {
    return {
      user: null
    }
  },
  created() {
    const userId = this.$route.params.id;
    fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
      .then(response => response.json())
      .then(data => {
        this.user = {
          ...data,
          profilePicture: 'https://via.placeholder.com/40' // Placeholder for profile picture
        };
      });
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}
</style>