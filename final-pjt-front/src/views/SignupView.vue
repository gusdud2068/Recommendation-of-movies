<template>
  <div class="signup" style="text-align:left;">
    <div class="mainsignup">
    <hr class="line">
    <h1 style="color:black;text-align:center">Signup</h1>
    <hr class="line">
    <div>
      <label for="username" style="font-family:VITRO CORE TTF; color:black;" >사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username" />
    </div>
    <div>
      <label for="password" style="font-family:VITRO CORE TTF;color:black;">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" />
    </div>
    <div>
      <label for="passwordConfirmation" style="font-family:VITRO CORE TTF;color:black;">비밀번호 확인: </label>
      <input
        v-model="credentials.passwordConfirm"
        @keyup.enter="signup"
        type="password"
        id="passwordConfirmation"
      />
    </div>
    <button class="btn btn-warning" @click="signup" style="font-family:VITRO CORE TTF;color:black;" >회원가입</button>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignupView",
  data: function() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirm: null,
      },
    };
  },
  methods: {
    signup: function() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: this.credentials,
      })
        .then(() => {
          alert("회원가입 성공!");
          this.$router.push({ name: "Login" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
  .signup{
    margin-top: 55px;
    height: 100vh;
    color: white;
    position: relative;
  }
  .mainsignup{
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
  .line{
    background: orange;
    height: 3px;
  }
</style>
