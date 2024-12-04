<template>
  <div class="container mx-auto p-4">
    <div class="flex items-center mb-4">
      <button @click="goBack" class="text-gray-700 hover:text-gray-900 mr-2 p-2 border border-gray-300 rounded-full">
        <i class="ti ti-arrow-left"></i>
      </button>
      <h1 class="text-2xl font-bold text-purple-700">User Todos</h1>
    </div>
    <ul class="space-y-4">
      <li v-for="todo in todos" :key="todo.id" class="bg-white p-4 rounded-lg shadow-md">
        <div class="flex items-center">
          <input type="checkbox" :checked="todo.completed" class="mr-2" />
          <span :class="{ 'line-through': todo.completed }">{{ todo.title }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'UserTodos',
  data() {
    return {
      todos: []
    }
  },
  created() {
    const userId = this.$route.params.id;
    fetch(`https://jsonplaceholder.typicode.com/todos?userId=${userId}`)
      .then(response => response.json())
      .then(data => {
        this.todos = data;
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