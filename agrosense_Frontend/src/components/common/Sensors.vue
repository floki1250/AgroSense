<template>
  <div class="relative card" v-if="data">

    <div>
      <Icon name="mingcute:radar-line" width="20" height="20"></Icon>
      Sensor ID : 1
    </div><br>
    <div>
      <Icon name="tabler:plant-2" width="20" height="20"></Icon>
      Category : 1
    </div><br>
    <div>
      <Icon name="tabler:temperature" width="20" height="20"></Icon>
      Temperature : <span>{{ data.find(item => item.id
        === "TEMPERATURE").$value }}°</span>
    </div><br>
    <div>
      <Icon name="material-symbols:humidity-percentage" width="20" height="20" /> Humidity : {{ data.find(item => item.id
        === "HUMIDITY").$value }} %
    </div><br>
    <div>
      <Icon name="material-symbols:water-ph-outline-sharp" width="20" height="20"></Icon>
      Ph : <b class="text-red-500">Sensor Not Available </b>
    </div><br>
    <div>
      <Icon name="ic:outline-water-drop" width="20" height="20"></Icon>
      <b>AI</b> Water Recommended : {{ Water }} mm/day
    </div>
    <Button icon="pi pi-sync" @click="runAi()" class="p-button-text absolute top-0 right-0" :loading="loading" />

  </div>
</template>
<script setup>
import { useDatabaseList, useDatabase } from 'vuefire'
import { ref as dbRef } from 'firebase/database'

const Water = ref(0)
const loading = ref(false)
const db = useDatabase()
const data = useDatabaseList(dbRef(db, 'ESP32_APP'))
const config = useRuntimeConfig();
const url = config.public.apiBase + "/recommend_water/";
const auth = useCookie('token')
function runAi () {
  const humidity = data.value.find(item => item.id === "HUMIDITY").$value
  const temperature = data.value.find(item => item.id === "TEMPERATURE").$value

  console.log(humidity, temperature)
  loading.value = true
  let conditions_data = new URLSearchParams();
  conditions_data.append("temperature", temperature);
  conditions_data.append("humidity", humidity);
  conditions_data.append("category", 1);
  console.log("running")
  $fetch(url, {
    method: "POST",
    responseType: "json",
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/x-www-form-urlencoded",
      'Access-Control-Allow-Origin': '*'
    },
    body: conditions_data,
  })
    .then((response) => {

      console.log(response)
      Water.value = response.water.toFixed(2);
      loading.value = false;

    })
    .catch((error) => {

      console.log("Error: " + error);
      loading.value = false;
    });
}
</script>
