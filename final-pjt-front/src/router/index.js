import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie/:id',
    name: 'movie',
    component: MovieView,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
