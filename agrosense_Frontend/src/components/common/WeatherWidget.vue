<template>
  <div class="weatherCard">
    <div class="currentTemp">
      <span class="temp">{{ Weather.main.temp.toFixed(0) }}&deg;</span>
      <span class="location">{{ Weather.name }}</span>
    </div>
    <div class="currentWeather">
      <span class="conditions"
        ><Icon name="fluent:weather-partly-cloudy-day-48-regular"></Icon
      ></span>
      <div class="info">
        <span class="rain">{{ Weather.rain ? Weather.rain["1h"] : 0 }} MM</span>
        <span class="wind">{{ Weather.wind.speed }} m/s </span>
      </div>
    </div>
  </div>
</template>
<script setup>
const {
  data: Weather,
  pending,
  refresh,
  error,
} = await useFetch(
  "https://api.openweathermap.org/data/2.5/weather?lon=10.4231&lat=35.8832&units=metric&appid=33f13427450bfb4117c7d1b07afe6b5a",
  {
    responseType: "json",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  }
);
</script>
<style scoped>
@import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
@import url(https://cdnjs.cloudflare.com/ajax/libs/weather-icons/1.2/css/weather-icons.min.css);

.weatherCard {
  width: 400px;
  height: 200px;
  font-family: "Open Sans";
  position: relative;
}
.currentTemp {
  width: 220px;
  height: 200px;
  background: #7dddb5;
  color: #497e68;
  position: absolute;
  border-radius: 2rem;
  top: 0;
  left: 0;
}
.currentWeather {
  width: 180px;
  height: 200px;
  background: rgb(237, 237, 237);
  margin: 0;
  position: absolute;
  top: 0;
  right: 0;
  border-radius: 2rem;
}
.temp {
  font-size: 80px;
  text-align: center;
  display: block;
  font-weight: 300;
  color: rgb(255, 255, 255);
  padding: 20px 0 0;
}
.location {
  color: rgb(255, 255, 255);
  text-align: center;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 15px;
  display: block;
}
.conditions {
  font-size: 80px;
  display: block;
  padding: 20px 0 0;
  text-align: center;
}
.info {
  width: 180px;
  height: 50px;
  position: absolute;
  bottom: 0;
  right: 0;
  background: #497e68;
  font-weight: 700;
  color: rgb(255, 255, 255);
  text-align: center;
  border-radius: 2rem;
  box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px,
    rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
}
.rain {
  width: 50%;
  position: absolute;
  left: 10px;
  word-spacing: 60px;
  top: 3px;
}
.rain::before {
  display: block;
  content: "\f04e";
  font-family: weathericons;
  font-size: 40px;
  left: 6px;
  top: -4px;
  position: absolute;
}
.wind {
  width: 50%;
  right: -10px;
  position: absolute;
  word-spacing: 60px;
  top: 3px;
}
.wind::before {
  display: block;
  content: "\f050";
  font-family: weathericons;
  font-size: 25px;
  left: -10px;
  position: absolute;
  top: 5px;
}
</style>
