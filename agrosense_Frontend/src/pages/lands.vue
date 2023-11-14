
<script setup>

import { ref } from 'vue';
import { useToast } from "primevue/usetoast";
const toast = useToast();
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Lands'
});
let deleteItemsDialog = ref(false);

const healthCheck = computed(() => {
  return (Leaf.value.find(el => el.label === 'Normal')).score > 0.7 ? 'green' : 'orange'
})


const showError = () => {
  toast.add({
    severity: "error",
    summary: "Error",
    detail: "Error",
    life: 3000,
  });
};
const showSuccess = () => {
  toast.add({
    severity: "success",
    summary: "Successful",
    detail: "Request Successful",
    life: 3000,
  });
};
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
  "sensor_id": 0,
  "surface": "",
  "lat": 0,
  "lang": 0
})
const selectedLand = ref(null);

const selectedImage = ref(null);
const onImageSelect = (event) => {
  const file = event.target.files[0];
  selectedImage.value = file;
};
const Leaf = ref(null)
const uploadImage = async () => {
  Leaf.value = null
  const file = selectedImage.value;

  const endpoint = "https://api-inference.huggingface.co/models/OttoYu/LeafCondition"
  $fetch(endpoint, {
    method: "POST",
    responseType: "json",
    headers: {
     
      'Content-Type': 'application/octet-stream'

    },
    body: file,
  })
    .then((response) => { console.log(response); Leaf.value = response })

    .catch((error) => {
      console.log("Error: " + error);
    });

};
const openNew = () => {

  land.value = {};
  LandDialog.value = true;
};
async function addLand (data) {
  console.log(data);

  $fetch(url, {
    method: "POST",
    body: data,
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "accept",
    },
  }).then((response) => {
    showSuccess();
  })
    .catch((error) => {
      showError();

      //loading.value = false;
    });

}
async function updateLand (data) {
  console.log(data);

  $fetch(url + data.land_id + "/", {
    method: "PUT",
    body: JSON.stringify(data),
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "accept",
    },
  }).then((response) => {
    showSuccess();
  })
    .catch((error) => {
      showError();

      //loading.value = false;
    });

}
const saveLand = () => {

  if (land.value.land_id) {
    updateLand(land.value);
  } else {
    addLand(land.value);
  }
  LandDialog.value = false;
  land.value = {};
  refresh();
};

async function deleteland (data) {
  console.log(data);
  $fetch(url + data.land_id, {
    method: "DELETE",
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "accept",
    },
  })
    .then((response) => {
      showSuccess();
    })
    .catch((error) => {
      showError();

      //loading.value = false;
    });
}
const editLand = () => {
  land.value = selectedLand.value
  LandDialog.value = true;
};
const deleteSelectedLand = () => {
  deleteland(selectedLand.value);
  selectedLand.value = null;

  deleteItemsDialog.value = false;
  refresh();
};
</script>

<template>
  <div class="grid">

    <div class="col-12 lg:col-12  flex align-items-center justify-content-between card">
      <Toast />
      <div class="my-3 ">
        <span class="p-buttonset">
          <Button label="New" icon="pi pi-plus" class="p-button-info p-button-text" @click="openNew" />
          <Button label="Delete" icon="pi pi-trash" class="p-button-danger p-button-text"
            @click="deleteItemsDialog = true" />
          <Button label=" Edit" icon="pi pi-pencil" class="p-button-rounded p-button-info p-button-text mr-2"
            @click="editLand" />
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



    <div class="col-12 lg:col-4">
      <commonSensors></commonSensors>
    </div>
    <div class="col-12 lg:col-8 card" v-if="selectedLand">

      <MapboxMap :key="selectedLand.land_id" map-id="map2" style="
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


    <div class="col-12 lg:col-12  flex align-items-center justify-content-around grid card">
      <div class="p-3 m-1 ">
        <div>
          <input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg" ref="file" @change="onImageSelect"
            class="p-button p-button-info p-button-text">
        </div>
        <Button @click="uploadImage" class="p-button-info p-button-text">
          <Icon name="solar:leaf-bold" width="24px" height="24px"></Icon>
          <span><b>AI</b> Check Leaf Health</span>
        </Button>
      </div>

      <div class="p-3 ">
        <div v-if="!Leaf">
          <commonFancyLoading></commonFancyLoading>
        </div>
        <div v-else class="card p-5">
          <Icon name="ri:leaf-fill" width="50px" height="50px" :color="healthCheck" />
          <div v-for="el in Leaf">
            <b>{{ el.label }} : {{ Math.round(el.score * 1000) / 10 }} % </b>
          </div>
        </div>
      </div>
    </div>

    <Dialog v-model:visible="LandDialog" :style="{ width: '450px' }" header="Land Details" class="p-fluid" modal>
      <p>
        <Icon name="carbon:help" width="24" height="24"></Icon>
        Go to <NuxtLink to="https://geojson.io">GeoJson.io
        </NuxtLink> , copy the locations of the land and paste it in the Geojson Text Area
      </p>
      <hr>

      <div class="field">
        <label for="sensor_id">Sensor id:</label>
        <InputNumber v-model="land.sensor_id" id="sensor_id" />
        <label for="GeoJson">GeoJson</label>
        <Textarea id="GeoJson" v-model="land.surface" rows="5" cols="30" />

        <label for="lat">lat:</label>
        <InputText v-model="land.lat" id="lat" />

        <label for="lang">lang:</label>
        <InputText v-model="land.lang" id="email" type="lang" />
      </div>
      <template #footer>
        <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="LandDialog = false" />
        <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveLand(land)" />
      </template>
    </Dialog>
    <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
      <div class="flex align-items-center justify-content-center">
        <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
        <span v-if="selectedLand">Are you sure you want to delete land :
          <b>{{ selectedLand.land_id }}</b>?</span>
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteItemsDialog = false" />
        <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedLand" />
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
