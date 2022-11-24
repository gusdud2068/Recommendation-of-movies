<template>
  <div class="card" id="cardhover">
    <img @click="movieDetail()" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
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
    movieDetail() {
      this.$store.dispatch('saveImageMovie', this.movie.backdrop_path)
      this.$router.push({ name: 'movie', params: { id: `${this.movie.id}`}})
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
  align-items:flex-start;
  flex-wrap:wrap;
}
#cardhover:hover {
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
