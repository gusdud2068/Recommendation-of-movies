<template>
  <div class="user-wrap">
    <img @click="imgclick()"  :src="`https://image.tmdb.org/t/p/original/${movie?.backdrop_path}`" class="backimg" alt="...">
    <div class="user-text">
    <h1><img src="@/assets/sparkling.gif" width="5%" class="sparkling"><span style="color:orange;text-shadow: 1px 3px black, 0 1.5px navy, 1.5px 0 navy, 0 -1.5px navy; font-size: 30px; ">  THIS MOVIE IS :   </span><span style="text-shadow: 2px 0px 0px white">"{{ movie?.title }}"</span><img src="@/assets/sparkling.gif" width="5%"></h1><hr>
    <!-- 포스터 없이 바로 트레일러 나올 수 있도록 만들어보자 -->
    <div style="display:flex;">
    <img @click="movieVideo(movie)" :src="`https://www.themoviedb.org/t/p/original${movie?.poster_path}`" alt="" style="height:600px; margin-right:10px;">
    
    <div style="text-align:left;line-height:20px;">
    <!-- 평점 if 문으로 별로 구현하기 -->
    <p style="font-family:'yang';text-shadow: 2px 0px 0px white"><span style="color:orange;">V</span>OTE_<span style="color:orange;">A</span>VERAGE : {{ movie?.vote_average }}</p>
    <p style="font-family:'yang';text-shadow: 2px 0px 0px white"><span style="color:orange;">R</span>ELEASE_<span style="color:orange;">D</span>ATE : {{ movie?.release_date }}</p>
    <p v-if="movie?.overview" style="font-family:'yang';text-shadow: 1px 1px 0px white"><span style="color:orange;">O</span>VERVIEW :<span style="font-family:overview; font-weight:bold;">{{ movie?.overview }}</span></p>
    <iframe :src="`https://www.youtube.com/embed/${video}?autoplay=1`" frameborder="0" style="height:300px; width:450px"></iframe>
    </div>
    
    </div>
    <hr>
      <LatestMovies
        :genres="genres"
      />
    </div>
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
      video: null,
      isClicked: false,
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
        axios({
          method:'get',
          url: `https://api.themoviedb.org/3/movie/${movie.id}/videos?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR`,
        })
        .then((res) => {
          const video = res.data.results[0].key
          this.video = video
          // this.video = `https://wwww.youtube.com/embed/${video}?autoplay=1`
          console.log(this.video)
          // this.$store.state.movieVideo= res.data.results[0]
          // console.log(this.$store.state.movieVideo)
        })
        .catch((err) => {
          console.log(err)
        })
    },   

  },
  created() {
    this.getDetail()
  },
  // watch: {
  //   movieTrailer() {
  //     this.movieVideo(this.movie)
  //   }
  // }
}
</script>

<style>
.backimg{
    position:fixed;
    top: 0%;
    right:0px;
    width:100%;
    height: 100vh;
    vertical-align: middle;
    opacity: 0.3;
    z-index: -1;
}
.user-wrap{
    width:100%;
    position: relative;
    
}
.user-text{
    position:absolute;
    top: 10%;
    left: 50%;
    transform: translate( -50%, -50% );
    /* color: white; */
    /* display: flex; */
    height: 100%;
    /* margin-top: 100px; */
    z-index: 2;
}
.sparkling{
  transform: rotateY( 180deg ) ; 
}
.logo2{
    z-index: 2;
}

</style>