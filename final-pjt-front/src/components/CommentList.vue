<template>
  <div>
  <h1>댓글 목록</h1>
  <CommentListItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
  />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
  name: 'CommentList',
  components: {CommentListItem},
  props: {
    latestmovie: String
  },
  method: {

  },
  computed: {
    // store 에서 해당 영화의 comments 가져오기
    comments() {
      // console.log(this.$store.state.comments)
      // console.log(this.$store.state.comments.comments)
      return this.$store.state.comments.comments
    }
  }
}
</script>

<style>

</style>