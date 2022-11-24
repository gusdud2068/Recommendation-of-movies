<template>
  <div class="user-wrap1">
    <!-- 새로고침하면 제목사라짐,,., 해결 완.-->
    <!-- store 에 저장할 때 vuex-persistedstate 를 이용해서 store의 state 초기화 방지 -->
    <img v-if="getBackgroundImage2" :src="`https://image.tmdb.org/t/p/original/${getBackgroundImage2}`" class="backimg1" alt="...">
    <div class="all1">
    <h1 class="font" style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white; z-index: 3;" @click="godetail(getMovie)" >
      <img src="@/assets/sparkling.gif" width="5%" class="sparkling">{{ getMovie.title }}<img src="@/assets/sparkling.gif" width="5%" class="sparkling">
      <!-- <button class="btn btn-warning" style="width:40px; height: 20px;" >자세히</button> -->
    </h1>
    <div class="user-text1">
    <div style="display:flex; width: 80%; margin-top: 60px; ">
      <iframe v-if="video" class="video" style="margin: auto;" v-show="content" :src="`https://www.youtube.com/embed/${video}?`" frameborder="0" width="1200" height="500"></iframe>
      <img class="video" v-else :src="`https://image.tmdb.org/t/p/original/${getMovie.poster_path}`" alt="" style="width:700px; height: 900px;">
      <div style="margin-left:30px">
        <CommentCreate
        :latestmovie="latestmovie"
        />
        <hr>
        <CommentList
        :latestmovie="latestmovie"
        />
      </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentCreate from '@/components/CommentCreate'
import CommentList from '@/components/CommentList'

export default {
  name: 'CommunityView',
  components: { CommentCreate, CommentList },
  data() {
    return {
      latestmovie: null,
      movie: null,
      video: null,
      content: false,
    }
  },
  computed: {
    getMovie() {
      return this.$store.state.latestmovie
    },
    getBackgroundImage2() {
      console.log(this.$store.state.backdrop_url2)
      return this.$store.state.backdrop_url2
    }
  },
  methods: {
    godetail(movie){
      this.$router.push({name:'movie',params:{id:`${movie.id}`}})
    },
    getVideo() {
      this.latestmovie = this.$route.params.latestmovie_id
      axios({
          method:'get',
          url: `https://api.themoviedb.org/3/movie/${this.latestmovie}/videos?api_key=8ffb4b999f9e6cb3f99f17488652cc28&language=ko-KR`,
        })
        .then((res) => {
          if (res.data.results) {
            const video = res.data.results[0].key
            this.video = video
            this.content = true
          console.log(this.getMovie)
          }
        })
        .catch((err) => {
          console.log(err)
        })
      this.$store.dispatch('getComments', this.latestmovie)
    },
    // 댓글이 없을 때 404 에러 발생, 댓글 작성 후에는 괜찮음
    // 해결 필요!
  },
  created() {
    this.getVideo()
  },

}
</script>

<style>
.user-wrap1{
  width:100%;
  position: relative;
    
}
.user-text1{
  position:absolute;
  top: 10%;
  left: 50%;
  transform: translate( -50%, -50% );
  display: flex;
  height: 100%;
  margin-top: 50px;
  justify-content: center;
  z-index: 2;
}
.video{
  box-shadow: 5px 5px 5px;
  margin-bottom: 80px !important;
  z-index: 1;
}
.font{
  margin-bottom: 80px;
  border: 2;
  width: 90%;
  height: 3px;
}
.backimg1{
  position:fixed;
  top: 0%;
  right:0px;
  width:100%;
  height: 100vh;
  vertical-align: middle;
  filter: brightness(60%);
  z-index: -100;
}
.all1{
  display: flex;
  justify-content: center;
  margin-bottom: 80px;
}
</style>