<template>
    <div class="container mx-auto p-4">
      <div class="flex items-center mb-4">
        <button @click="goBack" class="text-gray-500 hover:text-gray-700 mr-2 p-2 border border-gray-300 rounded-full">
            <i class="ti ti-arrow-left"></i>
        </button>
        <h1 class="text-2xl font-bold text-purple-700">User Albums</h1>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="album in albums"
          :key="album.id"
          class="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 cursor-pointer"
          @click="goToAlbumPhotos(album.id)"
        >
          <img
            :src="album.coverPhoto"
            alt="Album Cover"
            class="w-full h-48 object-cover rounded-lg mb-4"
          />
          <h2 class="text-xl font-semibold">{{ album.title }}</h2>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserAlbums',
    data() {
      return {
        albums: []
      }
    },
    created() {
      const userId = this.$route.params.id;
      fetch(`https://jsonplaceholder.typicode.com/albums?userId=${userId}`)
        .then(response => response.json())
        .then(data => {
          this.albums = data;
          this.albums.forEach(album => {
            fetch(`https://jsonplaceholder.typicode.com/albums/${album.id}/photos`)
              .then(response => response.json())
              .then(photos => {
                album.coverPhoto = photos[0]?.thumbnailUrl || 'https://via.placeholder.com/150';
              });
          });
        });
    },
    methods: {
      goToAlbumPhotos(albumId) {
        this.$router.push({ name: 'album-photos', params: { id: albumId } });
      },
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