<template>
    <div class="center">
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

<style>
.center {
  margin-left: 140px;
  margin-right: 90px;
}
/* div:hover{
  background-image: url(https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80);
} */
</style>