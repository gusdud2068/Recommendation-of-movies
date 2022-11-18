import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    moviesList: [],
    movieVideo: [],
    comments: [],
  },
  getters: {
  },
  mutations: {
    GET_COMMENTS(state, comments) {
      state.comments = comments
    },
  },
  actions: {
    // 최신영화에 달린 댓글 목록 가져오기
    getComments(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/comments/${movie_id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_COMMENTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
