<template>
  <div>
  <h1 style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white">댓글 목록</h1>
    <!-- <div class="toast-container position-static">
    <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="orange"></rect></svg>
        <strong class="me-auto">{{ comment.username }}</strong>
        <small class="text-muted">{{ comment.created_at }}</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body"> -->
        <CommentListItem
          v-for="comment in comments"
          :key="comment.id"
          :comment="comment"
          :latestmovie="latestmovie"
        />
      <!-- </div> -->
  </div>

  <!-- <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="auto"></rect></svg>
      <strong class="me-auto">작성자이름</strong>
      <small class="text-muted">댓글작성시간</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
          <CommentListItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
    :latestmovie="latestmovie"/>
        </div>
  </div> -->
  <!-- </div> -->
</template>
  <!-- 댓글 삭제 후 emit 으로 보내서 업데이트 가능??? -->
  <!-- computed 함수는 실행 못하나봐요.. -->
  <!-- ListItem 에서 다시 store 에 저장하도록 해결 -->

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
  name: 'CommentList',
  components: {CommentListItem},
  props: {
    latestmovie: String,
  },
  computed: {
    // store 에서 해당 영화의 comments 가져오기
    comments() {
      // console.log(this.$store.state.comments)
      return this.$store.state.comments
    }
  },
  methods: {

  }
}
</script>

<style>

</style>