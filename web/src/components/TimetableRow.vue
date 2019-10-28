<template>
  <div class="grid" :class="{'short': !info, 'hidden': !visible}">
    <div class="time">{{time}}</div>
    <Icon :icon="icon" size="normal" />
    <div class="title">{{title}}</div>
    <div class="break-time" v-if="info">{{breakDuration}} mins</div>
    <div class="line" v-if="info"></div>
    <div class="info" v-if="info">
      <div v-if="teacher" class="cluster">
        <Icon icon="person" size="small" />
        <span>{{teacher}}</span>
      </div>
      <div v-if="room" class="cluster">
        <Icon icon="location_pin" size="small" />
        <span>{{room}}</span>
      </div>
      <div v-if="flag" class="flag">{{flag}}</div>
    </div>
  </div>
</template>

<script>
import Icon from "../components/Icon.vue";

export default {
  components: {
    Icon
  },
  props: {
    time: String,
    icon: String,
    title: String,
    breakDuration: String,
    teacher: String,
    room: String,
    flag: String,
    info: {
      default: true,
      type: Boolean
    },
    visible: {
      default: true,
      type: Boolean
    }
  },
  watch: {
    visible(val) {
      this.visible = val;
    }
  }
};
</script>

<style lang="scss" scoped>
.grid {
  display: grid;
  grid-template-columns: 6rem 4rem auto;
  grid-template-rows: auto 6rem;
  row-gap: 1rem;
  padding-bottom: 1rem;
  &.hidden {
    display: none;
  }

  &.short {
    grid-template-rows: auto;
  }

  .time {
    display: inline-block;
    align-self: center;
    justify-self: center;
    min-width: 5rem;
    padding-left: 24px;
  }
  .title {
    display: inline-block;
    overflow: hidden;
    text-overflow: ellipsis;
    padding-right: 24px;
    align-self: center;
  }
  .break-time {
    grid-column: 1;
    align-self: flex-end;
    text-align: end;
    font-size: 75%;
    padding-bottom: 0.55em;
    color: #ffcc33;
  }
  .line {
    height: 8rem;
    background: linear-gradient(#ffcc33, #ffcc33) no-repeat bottom center / 2px
        30%,
      linear-gradient(#515355, #515355) no-repeat top center / 2px 100%;
    grid-column: 2;
  }
  .info {
    grid-column: 3;
    font-weight: 300;
    line-height: 1.2rem;
    .cluster {
      padding-top: 0.5rem;
    }
    span {
      padding-left: 0.2rem;
    }
    .flag {
      margin-top: 0.5em;
      display: inline-block;
      background: #e53459;
      border-radius: 0.5rem;
      text-align: center;
      font-weight: 500;
      padding: 0.3rem 0.5rem 0.3rem 0.5rem;
    }
  }
}
</style>