<template>
  <div>
    <h1>당신의 취향을 저격할 상영중인 영화 TOP 10</h1>
      <!-- <p>{{ genres }}</p> -->
      <p>{{ getRecommendedList }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LastestMovies',
  data() {
    return {
      recommends: null
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
          // console.log(this.genres.length)
          const random_index = Math.floor(Math.random() * (this.genres.length))
          console.log(this.genres[random_index])
          const genre = this.genres[random_index]
          const recommend_movies = res.data.filter((movie) => {
            return movie.genres.includes(genre)
          })
          // console.log(recommend_movies)
          const randommovie5 = recommend_movies.sort(() => 0.5 - Math.random())
          this.recommends = randommovie5.splice(0, 4)
          // console.log(this.recommends)
        })
        .catch((err) => {
          console.log(err)
        })
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