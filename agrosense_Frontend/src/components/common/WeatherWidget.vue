<script setup>
const {
  data: Weather,
  pending,
  refresh,
  error
} = await useFetch(
  'https://api.openweathermap.org/data/2.5/weather?lon=10.4231&lat=35.8832&units=metric&appid=33f13427450bfb4117c7d1b07afe6b5a',
  {
    responseType: 'json',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  }
);
</script>

<template>
  <div v-if="!error" class="grid weatherCard">
    <div class="col">
      <span class="location">{{ Weather.name }}</span>
      <span class="temp">{{ Weather.main.temp.toFixed(0) }}&deg;</span>
    </div>

    <div class="col info">
      <span style="text-transform: capitalize;">{{ Weather.weather[0].description }}</span>
      <hr>
      <div>
        <Icon name="solar:wind-bold" width="20" height="20" />
        <span>{{ Weather.wind.speed }} m/s </span>
      </div>
      <div>
        <Icon name="mdi:temperature-minus" />
        <span>{{ Weather.main.temp_min }} &deg;</span><br>
      </div>
      <div>
        <Icon name="mdi:temperature-add" />
        <span>{{ Weather.main.temp_max }}&deg; </span><br>
      </div>
      <div>
        <Icon name="mdi:barometer" />
        <span>{{ Weather.main.pressure }} mb</span><br>
      </div>
      <div>
        <Icon name="material-symbols:humidity-percentage" />
        <span>{{ Weather.main.humidity }} %</span><br>
      </div>

      <div>
        <Icon name="lucide:cloud-rain-wind" width="20" height="20" />
        <span>{{ Weather.rain ? Weather.rain["1h"] : 0 }} MM</span>
      </div>
    </div>
  </div>
  <div v-else style="margin-top: 20%;">

    <commonFancyLoading></commonFancyLoading>


  </div>
</template>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
@import url(https://cdnjs.cloudflare.com/ajax/libs/weather-icons/1.2/css/weather-icons.min.css);

span {
  padding-left: 10px;
}

.weatherCard {
  width: 400px;
  height: fit-content;
  font-family: "Open Sans";

}

.currentTemp {
  min-width: 220px;
  min-height: 200px;
  background: #7dddb5;
  color: #497e68;

  border-radius: 2rem;

}

.temp {

  font-size: 80px;
  text-align: center;
  display: block;
  font-weight: 300;
  color: #7dddb5;
}

.location {
  color: rgba(73, 75, 74, 0.5);
  text-align: left;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 1em;
  display: block;
}

.conditions {
  font-size: 80px;
  display: block;
  padding: 20px 0 0;
  text-align: center;
}

.info {
  background: #75c7a5;
  font-weight: 700;
  color: rgb(255, 255, 255);
  text-align: left;
  border-radius: 2rem;
  padding: 10px;
  box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px,
    rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
  display: block;
}

.rain {
  width: 50%;
  position: absolute;
  left: 10px;
  word-spacing: 60px;
  top: 3px;
}
</style>
