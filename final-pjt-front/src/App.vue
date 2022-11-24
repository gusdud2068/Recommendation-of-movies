<template>
  <div id="app">
    <img :src="`https://image.tmdb.org/t/p/original/${getImage}`" class="backimg" alt="..." >
  <br>
  <hr class="hrstyle">
  <div class="logo2 back">
  <img src="@/assets/logo2.png" width="100%" >
  <hr class="hrstyle">
  </div>
    <nav>
      <nav class="navbar navbar-expand-lg" style="text-shadow: -1px 0 navy, 0 1px navy, 1px 0 navy, 0 -1px navy; text-decoration-line: underline; z-index: 2;">
    <div class="container-fluid">
    <img src="@/assets/sun.png" width="70px" height="30px">
    <router-link class="nav-link active" @click.native="moviesList" :to="{ name: 'home' }">MOVIE</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
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
      }).then((res) => {
        let no_duplicate= []
        let result = []
        res.data.forEach((movie) => {
          if (!no_duplicate.includes(movie.id)) {
            no_duplicate.push(movie.id)
            result.push(movie)
          }
        })
        // console.log(no_duplicate)
        // console.log(result)

        this.$store.state.moviesList = result
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  computed: {
    getImage() {
      const moviesinfo = this.$store.state.moviesList
      const backdrop_paths = moviesinfo.filter((movie)=> {
        return movie.backdrop_path
      })
      const random_index = Math.floor(Math.random() * (backdrop_paths.length))
      console.log(backdrop_paths)
      console.log(random_index)
      const backgroundimage_url = backdrop_paths[random_index].backdrop_path
      return backgroundimage_url
    }
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
  /* background-color: navy; */
}

nav {
  padding: 10px;
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
@font-face {
  font-family:'yang';
  src: url('assets/yang.ttf') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family:'overview';
  src: url('assets/overview.ttf') format('truetype');
  font-weight: 400;
}
.hrstyle{
  margin: auto;
  border: 0;
  width: 90%;
  height: 3px;
  background: white;
  z-index: 2;
}
.back{
  background-color: rgba( 255, 255, 255, 0.3 );
}
</style>
