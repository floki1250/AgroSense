
<script setup>

import { ref } from 'vue';
import Toast from 'primevue/toast';
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Lands'
});
const config = useRuntimeConfig();
const url = config.public.apiBase + "/land/";
const auth = useCookie('token')
const LandDialog = ref(false)
const {
  data: lands,
  pending,
  refresh,
  error
} = await useFetch(url, {
  responseType: 'json',
  headers: {
    "Authorization": `Token ${auth.value}`,
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
});
const land = ref({
  "surface": "",
  "lat": 0,
  "lang": 0
})
const selectedLand = ref(null);
async function saveLand (data) {
  console.log(data);
  $fetch(url, {
    method: "POST",
    headers: {
      "Authorization": `Token ${auth.value}`,
      'Content-Type': 'application/json',
    },
    body: data,
  })
    .then((response) => {
      Toast.add({
        severity: "success",
        summary: "Successful",
        detail: " Created",
        life: 3000,
      }); LandDialog.value = false
    })
    .catch((error) => {
      toast.add({
        severity: "error",
        summary: "Error",
        detail: "Error " + error,
        life: 3000,
      }); LandDialog.value = false
    });
}
async function deleteland () {
  console.log(selectedLand.value);
  $fetch(url + selectedLand.value.land_id, {
    method: "DELETE",
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "accept",
    },
  })
    .then((response) => console.log(response))
    .catch((error) => { console.log(error); });
}
</script>

<template>
  <div class="grid">
    {{ selectedLand }}
    <div class="col-12 lg:col-12  flex align-items-center justify-content-between card">
      <div class="my-3 ">
        <span class="p-buttonset">
          <Button label="New" icon="pi pi-plus" class="p-button-info p-button-text" @click="LandDialog = true" />
          <Button label="Delete" icon="pi pi-trash" class="p-button-danger p-button-text" @click="deleteland()" />
          <Button label="Edit" icon="pi pi-pencil" class="p-button-rounded p-button-info p-button-text mr-2" />
          <Button label="Refresh" icon="pi pi-refresh" class="p-button-warning p-button-text" @click="refresh" />
        </span>
      </div>
      <div class="my-3 ">
        <div class="field">
          <label for="name">Land ID : </label>
          <Dropdown v-model="selectedLand" :options="lands" :loading="lands ? false : true" optionLabel="land_id"
            placeholder="Select a land" class="w-full md:w-14rem" />
        </div>
      </div>

    </div>

    <div class="col-12 lg:col-12">
      <div class="grid" v-if="selectedLand">
        <div class="col-12 lg:col-8">
          <div class="card">
            <ClientOnly>
              <template #fallback>
                <div class="flex justify-content-center">
                  <ProgressSpinner />
                </div>
              </template>
              <div>
                <MapboxMap map-id="map2" style="
                        width: 100%;
                        height: 200px;
                        z-index: 1;
                        margin: 0px;
                        position: relative;
                        border-radius: 0.5rem;
                      " :options="{
                        style: 'mapbox://styles/mapbox/satellite-v9',
                        projection: 'globe', // style URL
                        center: [selectedLand.lat, selectedLand.lang], // starting position [lng, lat]
                        zoom: 16 // starting zoom
                      }">
                  <MapboxSource source-id="geojson" :source="{
                    type: 'geojson',
                    data: selectedLand.surface
                  }" />
                  <MapboxLayer source-id="geojson" :layer="{
                    source: 'geojson',
                    id: 'geojson-layer',
                    type: 'fill',
                    paint: { 'fill-opacity': 0.5, 'fill-color': '#1fbb6d' }
                  }" />
                  <MapboxFullscreenControl />

                </MapboxMap>
              </div>

            </ClientOnly>
          </div>
        </div>
        <div class="col-12 lg:col-4">
          <div class="card">
            <commonSensors :Temperature="1" :Humidity="50" :Sensor="selectedLand.sensor_id"></commonSensors>
          </div>
        </div>
      </div>
      <div v-else class="flex align-items-center justify-content-center my-6">
        <commonFancyLoading></commonFancyLoading>
      </div>
    </div>

    <Dialog v-model:visible="LandDialog" :style="{ width: '450px' }" header="Land Details" class="p-fluid" modal>
      <p>
        <Icon name="carbon:help" width="24" height="24"></Icon>
        Go to <NuxtLink to="https://geojson.io">GeoJson.io
        </NuxtLink> , copy the locations of the land and paste it in the Geojson Text Area
      </p>
      <hr>
      {{ land }}
      <div class="field">
        <label for="GeoJson">GeoJson</label>
        <Textarea id="GeoJson" v-model="land.surface" rows="5" cols="30" />
      </div>
      <template #footer>
        <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="LandDialog = false" />
        <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveLand(land)" />
      </template>
    </Dialog>
  </div>
</template>
<style>
.code {
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
  padding: 20px;
}
</style>
