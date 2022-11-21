<template>
  <div>
    <!-- 새로고침하면 제목사라짐,,., -->
    <h1>{{ getTitle.title }}</h1>
    <div style="display:flex; width: 80%; margin: auto; ">
      <iframe v-if="video" style="margin: auto;" v-show="content" :src="`https://www.youtube.com/embed/${video}?`" frameborder="0" width="1000" height="500"></iframe>
      <img v-else :src="`https://image.tmdb.org/t/p/original/${getTitle?.poster_path}`" alt="" style="width:700px; height: 900px;">
      <div>
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
</template>

<script>
import axios from 'axios'
import CommentCreate from '@/components/CommentCreate'
import CommentList from '@/components/CommentList'

export default {
  name: 'CommunityView',
  computed: {
    getTitle() {
      return this.$store.state.recommendname
    }
  },
  components: { CommentCreate, CommentList },
  data() {
    return {
      latestmovie: null,
      video: null,
      content: false,
    }
  },
  methods: {
    getMovie() {
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
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComments() {
      this.$store.dispatch('getComments', this.latestmovie)
    }
  },
  created() {
    this.getMovie()
  },
  watch: {
    latestmovie() {
      this.getComments()
    }
  }
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
    /* color: white; */
    display: flex;
    height: 100%;
    /* margin-top: 100px; */
    z-index: 2;
}
</style>