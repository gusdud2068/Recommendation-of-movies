<template>
  <div>
    <p>작성자: {{ comment.username }}</p>
    <p>내용: {{ comment.content }}</p>
    <p>{{ comment.like_users }}</p>
    <div v-if="isLiked">
      <button @click="likesChange()">좋아요 취소</button>
    </div>
    <div v-else>
    <button @click="likesChange()">좋아요</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data() {
    return {
      likecnt : 0,
      dislikecnt : 0,
      isLiked: false,
      likeCount: 0,
    }
  },
  methods: {
    likesChange() {
      // console.log(a)
      let token = localStorage.getItem('jwt')
      this.isLiked = !this.isLiked
      // console.log(token)

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/like/`,
        headers: {
          Authorization: `Bearer ${token}`
        },
      })
        .then((res) => {
          console.log(res.data.is_liked)
          this.likeCount = res.data.like_count
          // this.$store.dispatch('getComments', this.latestmovie)
        })
    },    
  },
}
</script>

<style>

</style>