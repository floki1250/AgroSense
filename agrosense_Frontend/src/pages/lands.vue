
<script setup>
import { ref } from 'vue';
const config = useRuntimeConfig();
const url = config.public.apiBase + "/land/";
const auth = useCookie('token')

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
const selectedLand = ref(null);
</script>

<template>
  <div>

    <div class="card">
      <div class="field">
        <label for="name">Land ID : </label><br>
        <Dropdown v-model="selectedLand" :options="lands" :loading="lands ? false : true" optionLabel="land_id"
          placeholder="Select a land" class="w-full md:w-14rem" />
      </div>

    </div>
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
                <MapboxDefaultMarker marker-id="marker1" :options="{}" :lnglat="[selectedLand.lat, selectedLand.lang]">
                  <MapboxDefaultPopup popup-id="popup1" :lnglat="[selectedLand.lat, selectedLand.lang]" :options="{
                    closeOnClick: false
                  }">
                    <h1>Zitoun</h1>
                  </MapboxDefaultPopup>
                </MapboxDefaultMarker>
              </MapboxMap>
            </div>

          </ClientOnly>
        </div>
      </div>
      <div class="col-12 lg:col-4">
        <div class="card">
          <commonSensors></commonSensors>
        </div>
      </div>
    </div>
    <div v-else style="position: absolute;top:40%;left:60%">
      <commonFancyLoading></commonFancyLoading>
    </div>
  </div>
</template>
