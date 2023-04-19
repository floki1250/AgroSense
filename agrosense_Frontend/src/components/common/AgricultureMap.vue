<template>
  <div class="map-container">
    <div ref="map" class="map"></div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export default {
  name: "Map",
  setup() {
    const mapElement = ref(null);
    let map = null;

    const addGeoJsonLayer = () => {
      const geoJsonLayer = L.geoJSON({
        type: "Feature",
        properties: {
          name: "Agriculture Field",
          description: "ERP details",
        },
        geometry: {
          type: "Polygon",
          coordinates: [
            [
              [-0.1458740234375, 51.49878103585668],
              [-0.1458740234375, 51.5096757990736],
              [-0.1318359375, 51.5096757990736],
              [-0.1318359375, 51.49878103585668],
              [-0.1458740234375, 51.49878103585668],
            ],
          ],
        },
      });
      geoJsonLayer.addTo(map);
    };

    onMounted(() => {
      map = L.map(mapElement.value).setView([51.505, -0.09], 13);

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18,
      }).addTo(map);

      addGeoJsonLayer();
    });

    return {
      mapElement,
    };
  },
};
</script>

<style>
.map-container {
  position: relative;
  height: 100%;
}

.map {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
}
</style>
