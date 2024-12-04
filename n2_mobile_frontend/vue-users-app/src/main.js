import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import UserList from './views/UserList.vue'
import UserProfileLayout from './views/UserProfileLayout.vue'
import UserTodos from './views/UserTodos.vue'
import UserPosts from './views/UserPosts.vue'
import UserAlbums from './views/UserAlbums.vue'
import AlbumPhotos from './views/AlbumPhotos.vue'
import './style.css'

const routes = [
  { path: '/', name: 'home', component: UserList },
  { path: '/users/:id', component: UserProfileLayout, children: [
    { path: '', name: 'user-detail', component: UserTodos, props: true },
    { path: 'todos', name: 'user-todos', component: UserTodos, props: true },
    { path: 'posts', name: 'user-posts', component: UserPosts, props: true },
    { path: 'albums', name: 'user-albums', component: UserAlbums, props: true },
  ]},
  { path: '/albums/:id', name: 'album-photos', component: AlbumPhotos, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')