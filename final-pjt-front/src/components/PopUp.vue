<template>
  <div>
    <h1>팝업창</h1>
        <img @click="closePopup()" src="../assets/close-img.png" alt="" width="30px" height="30px">
    <form @submit.prevent="updateComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="80" rows="3" v-model="comment_content"></textarea><br>
      <input @click="updateComment" class="btn btn-warning" type="submit" id="submit" style="width:20%" value="수정">  
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'PopUp',
    data() {
        return {
            comment_content: null,
        }
    },
    props: {
        comment: Object,
        latestmovie: String,
    },
    methods: {
        // 팝업 창 닫기
        closePopup() {
            this.$emit('close-popup')
        },
        // 댓글 가져오기
        // created ? mounted ? 생각해보기 (created 실행해보기)
        getComment() {
            let token = localStorage.getItem('jwt')
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
            .then((res) => {
                console.log(res.data)
                this.comment_content = res.data.content
            })
            .catch((err) => {
                console.log(err)
            })
        },
        // 댓글 수정
        // 수정 후 댓글 목록 다시 불러와야 함!
        updateComment() {
            const comment_content = this.comment_content
            if (!comment_content) {
                alert('댓글을 입력해주세요')
                return
            }
            let token = localStorage.getItem('jwt')
            axios({
                method: "put",
                url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
                data: {
                    content: comment_content,
                },
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
            .then(() => {
                // 댓글 수정 후 업데이트가 안됨
                // this.closePopup()
                // this.$store.dispatch('getComments', this.latestmovie)
                this.$emit('update-comment')
                location.reload();
                // ???/?
                
                // this.$router.push({ name: 'latestmovie', params: { latestmovie_id : `${this.latestmovie}`}})
            })
            .catch((err) => {
                console.log(err);
            });
        },
        
    },
    created() {
        this.getComment()
    },
}
</script>

<style>
/* .close-image {
    width: 10%;
    height: 10%;
} */

</style>