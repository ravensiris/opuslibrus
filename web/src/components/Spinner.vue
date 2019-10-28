<template>
<div class="center">
    <div class="sbl-rect-spin-fill"></div>
</div>
  
</template>

<script>
export default {

}
</script>

<style scoped>

.center{
    position: absolute;/*important*/
    top: 50%;/*position Y halfway in*/
    left: 50%;/*position X halfway in*/
    transform: translate(-50%,-50%);/*move it halfway back(x,y)*/
    width: 8rem;/*any width*/
    height: 8rem;/*any height*/
}

.sbl-rect-spin-fill {
  color: #5a5a5a;
  height: 8rem;
  width: 8rem;
  position: relative;
  border: 4px solid;
  display: inline-block;
  animation: rect-rotate 1s  linear infinite; }

.sbl-rect-spin-fill::after {
  content: '';
  height: 0;
  width: inherit;
  display: block;
  background: rgba(90, 90, 90, 0.5);
  animation: fill-rect 1s linear infinite; }

@keyframes rect-rotate {
  0% {
    transform: rotate(0); }
  50%, 100% {
    transform: rotate(180deg); } }

@keyframes fill-rect {
  0%, 50% {
    height: 0; }
  100% {
    height: inherit; } }
</style>