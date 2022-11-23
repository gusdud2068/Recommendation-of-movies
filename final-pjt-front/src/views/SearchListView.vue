<template>
  <div>
    <div class="input-size">
      <input v-model="inputValue" type="text" placeholder="영화제목을 입력!" @keyup.enter="searchMovie(inputValue)">
    </div>
    <div class="center">
        <MovieCard
            v-for="movie in searchList"
            :key="movie.id"
            :movie="movie"
            class="col-3"
        />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'

export default {
    name: 'SearchListView',
    data() {
    return {
      inputValue: null,
      searcharr:[]
    }
  },
    components: {
        MovieCard,
    },
    computed: {
        searchList() {
            return this.$store.state.searchList
        }
    },
    methods: {
        searchMovie(inputValue) {
        axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/movies/',
        })
            .then((res) => {
                this.searcharr = []
                for(let i=0; i<res.data.length; i++){
                    if (res.data[i].title.includes(inputValue)) {
                    this.searcharr.push(res.data[i])
                    }
                }
                this.$store.dispatch("save_search_result", this.searcharr)
                this.$router.push({ name: 'SearchList'}).catch(() => {})
            })
            .catch((err) => {
                console.log(err)
            })
        },
    },
}
</script>

<style>

</style>