<template>
  <div>
    <h1>{{ movie?.title }}</h1>
    <!-- <img :src="`https://www.themoviedb.org/t/p/original${movie?.poster_path}`" alt=""> -->
    <iframe :src= movieVideo(movie) frameborder="0"></iframe>
    <p>개봉날짜 : {{ movie?.release_date }}</p>
    <!-- 평점 if 문으로 별로 구현하기 -->
    <p>평점 : {{ movie?.vote_average }}</p>
    <p v-if="movie?.overview">줄거리 : {{ movie?.overview }}</p>
      <LatestMovies
        :genres="genres"
      />
  </div>
</template>

<script>
import axios from 'axios'
import LatestMovies from '@/components/LatestMovies'

export default {
  name: 'MovieView',
  components: { LatestMovies },
  data() {
    return {
      movie: null,
      genres: null,
    }
  },
  computed: {
 

  },
  methods: {
    getDetail() {
      const movie_id = this.$route.params.id
      // console.log(typeof(movie_id))
      // console.log(movie_id)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/'
      })
        .then((res) => {
          // console.log(res.data)
          // console.log(res.data.movie_id)
          const detail = res.data.filter((movie) => {
            return movie.id === Number(movie_id)
          })
          const genres = detail[0].genres
          this.genres = genres
          console.log(this.genres)
          this.movie = detail[0]
          // console.log(this.movie)
        })
      },
     movieVideo(movie){
      let video = null
      console.log(movie)
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${movie.id}/videos?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR`,
      })
      .then(res=>{
        video = res.data.results[0].key
        // this.$store.state.movieVideo= res.data.results[0]
        // console.log(this.$store.state.movieVideo)
      })
      .catch(err=>{
        console.log(err)
      })
      console.log(video)
      return video
    }       

  },
  created() {
    this.getDetail()
  }
}
</script>

<style>

</style>