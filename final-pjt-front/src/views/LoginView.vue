<template>
  <div class='login' style="text-shadow: 1px 3px white, 0 1.5px white, 1.5px 0 white, 0 -1.5px white">
    <div class="mainlogin">
    <hr class="line">
    <h1 style="color:black;text-align:center">Login</h1>
    <hr class="line">
    <div>
      <label for="username" style="font-family:VITRO CORE TTF; color:black;">아이디: </label>
      <input type="text" id="username" v-model="credentials.username" />
    </div>
    <div>
      <label for="password" style="font-family:VITRO CORE TTF; color:black;">비밀번호: </label>
      <input
        type="password"
        id="password"
        v-model="credentials.password"
        @keyup.enter="login"
      />
    </div>
    <button class="btn btn-warning" @click="login" style="font-family:VITRO CORE TTF;color:black;">로그인</button>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data: function() {
    return {
      credentials: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    login: function() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: this.credentials,
      })
        .then((res) => {
          localStorage.setItem("jwt", res.data.access);
          this.$emit("login");
          this.$router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
  .login{
    margin-top: 55px;
    height: 100vh;
    color: white;
    position: relative;
  }
  .mainlogin{
    line-height: 30px;
    position:absolute;
    top: 20%;
    left: 50%;
    transform: translate( -50%, -50% );
    text-align: left;
    width: 50%;
  }
  input{
    width: 100%;

  }
  .btn{
    width: 100%;
    height: 50px;
    margin-top: 10px;
    background-color: orange;
  }

</style>