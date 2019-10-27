<template>
  <div id="app">
    <Navbar v-bind="nav" />
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'app',
  components: {
    Navbar
  },
  data(){
    return {
      nav: Navbar
    }
  }
}
</script>

<style lang='scss'>

@font-face {
  font-family: 'Poppins';
  src: url('assets\\fonts\\Poppins-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Poppins';
  src: url('assets\\fonts\\Poppins-Bold.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
}
@font-face {
  font-family: 'Poppins';
  src: url('assets\\fonts\\Poppins-Black.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}

*{
  margin: 0;
  font-family: 'Poppins';
  max-width: 100%;
  color: #EAEBEB;
  max-height: 100%;
}

$light-bg: #222427;

body{
  background-color: $light-bg;
  
}

#app{
  height: 100vh;
  max-height: 100vh;
}

input[type=text], input[type=password]{
  height: 3rem;
  border-radius: 6px;
  outline: none;
  border: none;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  width: 75vw;
  max-width: 36rem;
  padding: 6px;
  padding-left: 12px;
  padding-right: 12px;
  color: black;
  background-color: #EAEBEB;
  font-size: 1.3rem;
  cursor: text;
}

</style>
