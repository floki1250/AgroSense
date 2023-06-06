<template>
  <div>
    <div>
      <Icon name="mingcute:radar-line" width="20" height="20"></Icon>
      Sensor ID : {{ Sensor }}
    </div><br>
    <div>
      <Icon name="tabler:temperature" width="20" height="20"></Icon>
      Temperature : <span>{{ Temperature }}°</span>
    </div><br>
    <div>
      <Icon name="material-symbols:humidity-percentage" width="20" height="20" /> Humidity : {{ Humidity }} %
    </div><br>
    <div>
      <Icon name="material-symbols:water-ph-outline-sharp" width="20" height="20"></Icon>
      Ph : <b class="text-red-500">Sensor Not Available </b>
    </div><br>
    <div>
      <Icon name="mdi:robot-outline" width="20" height="20"></Icon><b>AI</b> Water
      Needed : 0
    </div>
  </div>
</template>
<script setup>
const props = defineProps({
  Humidity: Number,
  Temperature: Number,
  Sensor: Number
});
</script>
