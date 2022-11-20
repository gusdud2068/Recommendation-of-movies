<template>
  <div>
    <h1>댓글 생성</h1>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="80" rows="3" v-model="comment_content"></textarea><br>
      <input class="btn btn-warning" type="submit" id="submit" style="width:20%">  
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
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/movie/${this.latestmovie}/comments/`,
        data: {
          content: comment_content,
        },
        headers: {
          // 수정??해야하는지 생각해보기
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.comment_content = null
          this.$store.dispatch('getComments', this.latestmovie)
          // this.$router.push({ name: 'latestmovie', params: { latestmovie_id : `${this.latestmovie}`}})
        })
        .catch((err) => {
          console.error(err);
        });
      }
    },
}
</script>

<style>

</style>