<template>
  <div>
    <div style="margin-top: 10px">
      <p>작성자: {{ comment.username }}</p>
      <p>내용: {{ comment.content }}</p>
      <input @click="openPopup()" class="btn btn-warning" type="submit" id="submit" style="width:20%; margin-right: 5px;" value="수정">
      <input @click="deleteComment" class="btn btn-warning" type="submit" id="submit" style="width:20%" value="삭제">
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
    // 팝업창에서 수정 후 댓글 업데이트

    // **********************
    // 같은 댓글 연속으로 여러 번 수정 시 중간에 댓글 내용이 업데이트가 안됨
    updateComment() {
      console.log(this.comment)
      this.$store.dispatch('getComments', this.latestmovie)
    },
    // 댓글 삭제
    // 댓글 삭제 후 댓글 목록 다시 업데이트 하려면,,,?
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
                // this.$emit('update-commentlist')
                // store 에서 댓글 다시 가져오기 실행??
                // 해결!!!
                this.$store.dispatch('getComments', this.latestmovie)
                alert('댓글이 삭제되었습니다.')
            })
            .catch((err) => {
                console.log(err)
            })
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
/* ******************** */
/* 팝업창 정 가운데에 맨 위에 위치하도록 만들어보자 */
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