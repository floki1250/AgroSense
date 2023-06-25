<template>
  <div class="flex align-items-center justify-content-center h-full time">

    <h1>It's {{ letterTime }}</h1>

  </div>
</template>



<script>
import { ref, onMounted } from 'vue';

export default {
  setup () {
    const letterTime = ref('');

    const updateTime = () => {
      const now = new Date();
      const hours = now.getHours();
      const minutes = now.getMinutes();
      letterTime.value = convertToLetterTime(hours, minutes);
    };

    const convertToLetterTime = (hours, minutes) => {
      const hourWords = [
        '', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve'
      ];

      const minuteWords = [
        '', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
        'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five',
        'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'half'
      ];

      let hour = hours % 12;
      if (hour === 0) {
        hour = 12;
      }

      let minute;
      let connector;
      if (minutes === 0) {
        minute = 'O\'clock';
      } else if (minutes <= 30) {
        minute = minuteWords[minutes];
        connector = 'past';
      } else {
        minute = minuteWords[60 - minutes];
        connector = 'to';
        hour = (hour % 12) + 1;
      }

      if (minutes === 15) {
        minute = 'quarter';
      } else if (minutes === 30) {
        minute = 'half';
        connector = 'past';
      }

      return `${minute} ${connector} ${hourWords[hour]}`;
    };

    onMounted(() => {
      updateTime();
      setInterval(updateTime, 1000);
    });

    return {
      letterTime
    };
  }
};
</script>



<style>
h1 {
  text-transform: capitalize;
  font-size: 2em;
  font-weight: bold;
}

.time {
  background: linear-gradient(-45deg, #a6ffd7 0%, #b6ffe0 100%);
  padding: 10px;
  border-radius: 2rem;
  color: white;
  height: 100%;

}
</style>
