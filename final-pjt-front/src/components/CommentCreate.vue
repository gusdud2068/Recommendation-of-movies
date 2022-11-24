<template>
  <div>
    <h1 style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white">댓글</h1>
    <form @submit.prevent="createComment">
      <label for="content" style="font-family:'yang';font-weight: light; text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white; "> 댓글을 남겨주세요: </label>
      <textarea class="toast fade show" id="content" cols="80" rows="3" v-model="comment_content" style=""></textarea><br>
      <input class="btn btn-warning" type="submit" id="submit" style="width:20%; height: 10%;">  
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentCreate',
  data() {
    return {
      comment_content: null,
    }
  },
  props: {
    latestmovie: String,
  },
  methods: {
    createComment: function() {
      const comment_content = this.comment_content
      if (!comment_content) {
        alert('댓글을 입력해주세요')
        return
      }
      let token = localStorage.getItem('jwt')
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/movie/${this.latestmovie}/comments/`,
        data: {
          content: comment_content,
        },
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(() => {
          this.comment_content = null
          this.$store.dispatch('getComments', this.latestmovie)
        })
        .catch((err) => {
          alert('로그인 후 이용 가능합니다.')
          console.error(err);
        });
      }
    },
}
</script>

<style>

</style>