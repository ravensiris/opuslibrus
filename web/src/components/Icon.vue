<template>
  <div class="icon" :class="icon+' '+size">

  </div>
</template>

<script>
export default {
    props:{
        icon:String,
        size:String
    },
}
</script>

<style lang='scss' scoped>

.icon{
    display: inline-block;
    grid-column: 2;
    background-repeat: no-repeat;
    align-self: center;
    justify-self: center;
    &.normal{
        width: 2rem;
        height: 2rem;
    }
    &.small{
        width: 1rem;
        height: 1rem;
    }
    &.checkmark{
        background-image: url('../assets/img/checkmark.svg');
    }
    &.checked{
        background-image: url('../assets/img/checked.svg');
    }
    &.end{
        background-image: url('../assets/img/end.svg');
    }
    &.location_pin{
        background-image: url('../assets/img/location_pin.svg');
    }
    &.person{
        background-image: url('../assets/img/person.svg');
    }
    &.unchecked{
        background-image: url('../assets/img/unchecked.svg');
    }
    
}

</style>