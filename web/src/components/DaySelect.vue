<template>
  <div class="day">
      <div class="numeric" :class="{'active':isActive}">
          {{numeric}}
      </div>
      <div v-if="isActive" class="literal">
          {{literal}}
      </div>
  </div>
</template>

<script>
export default {
    props:{
        isActive:Boolean,
        numeric:Number,
        literal:String
    }
}
</script>

<style lang='scss' scoped>

@keyframes dateDayAnimation{
    0%{
        transform: rotate(0) scale(0) translateY(-2em);
        }
    100%{
        transform: rotate(0) scale(1);
        }
}

@keyframes dateTextAnimation{
    0%{
        transform: rotate(0) translateY(0.5rem);
        font-size: 1rem;
        font-weight: 400;
        }
    100%{
        transform: rotate(0);
        font-size: 140%;
        font-weight: 500;
        }
}

.day{
    display: flex;
    flex-direction: column;
    justify-content: center;
    font-size: 1.2rem;
    height: 4rem;
    align-content: center;
    cursor: pointer;
    .numeric{
        align-self: center;
        &.active{
        animation: dateTextAnimation 250ms forwards 0s ease-in;
        font-size: 1.5rem;
        font-weight: 500;
        
    }
    }
    

    .literal{
        animation: dateDayAnimation 150ms forwards 0s ease-out;
        font-size: 1rem;
        line-height: 1rem;
        align-self: center;
        font-weight: 400;
    }
}

</style>