<template>
  <div>
    <h1 style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white">댓글 목록</h1>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      :latestmovie="latestmovie"
    />
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
    comments() {
      return this.$store.state.comments
    }
  },
  methods: {
    updateComment() {
      this.$emit('update-comment', this.latestmovie)
    }
  }
}
</script>

<style>

</style>