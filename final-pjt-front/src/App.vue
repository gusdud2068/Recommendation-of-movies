<template>
  <div id="app">
    <br>
  <img src="@/assets/logo.png" width="50%">
    <nav>
      <nav class="navbar navbar-expand-lg" style="background-color:white;text-shadow: 2px 1px 0px black; text-decoration-line: underline;">
    <div class="container-fluid">
    <router-link class="nav-link active" @click.native="moviesList" :to="{ name: 'home' }">MOVIE</router-link>
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
    <span v-show="isLoggedIn">
      <router-link @click.native="logout" to="#">Logout</router-link>
    </span>
    <span v-show="!isLoggedIn">
      <router-link :to="{ name: 'Signup' }">Signup</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link>
    </span>
    </div>
  </div>
</nav>

    </nav>
    <router-view @login="changeLog"/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
    };
  },
  methods: {
    logout() {
      this.isLoggedIn = false;
      localStorage.removeItem("jwt");
      this.$router.push({ name: "Login" });
    },
    changeLog(){
      this.isLoggedIn = true;
      console.log(this.isLoggedIn)
    },
    moviesList() {
      const URL = 'http://127.0.0.1:8000/movies/'
      axios({
        method: 'get',
          url: URL,
      }).then((response) => {
        // console.log(response.data)
          this.$store.state.moviesList = response.data
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  created() {
    this.moviesList()
    const token = localStorage.getItem("jwt");
    if (token) {
      this.isLoggedIn = true;
    }
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif, VITRO CORE TTF;
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
  color: orange;
  font-family:'VITRO CORE TTF';
}

nav a.router-link-exact-active {
  color: orange
}
.v-application {
  font-family: 'VITRO CORE TTF', sans-serif !important;
}
@font-face {
  font-family:'VITRO CORE TTF';
  src: url('assets/VITRO CORE TTF.ttf') format('truetype');
  font-weight: 400;
}
</style>
