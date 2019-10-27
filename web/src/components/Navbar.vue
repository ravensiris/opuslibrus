<template>
  <div class="navbar">
      <div class="title">{{title}}</div>
      <div class="action">
          <a href="#">Home1</a>
          <a href="#">Home2</a>
          <a href="#">Home3</a>
      </div>
  </div>
</template>

<script>
export default {
    props:{
        title: String
    }
}
</script>

<style lang='scss' scoped>
$bg-dark: #1B1E20;

.navbar{
    display: flex;
    width: 100%;
    background-color: $bg-dark;
    height: 5rem;
    justify-content: space-between;
    .title{
        position: relative;
        display: inline-block;
        font-size: 2rem;
        font-weight: 500;
        left:1rem;
        line-height: 2rem;
        align-self: center;
    }
    .action{
        display: inline-block;
        position: relative;
        align-self: center;
        justify-self: end;
        right: 1rem;
        a{
            padding-left: 0.3rem;
            padding-right: 0.3rem;
            color: cyan;
            text-decoration: none;
        }
    }
}

</style>