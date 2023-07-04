<template>
  <div class="card">
    {{ data }}
    <MapboxMap map-id="map" style="
                        width: 100%;
                        height: 200px;
                        z-index: 1;
                        margin: 0px;
                        position: relative;
                        border-radius: 0.5rem;
                      " :options="{
                        style: 'mapbox://styles/mapbox/satellite-v9',
                        projection: 'globe', // style URL
                        center: [10.423108612635616, 35.88300600166197], // starting position [lng, lat]
                        zoom: 16 // starting zoom
                      }">
      <MapboxSource source-id="geojson" :source="{
        type: 'geojson',
        data: data
      }" />
      <MapboxLayer source-id="geojson" :layer="{

        id: 'geojson-layer',
        type: 'fill',
        paint: { 'fill-opacity': 0.5, 'fill-color': '#1fbb6d' }
      }" />
      <MapboxFullscreenControl />

    </MapboxMap>
  </div>
</template>
<script setup>
const data = ref()
data.value = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            10.423108612635616,
            35.88300600166197
          ],
          [
            10.420661004029483,
            35.882024954356424
          ],
          [
            10.420940980951798,
            35.88174280510623
          ],
          [
            10.42284121498804,
            35.8827332813017
          ],
          [
            10.422878489547145,
            35.88266605847858
          ],
          [
            10.422972873541966,
            35.88270969418522
          ],
          [
            10.423071260001251,
            35.88256263574068
          ],
          [
            10.42334353332879,
            35.882704049045415
          ],
          [
            10.423108790886403,
            35.88300607425633
          ]
        ]
      },
      "properties": {}
    }
  ]
}
</script>
