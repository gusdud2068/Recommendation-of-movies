<template>
  <div class="card">
    <img @click="movieDetail(movie)" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <!-- <p class="card-text">{{ movie.overview }}</p> -->
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieCard',
  props: {
    movie: Object
  },
  methods: {
  movieDetail(movie) {
    console.log(movie.id)
    this.$router.push({ name: 'movie', params: { id: `${movie.id}`}})
  }
}
};
</script>

<style>
.card{
  float:left;
  height: 1000px;
  width: 30%;
  margin: 10px;
  padding: 0;
  overflow: hidden;
  border-radius: 20px;
  font-family:'VITRO CORE TTF';
  opacity: 1;
}
.card-img-top{
  height: 700px;
}

</style>
