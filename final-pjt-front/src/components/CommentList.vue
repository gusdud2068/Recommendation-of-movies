<template>
  <div>
  <h1>댓글 목록</h1>
  <CommentListItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
    :latestmovie="latestmovie"
  />
  <!-- 댓글 삭제 후 emit 으로 보내서 업데이트 가능??? -->
  <!-- computed 함수는 실행 못하나봐요.. -->
  <!-- ListItem 에서 다시 store 에 저장하도록 해결 -->
  </div>
</template>

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