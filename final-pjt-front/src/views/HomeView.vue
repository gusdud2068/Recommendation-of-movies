<template>
    <div>
      <MovieCard
          v-for="movie in moviesList" :key="movie.id"
          :movie="movie"
      />
    </div>
</template>


<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard'

export default {
  name: 'HomeView',
  components: { MovieCard },
  computed: {
      moviesList() {
          // console.log(this.$store.state.movieList)
          return this.$store.state.moviesList
      }
  }
}
</script>