import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import CommunityView from '@/views/CommunityView'
import SearchListView from '@/views/SearchListView'
import NotFound404 from '@/views/NotFound404'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/search',
    name: 'SearchList',
    component: SearchListView,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/movie/:id',
    name: 'movie',
    component: MovieView,
  },
  {
    path: '/movie/community/:latestmovie_id',
    name: 'latestmovie',
    component: CommunityView,
  },
  {
    path: '*',
    redirect: { name: 'NotFound404' }
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
