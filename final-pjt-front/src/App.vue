<template>
  <div id="app">
    <nav>
      <nav class="navbar navbar-expand-lg" style="background-color:#e3f2fd; color:white;">
    <div class="container-fluid">
    <router-link class="nav-link active" @click.native="moviesList" :to="{ name: 'home' }">Movie</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <!-- <li class="nav-item">
          <router-link class="nav-link" @click.native="moviesList" :to="{ name: 'random' }">Random</router-link>
        </li> -->
        <!-- <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'watchlist' }">WatchList</router-link>
        </li> -->
      </ul>
    </div>
  </div>
</nav>

    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  methods: {
    moviesList() {
      const URL = 'http://127.0.0.1:8000/movies/'
      axios({
        method: 'get',
          url: URL,
      }).then((response) => {
        console.log(response.data)
          this.$store.state.moviesList = response.data
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  created() {
    this.moviesList()
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
