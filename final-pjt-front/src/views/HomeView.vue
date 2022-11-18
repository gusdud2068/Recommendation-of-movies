<template>
    <div>
      <MovieCard
          v-for="movie in moviesList" :key="movie.id"
          :movie="movie"
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