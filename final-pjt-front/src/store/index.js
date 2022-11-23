import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      // paths: [""]
    })
  ],
  state: {
    moviesList: [],
    movieVideo: [],
    comments: [],
    // recommendname: [],
    latestmovie: [],
    searchList: [],
  },
  getters: {
  },
  mutations: {
    GET_COMMENTS(state, comments) {
      state.comments = comments
    },

    SAVE_SEARCH_RESULT(state, result) {
      state.searchList = result
    }
  },
  actions: {
    // 최신영화에 달린 댓글 목록 가져오기
    getComments(context, movie_id) {
      let token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/comments/`,
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then((res) => {
          // for (let i=0; i < res.data.length; i++) {
          const movie_comment = res.data.filter((movie) => {
            return movie.movie === Number(movie_id)
          })
          // console.log(movie_comment)
          // }
          console.log(movie_comment)
          context.commit('GET_COMMENTS', movie_comment)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    save_search_result(context, result) {
      context.commit("SAVE_SEARCH_RESULT", result)
    }
  },
  modules: {
  }
})
