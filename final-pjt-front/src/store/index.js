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
    latestmovie: [],
    searchList: [],
    backdrop_url: null,
    backdrop_url2: null,
  },
  getters: {
  },
  mutations: {
    GET_COMMENTS(state, comments) {
      state.comments = comments
    },

    SAVE_SEARCH_RESULT(state, result) {
      state.searchList = result
    },
    SAVE_IMAGE_MOVIE(state, url) {
      state.backdrop_url = url
    },
    SAVE_IMAGE_MOVIE2(state, url) {
      state.backdrop_url2 = url
    },
    SAVE_MOVIELIST(state, movielist) {
      state.moviesList = movielist
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
          const movie_comment = res.data.filter((movie) => {
            return movie.movie === Number(movie_id)
          })
          context.commit('GET_COMMENTS', movie_comment)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    save_search_result(context, result) {
      context.commit("SAVE_SEARCH_RESULT", result)
    },
    saveImageMovie(context, url) {
      context.commit('SAVE_IMAGE_MOVIE', url)
    },
    saveImageMovieLatest(context, url) {
      console.log(url)
      context.commit('SAVE_IMAGE_MOVIE2', url)
    },
    save_movielist(context, result) {
      context.commit('SAVE_MOVIELIST', result)
    }
  },
  modules: {
  }
})
