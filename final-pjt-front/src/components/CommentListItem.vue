<template>
  <div v-if="comment">
    <div class="toast-container position-static">
      <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
          <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="orange"></rect></svg>
          <strong class="me-auto">{{ comment.username }} 님의 댓글</strong>
          <small class="text-muted">{{ comment.created_at | changeDate }}</small>
          <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" @click="deleteComment"></button>
        </div>
        <div class="toast-body">
          <div style="margin-top: 10px">
            <p>내용: {{ comment.content }}</p>
            <input @click="openPopup()" class="btn btn-warning" style="width:20%; height: 10%;" type="submit" id="update" value="수정">
            <hr>
            <div class="popup-view" :class="{ active : popupView }">
              <PopUp
                @close-popup="openPopup()"
                @update-comment="updateComment()"
                :comment="comment"
                :latestmovie="latestmovie"  
              />
            </div>
          </div>
        </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PopUp from '@/components/PopUp'

export default {
  name: 'CommentListItem',
  components: {
    PopUp
  },
  props: {
    comment: Object,
    latestmovie: String,
  },
  data() {
    return {
      likecnt : 0,
      dislikecnt : 0,
      isLiked: false,
      likeCount: 0,
      popupView: false,
    }
  },
  methods: {
    openPopup() {
      this.popupView = !this.popupView
    },
    updateComment() {
      this.$emit('update-comment', this.latestmovie)
    },
    deleteComment() {
      let token = localStorage.getItem('jwt')
      axios({
          method: "delete",
          url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
          headers: {
              Authorization: `Bearer ${token}`
          }
      })
      .then(() => {
        this.$store.dispatch('getComments', this.latestmovie)
        alert('댓글이 삭제되었습니다.')
        this.$router.go()
      })
      .catch((err) => {
          console.log(err)
      })
  },   
  },
  filters: {
    changeDate(value) {
      const changedate = value.slice(0, 10)
      const changetime = value.slice(11, 16)
      const result = `${changedate} | ${changetime}`
      return result
    }
  }
}
</script>

<style>
.popup-view{
  opacity: 0;
  display: none;
  visibility: hidden;
}

.active{
  opacity: 1;
  display: block;
  visibility: visible;
}

</style>