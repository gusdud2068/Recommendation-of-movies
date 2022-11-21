<template>
  <div>
      <span v-for="movie in getRecommendedList" :key="movie.id">
        <span @click="GoCommunity(movie)" class="card text-bg-dark">
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img" alt="...">
        <div class="card-img-overlay">
          <!-- css 로 제목 잘보이게 만들기! -->
          <!-- 카드 margin 음수로 줘보기 -->
          <h5 class="card-title" style="font-family:'yang';text-shadow: 2px 2px 2px navy;">{{ movie.title }}</h5>
        </div>
      </span>
    </span>
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
          console.log(this.genres[random_index])
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
      this.$store.state.recommendname = movie
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