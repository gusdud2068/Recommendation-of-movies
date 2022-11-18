<template>
  <div>
    <h1>최신영화 트레일러, 댓글</h1>
    <iframe v-show="content" :src="`https://www.youtube.com/embed/${video}?`" frameborder="0"></iframe>
    <hr>
    <CommentCreate
      :latestmovie="latestmovie"
    />
    <hr>
    <CommentList
      :latestmovie="latestmovie"
    />

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
  computed: {

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

</style>