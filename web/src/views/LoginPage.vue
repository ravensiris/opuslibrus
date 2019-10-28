<template>
  <form class="login-page" @submit.prevent="checkForm">
    <div class="centered">
      <input v-model="username" type="text" name="username" id="username" placeholder="Username" />
      <input
        v-model="password"
        type="password"
        name="password"
        id="password"
        placeholder="Password"
      />
    </div>
    <div class="bottomed">
      <input type="submit" value="LOG IN" />
    </div>
  </form>
</template>

<script>
import { LibrusService } from "../LibrusService.js";

const ls = new LibrusService();

export default {
  data() {
    return {
      username: null,
      password: null,
      router: this.$router
    };
  },

  methods: {
    checkForm() {
      if (this.username && this.password) {
        ls.getToken(this.username, this.password)
          .then(r => {
            localStorage.token = r.data.token;
            this.router.push("/");
          })
          .catch(e => {
            if (e.response.data.message) {
              alert(e.response.data.message);
            }
          });
      }
    }
  },

  beforeCreate() {
    if (localStorage.token) {
      ls.checkToken(localStorage.token).then(r => {
        if (r.data.valid) this.$router.push("/");
      });
    }
  },

  created() {
    this.$parent.nav.title = "Log in";
  }
};
</script>

<style lang='scss' scoped>
.login-page {
  height: calc(100% - 5rem); //minus navbar height
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 2rem 16rem 5rem 4rem 2rem;
  .centered {
    grid-row: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
  }
  .bottomed {
    grid-row: 4;
    display: flex;
    justify-content: center;
    input[type="submit"] {
      color: mix(#eaebeb, #222427, 12%);
      background: mix(#63d092, #222427, 63%);
      border-radius: 32px;
      outline: none;
      border: 1px #1b1e20 solid;
      font-size: 2rem;
      width: 20rem;
      height: 4rem;
      max-width: 80%;
      cursor: pointer;
      transition: color background-color;
      transition-duration: 350ms;
      font-weight: 700;

      &:hover {
        color: mix(#eaebeb, #222427, 100%);
        background: mix(#63d092, #222427, 80%);
        transition: color background-color;
        transition-duration: 350ms;
      }
      &:active {
        color: mix(#eaebeb, #222427, 1%);
        background: mix(#63d092, #222427, 45%);
        transition: color background-color;
        transition-duration: 350ms;
      }
    }
  }
}
</style>