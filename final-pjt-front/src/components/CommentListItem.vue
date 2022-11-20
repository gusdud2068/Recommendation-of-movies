<template>
  <div>
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  }
}
</script>

<style>

</style>