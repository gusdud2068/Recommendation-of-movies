<template>
  <div>
    <img
      @click="closePopup()"
      src="../assets/close-img.png"
      alt=""
      width="10px"
      height="10px"
      style="float: right"
    />
    <form @submit.prevent="updateComment">
      <label for="content"></label>
      <textarea
        id="content"
        cols="30"
        rows="3"
        v-model="comment_content"
      ></textarea
      ><br />
      <input
        @click="updateComment"
        class="btn btn-warning"
        type="submit"
        id="submit"
        style="width: 20%; height: 10%"
        value="완료"
      />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PopUp",
  data() {
    return {
      comment_content: null,
    };
  },
  props: {
    comment: Object,
    latestmovie: String,
  },
  methods: {
    closePopup() {
      this.$emit("close-popup");
    },
    getComment() {
      let token = localStorage.getItem("jwt");
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then((res) => {
          this.comment_content = res.data.content;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateComment() {
      const comment_content = this.comment_content;
      if (!comment_content) {
        alert("댓글을 입력해주세요");
        return;
      }
      let token = localStorage.getItem("jwt");
      axios({
        method: "put",
        url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
        data: {
          content: comment_content,
        },
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then(() => {
          this.$emit("update-comment");
          location.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getComment();
  },
};
</script>

<style>
</style>