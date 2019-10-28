import Vue from "vue";
import App from "./App.vue";
import Router from "vue-router";
import routes from "./routes";

Vue.use(Router);

const router = new Router({ mode: "history", routes });

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
