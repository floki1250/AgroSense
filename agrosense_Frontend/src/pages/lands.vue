
<script setup>
import { ref } from 'vue';
const config = useRuntimeConfig();
const url = config.public.apiBase + "/land/";
const {
  data: lands,
  pending,
  refresh,
  error
} = await useFetch(url, {
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
});
const selectedLand = ref(null);
</script>

<template>
  <div v-if="!pending">
    {{ selectedLand }}
    <div class="card">
      <Dropdown v-model="selectedLand" :options="lands" optionLabel="land_id" placeholder="Select a land"
        class="w-full md:w-14rem" />
    </div>
    <div class="col-fixed" style="width: 50%">
      <div class="card">
        <ClientOnly>
          <template #fallback>
            <div class="flex justify-content-center">
              <ProgressSpinner />
            </div>
          </template>
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
        </ClientOnly>
      </div>
    </div>
  </div>
  <div v-else>
    {{ error }}
    <ProgressSpinner />
  </div>
</template>
