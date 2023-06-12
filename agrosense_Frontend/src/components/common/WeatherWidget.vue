<script setup>
let flipped = ref(false)


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

    }
  }
);
</script>

<template>
  <div class="wcard-container" v-if="!error">
    <div class="wcard">
      <div class="front-content">
        <div>
          <span class="location">{{ Weather.name }}</span><br>
          <span class="temp">{{ Weather.main.temp.toFixed(0) }}&deg;</span>
        </div>

      </div>
      <div class="content">
        <span style=" text-transform: capitalize">{{ Weather.weather[0].description }}</span>
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

.wcard-container {
  position: relative;
  min-width: 20rem;
  min-height: 20rem;
  overflow: hidden;
  width: 100%;
  height: 100%;
}

.wcard {
  width: 100%;
  height: 100%;
  border-radius: inherit;
}

.wcard .front-content {
  min-width: 20rem;
  min-height: 20rem;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1);

}

.wcard .front-content span {

  font-weight: 700;
  opacity: 1;
  background: linear-gradient(-45deg, #39c98d 0%, #8af5c8 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1)
}

.wcard .content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: left;
  text-align: left;
  gap: 10px;

  background: white;
  color: #39c98d;
  padding: 20px;
  line-height: 1.5;
  border-radius: 5px;
  pointer-events: none;
  transform: translateY(96%);
  transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1);
}

.wcard .content .heading {
  font-size: 32px;
  font-weight: 700;
}

.wcard:hover .content {
  transform: translateY(0);
}

.wcard:hover .front-content {
  transform: translateY(-30%);
}

.wcard:hover .front-content p {
  opacity: 0;
}




.currentTemp {
  min-width: 220px;
  min-height: 200px;
  background: #7dddb5;
  color: #497e68;

  border-radius: 2rem;

}

.temp {

  font-size: 8em;
  text-align: center;
  display: block;
  font-weight: 300;
  color: #7dddb5;
}



.conditions {
  font-size: 80px;
  display: block;
  padding: 20px 0 0;
  text-align: center;
}




.rain {
  width: 50%;
  position: absolute;
  left: 10px;
  word-spacing: 60px;
  top: 3px;
}
</style>
