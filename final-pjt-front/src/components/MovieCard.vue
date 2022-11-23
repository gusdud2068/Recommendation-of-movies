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
    console.log(movie.id)
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
  border: solid 1px black;
  overflow: hidden;
  transition-delay: 2ms;
}
.card-img-top{
  height: 700px;
}
/* 반응형 페이지에 따라 제목이 두 줄로 넘어가도 크기가 달라지지 않도록 body 크기 늘려줌 / 제목은 정가운데 배열로 변경 */
.card-body {
  height: 90px;
  display : flex;
  justify-content : center;
  align-items : center;
  float: left;
}
.card-title{
  font-size: 1.2rem;
}

</style>
