<template>
  <div>
    <h1>최신 영화</h1>
    <div v-for="movie in moviesList" :key="movie.id">
      <div v-if="movie">

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LastestMovies',
  methods: {
    
  },
  computed: {
    moviesList() {
      return this.$store.state.moviesList
    }
  }
}
</script>

<style>

</style>