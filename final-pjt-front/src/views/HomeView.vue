<template>
  <div>
    <div class="input-size">
      <input v-model="inputValue" type="text" placeholder="영화제목을 입력!" @keyup.enter="searchMovie(inputValue)">
    </div>
    <div class="center">
      <MovieCard
        v-for="movie in moviesList" :key="movie.id"
        :movie="movie"
        class="col-3"
      />
    </div>
  </div>
</template>


<script>
import MovieCard from '@/components/MovieCard'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: { MovieCard },
  data() {
    return {
      inputValue: null,
      searcharr:[]
    }
  },
  computed: {
      moviesList() {
          return this.$store.state.moviesList
      }
  },
  methods: {
    searchMovie(inputValue) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
      })
        .then((res) => {
          for(let i=0; i<res.data.length; i++){
            if (res.data[i].title.includes(inputValue)) {
              this.searcharr.push(res.data[i])
            }
          }
          this.$store.dispatch("save_search_result", this.searcharr)
          this.$router.push({ name: 'SearchList'})
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>
.input-size {
  width: 1000px;
  margin: auto;
}
.center {
  margin-left: 300px;
  /* margin: auto; */
}

</style>