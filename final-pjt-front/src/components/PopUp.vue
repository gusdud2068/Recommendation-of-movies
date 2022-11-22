<template>
  <div>
    <h1>팝업창</h1>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="80" rows="3" v-model="comment_content"></textarea><br>
      <!-- 수정 버튼 클릭시 axios 로 수정한 데이터 제출 -->
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
    },
    methods: {
        // 댓글 가져오기
        // created ? mounted ? 생각해보기
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
                alert('댓글이 수정되었습니다.')
                // ???/?

                // 수정 완료 후 store 에 댓글 저장해야 댓글 목록에 나오는 지 확인해보기
                // this.$store.dispatch('getComments', this.latestmovie)

                // this.$router.push({ name: 'latestmovie', params: { latestmovie_id : `${this.latestmovie}`}})
                })
                .catch((err) => {
                console.log(err);
                });
        },
        // 댓글 삭제
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
                    alert('댓글이 삭제되었습니다.')
                })
                .catch((err) => {
                    console.log(err)
                })
        }
    }
}
</script>

<style>

</style>