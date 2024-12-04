<template>
    <div class="container mx-auto p-4">
      <div class="flex items-center mb-4">
        <button @click="goBack" class="text-gray-700 hover:text-gray-900 mr-2 p-2 border border-gray-300 rounded-full">
          <i class="ti ti-arrow-left"></i>
        </button>
        <h1 class="text-2xl font-bold text-purple-700">User Posts</h1>
      </div>
      <ul class="divide-y divide-gray-200">
        <li
          v-for="post in posts"
          :key="post.id"
          class="bg-white p-6 rounded-lg shadow-md cursor-pointer"
          @click="openPostModal(post)"
        >
          <h2 class="text-lg font-semibold mb-2">{{ post.title }}</h2>
          <p class="text-sm text-gray-700 mb-4">{{ post.body }}</p>
          <div class="text-right">
            <span class="text-purple-700 font-semibold">See More</span>
            <i class="ti ti-arrow-right-circle ml-2 text-purple-700"></i>
          </div>
        </li>
      </ul>
      <div v-if="selectedPost" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-5xl h-auto max-h-[80vh] relative overflow-y-auto">
          <button @click="closePostModal" class="absolute top-2 right-2 text-gray-500 hover:text-gray-700">
            <i class="ti ti-x"></i>
          </button>
          <div class="flex">
            <div class="w-1/2 pr-4">
              <h2 class="text-lg font-semibold mb-2">{{ selectedPost.title }}</h2>
              <p class="text-sm">{{ selectedPost.body }}</p>
            </div>
            <div class="w-px bg-gray-300 mx-4"></div>
            <div class="w-1/2 pl-4">
              <h3 class="text-md font-semibold mb-2">Comments</h3>
              <ul class="space-y-2">
                <li v-for="comment in comments" :key="comment.id" class="p-2 rounded-lg flex items-start">
                  <img
                    :src="'https://via.placeholder.com/40?text=' + comment.name.charAt(0)"
                    alt="Profile"
                    class="w-10 h-10 rounded-full mr-4"
                  />
                  <div>
                    <p class="font-semibold text-sm">{{ comment.name }}</p>
                    <p class="text-sm">{{ comment.body }}</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserPosts',
    data() {
      return {
        posts: [],
        selectedPost: null,
        comments: []
      }
    },
    created() {
      const userId = this.$route.params.id;
      fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`)
        .then(response => response.json())
        .then(data => {
          this.posts = data;
        });
    },
    methods: {
      openPostModal(post) {
        this.selectedPost = post;
        fetch(`https://jsonplaceholder.typicode.com/posts/${post.id}/comments`)
          .then(response => response.json())
          .then(data => {
            this.comments = data;
          });
      },
      closePostModal() {
        this.selectedPost = null;
        this.comments = [];
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