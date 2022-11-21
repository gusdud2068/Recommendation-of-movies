<template>
  <div>
    <div style="margin-top: 10px">
      <p>작성자: {{ comment.username }}</p>
      <p>내용: {{ comment.content }}</p>
      <input @click="updateComment" class="btn btn-warning" type="submit" id="submit" style="width:20%; margin-right: 5px;" value="수정">
      <input @click="deleteComment" class="btn btn-warning" type="submit" id="submit" style="width:20%" value="삭제">
      <hr>
    </div>
    <!-- <p>{{ comment.like_users }}</p> -->
    <!-- 좋아요 실패., -->
    <!-- <div v-if="isLiked">
      <button @click="likesChange()">좋아요 취소</button>
    </div>
    <div v-else>
    <button @click="likesChange()">좋아요</button>
    </div> -->
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
    updateComment() {

    },
    deleteComment() {

    },
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