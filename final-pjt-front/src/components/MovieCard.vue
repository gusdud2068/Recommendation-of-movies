<template>
  <div class="card" id="cardhover">
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
    // console.log(movie.id)
    this.$store.dispatch('saveImageMovie', movie.backdrop_path)
    this.$router.push({ name: 'movie', params: { id: `${movie.id}`}})
  }
}
};
</script>

<style>
.card{
  float:left;
  width: 300px;
  height: 400px;
  margin: 10px;
  padding: 0px;
  overflow:auto;
  border-radius: 20px;
  font-family:'VITRO CORE TTF';
  /* opacity: 1; */
  align-items:flex-start;
  flex-wrap:wrap;
}
#cardhover:hover {
  /* 배경바꾸고 다시 보더 색 정하기 */
  border: solid 1px orange;
  overflow: hidden;
  transition-delay: 2ms;
}
.card-img-top{
  height: 700px;
}

.card-body {
  height: 90px;
  display : flex;
  justify-content : center;
  margin: auto;
  align-items : center;
  float: left;
}
.card-title{
  font-size: 1.2rem;
}

</style>
