import HomePage from "./views/HomePage.vue";
import LoginPage from "./views/LoginPage.vue";
import TimetablePage from "./views/TimetablePage.vue";

const routes = [
  { path: "/", component: TimetablePage },
  { path: "/h", component: HomePage },
  { path: "/login", component: LoginPage },

  { path: "*", redirect: "/" }
];

export default routes;
