<template>
  <div class="user-wrap">
    <img v-if="getBackgroundImage" :src="`https://image.tmdb.org/t/p/original/${getBackgroundImage}`" class="backimg" alt="...">
    <div class="user-text">
      <h1>
        <img src="@/assets/sparkling.gif" width="5%" class="sparkling">
        <span style="color:orange;text-shadow: 1px 3px black, 0 1.5px black, 1.5px 0 black, 0 -1.5px black; font-size: 30px; ">  THIS MOVIE IS :   </span>
        <span style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white">"{{ movie?.title }}"</span>
        <img src="@/assets/sparkling.gif" width="5%">
      </h1>
      <hr>
      <div style="display:flex;">
        <img :src="`https://www.themoviedb.org/t/p/original${movie?.poster_path}`" alt="" style="height:600px; margin-right:10px; border-radius:20px;">
    
        <div class="all">
          <div class="back1">
            <div style="text-align:left;line-height:20px;">
              <br>
              <p style="font-family:'yang';text-shadow: 1px 0px 0px white;">
                <span style="color:orange;">V</span>OTE_
                <span style="color:orange;">A</span>VERAGE : {{ movie?.vote_average }}
              </p>
              <p style="font-family:'yang';text-shadow: 1px 0px 0px white;">
                <span style="color:orange;">R</span>ELEASE_
                <span style="color:orange;">D</span>ATE : {{ movie?.release_date }}
              </p>
              <p v-if="movie?.overview" style="font-family:'yang'; text-shadow: 1px 0px 0px white;">
                <span style="color:orange;">O</span>VERVIEW :
                <span style="font-family:overview; font-weight:bold;"><br>{{ movie?.overview }}</span>
              </p>
            </div>
          </div>
          <div>
            <iframe v-if="video" :src="`https://www.youtube.com/embed/${video}?autoplay=1`" frameborder="0" style="height:300px; width:570px ;margin-top: 20px; box-shadow: 2px; border-radius: 20px;"></iframe>
          </div>
        </div>
      </div>
      <hr>
      <h1 v-if="check" style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white">당신의 <br> 
        <span style="color:orange">
          <img src="@/assets/sparkling.gif" width="4%" style="float:center">취향<img src="@/assets/sparkling.gif" width="4%" style="float:center"></span>을 <br>저격할 상영중인 영화
      </h1>
      <div class="movie_list">
        <LatestMovies
          :genres="genres"
          :movie="movie"
        />
      </div>
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
      check: false,
    }
  },
  computed: {
    getBackgroundImage() {
      return this.$store.state.backdrop_url
    }
  },
  methods: {
    getDetail() {
      const movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/'
      })
        .then((res) => {
          const detail = res.data.filter((movie) => {
            return movie.id === Number(movie_id)
          })
          const genres = detail[0].genres
          this.genres = genres
          this.movie = detail[0]
        })
        .catch((err) => {
          console.log(err)
          this.$router.push({ name: "NotFound404" })
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
        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkGenre(genres) {
      if (genres.length != 0) {
        this.check = true
      }
    } 
  },
  created() {
    this.getDetail()
  },
  watch: {
    movie() {
      this.movieVideo(this.movie)
    },
    genres() {
      this.checkGenre(this.genres)
    }
  }
}
</script>

<style>
h1{
  font-family:'VITRO CORE TTF';
}
.backimg{
    position:fixed;
    top: 0%;
    right:0px;
    width:100%;
    height: 100vh;
    vertical-align: middle;
    filter: brightness(60%);
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
    height: 100%;
    z-index: 2;
}

.sparkling{
  transform: rotateY( 180deg ) ; 
}

.logo2{
    z-index: 2;
}

.all {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.back1{
  background-color: rgba( 255, 255, 255, 0.65 );
  border-radius: 20px;
  padding: 20px;
}

.movie_list {
    display: flex;
    width: 1000px;
    overflow-x: scroll;
    scroll-behavior: smooth;
    height: 450px;
    overflow-y:hidden;
    white-space: nowrap;
}

.movie_list::-webkit-scrollbar{
  opacity: 0;
}

.movie_list::-webkit-scrollbar-thumb{
    background-color: orange;
}

</style>