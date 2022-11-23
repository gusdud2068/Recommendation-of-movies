<template>
    <div class="center">
      <MovieCard
          v-for="movie in moviesList" :key="movie.id"
          :movie="movie"
          class="col-3"
      />
    </div>
</template>


<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'HomeView',
  components: { MovieCard },
  computed: {
      moviesList() {
          return this.$store.state.moviesList
      }
  },
}
</script>

<style>
.center {
  margin-left: 300px;
}

</style>