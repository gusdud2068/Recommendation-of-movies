<template>
  <div style="display:flex">
      <div v-for="movie in getRecommendedList" :key="movie.id">
        <span @click="GoCommunity(movie)" class="card text-bg-dark">
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img" style="height:400px;" alt="...">
        <div class="card-img-overlay">
          <h5 class="card-title" style="font-family:'yang';  text-shadow: 2px 2px 2px navy; background-color: rgba( 0, 0, 0, 0.3 ); padding: 2px;">{{ movie.title }}</h5>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LatestMovies',
  components: {},
  data() {
    return {
      recommends: null,
    }
  },
  props: {
    genres: Array,
  },
  methods: {
      recommendMovie() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/now/'
      })
        .then((res) => {
          const random_index = Math.floor(Math.random() * (this.genres.length))
          const genre = this.genres[random_index]
          const recommend_movies = res.data.filter((movie) => {
            return movie.genres.includes(genre)
          })
          const randommovie9 = recommend_movies.sort(() => 0.5 - Math.random())
          this.recommends = randommovie9.splice(0, 9)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    GoCommunity(movie) {
      this.$store.state.latestmovie = movie
      console.log(this.$store.state.latestmovie)
      this.$store.dispatch('getComments', movie.id)
      this.$router.push({ name: 'latestmovie', params: { latestmovie_id : `${movie.id}`}})

    }
  },
  computed: {
    getRecommendedList() {
      return this.recommends
    }

  },
  watch: {
    genres() {
      this.recommendMovie()
    }
  }
}
</script>

<style>


</style>