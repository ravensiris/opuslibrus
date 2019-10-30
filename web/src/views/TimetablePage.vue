<template>
<div>
    <Spinner v-if="loading" />
    <EmptyInfo v-if="dayEmpty" />
  <div v-if="!loading" class="timetable" id="timetable">
      
      <div v-if="weekDays.length===7" class="daySelectors">
          <DaySelect :numeric="weekDays[0].getDate()" literal="MON" :isActive="now==0" @click.native="now = 0" />
          <DaySelect :numeric="weekDays[1].getDate()" literal="TUE" :isActive="now==1" @click.native="now = 1" />
          <DaySelect :numeric="weekDays[2].getDate()" literal="WED" :isActive="now==2" @click.native="now = 2" />
          <DaySelect :numeric="weekDays[3].getDate()" literal="THU" :isActive="now==3" @click.native="now = 3" />
          <DaySelect :numeric="weekDays[4].getDate()" literal="FRI" :isActive="now==4" @click.native="now = 4" />
          <DaySelect :numeric="weekDays[5].getDate()" literal="SAT" :isActive="now==5" @click.native="now = 5" />
          <DaySelect :numeric="weekDays[6].getDate()" literal="SUN" :isActive="now==6" @click.native="now = 6" />
      </div>
      <div class="pusher"></div>
    <TimetableRow
      :key="'d' + lesson.day.toString() + 'l' + lesson.index.toString()"
      v-for="lesson in timetable"
      :time="toTime(lesson.start)"
      :icon="getIcon(lesson.start, lesson.break_start)"
      :title="lesson.name"
      :breakDuration="getDuration(lesson.break_end, lesson.break_start)"
      :teacher="lesson.teacher"
      :room="'Room '+lesson.room"
      :flag="lesson.flag"
      :visible="lesson.day==now"
    />

    <TimetableRow v-if="tail" :time="toTime(tail.break_start)" icon="end" :info="false" />
  </div>
  </div>
</template>

<script>
import TimetableRow from "../components/TimetableRow.vue";
import EmptyInfo from "../components/EmptyInfo.vue";
import Spinner from "../components/Spinner.vue";
import DaySelect from "../components/DaySelect.vue";

import { LibrusService } from "../LibrusService";

const ls = new LibrusService();

export default {
  data() {
    return {
      timetable: null,
      router: this.$router,
      now: 0,
      tail: null,
      weekDays: [],
      loading: true,
      dayEmpty: false
    };
  },
  components: {
    TimetableRow,
    DaySelect,
    Spinner,
    EmptyInfo
  },
  mounted() {
    if (!localStorage.token) this.router.push("/login");
    ls.checkToken(localStorage.token).then(r => {
      if(!r.data.valid) this.router.push("/login");
    }).catch(e => {
      if(!e.response.data){
        alert('Trouble connecting to server.');
        this.router.push("/login");
      }else{
        if(!e.response.data.valid) this.router.push("/login");
      }
    });
    ls.getTimetable(localStorage.token)
      .then(r => {
        this.timetable = r.data.timetable;
        this.tail = this.getTail();
        const dayZero = this.timetable.filter(lesson => lesson.day == 0);
        if (dayZero){
            const x = Date.parse(dayZero[0].start);
            for(let i=0; i<=6; i++){
                const d = new Date(x+ i*86400000); //86400000 day in miliseconds
                this.weekDays.push(d);
            }
        }
        this.loading = false;
      });
  },
  created() {
    this.$parent.nav.title = "Classes";
  },
  methods: {
    toTime(d) {
      const date = new Date(Date.parse(d));
      return date.toLocaleString("en-US", {
        hour: "numeric",
        minute: "numeric",
        hour12: true
      });
    },
    getTail() {
      const nowLessons = this.timetable.filter(lesson => lesson.day == this.now);
      if (nowLessons.length===0){
          this.dayEmpty = true;
          return null;
      }
      this.dayEmpty = false;
      return nowLessons.reduce((a, b) => (a.index > b.index ? a : b));
    },
    getDuration(a, b) {
      return ((Date.parse(a) - Date.parse(b)) / 1000 / 60).toString();
    },
    getIcon(start, end){
        const _end = Date.parse(end);
        const now = Date.now();
        const hasEnded = (now - _end) >= 0;
        if (hasEnded) return 'checkmark';
        const _start = Date.parse(start);
        const hasStarted = (_start - now <= _end - _start);
        if (hasStarted){
            return 'checked';
        }else{
            return 'unchecked';
        }
    }
  },
  watch: {
    now(val) {
      this.now = val;
      this.tail = this.getTail();
    }
  }
};
</script>

<style lang="scss" scoped>
.timetable{
    .daySelectors{
        display: flex;
        position:fixed;
        height: 5rem;
        width: 100%;
        background-color: #1b1e20;
        justify-content: space-evenly;
    }

    .pusher{
        padding-bottom:6rem;
    }
}
</style>