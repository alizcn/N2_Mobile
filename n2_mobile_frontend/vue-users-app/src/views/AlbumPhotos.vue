<template>
  <div class="container mx-auto p-4">
    <div class="flex items-center mb-4">
      <button @click="goBack" class="text-gray-700 hover:text-gray-900 mr-2 p-2 border border-gray-300 rounded-full">
        <i class="ti ti-arrow-left"></i>
      </button>
      <h1 class="text-2xl font-bold text-purple-700">Album Photos</h1>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <img
        v-for="photo in photos.slice(0, 5)"
        :key="photo.id"
        :src="photo.thumbnailUrl"
        :alt="photo.title"
        class="w-full h-auto rounded-lg"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'AlbumPhotos',
  data() {
    return {
      photos: []
    }
  },
  created() {
    const albumId = this.$route.params.id;
    fetch(`https://jsonplaceholder.typicode.com/albums/${albumId}/photos`)
      .then(response => response.json())
      .then(data => {
        this.photos = data;
      });
  },
  methods: {
    goBack() {
      this.$router.go(-1);
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