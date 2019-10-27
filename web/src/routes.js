import HomePage from './views/HomePage.vue';
import LoginPage from './views/LoginPage.vue';

const routes = [
    {path: '/', component: HomePage},
    {path: '/login', component:LoginPage},
  
    {path: '*', redirect: '/'}
  ];
  
export default routes;