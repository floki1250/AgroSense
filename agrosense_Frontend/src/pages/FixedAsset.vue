<script setup>
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Immobilisation'
});

const imageFile = ref(null);
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/immo/";
let itemDialog = ref(false);
let deleteItemDialog = ref(false);


const item = ref({
  "serial_number": "",
  "description": "",
  "date_of_commissioning": null,
  "cost_account": null,
  "depreciation_period": null,
  "amount_per_hour": null,
  "usage": 0,
  "image": null
});
const showError = () => {
  toast.add({ severity: 'error', summary: 'Error', detail: "Error", life: 3000 });
};
const showSuccess = () => {
  toast.add({
    severity: "success",
    summary: "Successful",
    detail: "Item Created",
    life: 3000,
  });
};
const show_details = ref(false);
let selecteditem = ref({
  "serial_number": "",
  "description": "",
  "date_of_commissioning": null,
  "cost_account": null,
  "depreciation_period": null,
  "amount_per_hour": null,
  "usage": null,
  "image": null
});
const auth = useCookie('token')
let submitted = false;
const {
  data: dataitems,
  pending,
  refresh,
  error,
} = await useFetch(url, {
  responseType: "json",
  headers: {
    "Authorization": `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
const openNew = () => {
  selecteditem.value = {}
  show_details.value = true;
  itemDialog.value = true;
  item.value = {}
};

const hideDialog = () => {
  itemDialog.value = false;
  submitted = false;
};

function handleFileUpload (event) {
  imageFile.value = event.target.files[0];
}
async function addItem (formData) {

  const formDataObj = new FormData();
  formDataObj.append('serial_number', formData.serial_number);
  formDataObj.append('description', formData.description);
  formDataObj.append('date_of_commissioning', formData.date_of_commissioning);
  formDataObj.append('cost_account', formData.cost_account);
  formDataObj.append('depreciation_period', formData.depreciation_period);
  formDataObj.append('amount_per_hour', 0);
  formDataObj.append('image', imageFile.value);
  formDataObj.append('usage', 0);

  $fetch(url, {
    method: "POST",
    body: formDataObj,
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "accept",
    },
  })
    .then((response) => {
      showSuccess();
    })
    .catch((error) => {
      showError();
      console.log("Error: " + error);
      //loading.value = false;
    });
}
async function deleteItem (data) {

  $fetch(url + data.idimmo + "/", {
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
      console.log("Error: " + error);
      //loading.value = false;
    });
}
async function updateItem (formData) {
  console.log(formData)
  const formDataObj = new FormData();
  formDataObj.append('serial_number', formData.serial_number);
  formDataObj.append('description', formData.description);
  formDataObj.append('date_of_commissioning', formData.date_of_commissioning);
  formDataObj.append('cost_account', formData.cost_account);
  formDataObj.append('depreciation_period', formData.depreciation_period);
  formDataObj.append('amount_per_hour', 0);
  formDataObj.append('image', imageFile.value);
  formDataObj.append('usage', formData.usage);

  $fetch(url + formData.idimmo + "/", {
    method: "PUT",
    body: formData,
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "accept",
    },
  })
    .then((response) => {
      showSuccess();
    })
    .catch((error) => {
      showError();
    });
}
const saveItem = () => {

  if (selecteditem.value.idimmo > 0) {

    updateItem(item.value);

  } else {

    addItem(item.value);

  }

  itemDialog.value = false;
  item.value = {};
  refresh();
};



const editItem = (el) => {
  show_details.value = true;
  selecteditem.value = el
  item.value = el
  itemDialog.value = true;

};
const details = () => {
  item.value = selecteditem.value
  itemDialog.value = true;
  show_details.value = false;
};
const confirmDeleteItem = (el) => {
  selecteditem.value = el;
  deleteItemDialog.value = true;
};
function exportToCSV (dataObj, filename) {
  const csvContent = "";
  const blob = new Blob([csvContent], { type: "text/csv" });
  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", filename);
  link.click();
}

const exportCSV = () => {
  const dt = dataitems._rawValue;
  console.log(typeof dt, dt);
  //dt.exportCSV();
  exportToCSV(dt, "Immobilization.csv");
};

const deleteSelectedItem = () => {
  deleteItem(selecteditem.value);
  deleteItemDialog.value = false;
  selecteditem.value = {};
  refresh();
};
</script>

<template>
  <div class="grid">


    <div class="col-12">
      <div>
        <Toast />
        <Toolbar class="mb-4">
          <template #start>
            <div class="my-3">
              <span class="p-buttonset">
                <Button label="New" icon="pi pi-plus" class="p-button-info p-button-text" @click="openNew" />

                <Button label="Refresh" icon="pi pi-refresh" class="p-button-warning p-button-text" @click="refresh" />
              </span>
            </div>
          </template>

          <template #end>
            <FileUpload mode="basic" accept="text/*" :max-file-size="1000000" label="Import" choose-label="Import"
              class="mr-2 inline-block p-button-text" />
            <Button label="Export" icon="pi pi-upload" class="p-button-help p-button-text" @click="exportCSV"></Button>
          </template>
        </Toolbar>
        <div class="grid">
          <div v-for="el in dataitems" class="col">
            <commonCard :id="el.idimmo" :usage="el.usage" :title="el.serial_number" @delete="confirmDeleteItem(el)"
              @edit="editItem(el)" @details="details(el)" :img="el.image" :description="el.description" />
          </div>
        </div>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Fixed Asset Details" class="p-fluid"
          modal>
          <input type="file" ref="fileInput" @change="handleFileUpload">


          <div v-if="item.idimmo > 0" class="flex align-items-center justify-content-center p-2">
            <img :src="item.image" alt=""
              style="width: 200px;height:150px;border-radius: 1rem;border:5px solid whitesmoke" />
          </div>

          <div class="field">
            <label for="idimmo">FixedAsset Id</label>
            <InputText id="idimmo" v-model.trim="item.idimmo" required="true" autofocus disabled />
            <small v-if="submitted && !item.idimmo" class="p-invalid">idimmo is required.</small>
          </div>
          <div class="field">
            <label for="serial_number">serial number </label>
            <InputText id="serial_number" v-model.trim="item.serial_number" required="true" autofocus
              :disabled="!show_details" />

          </div>
          <div class="field">
            <label for="description">description</label>
            <InputText id="description" v-model.trim="item.description" :disabled="!show_details" />

          </div>
          <div class="field">
            <label for="date_of_commissioning">Date of Commissioning</label>
            <input type="date" v-model="item.date_of_commissioning" class="p-inputtext p-component"
              :disabled="!show_details" />
          </div>
          <div class="field">
            <label for="cost_account">Cost Account</label>
            <input type="number" class="p-inputtext p-component" id="cost_account" v-model.number="item.cost_account"
              placeholder="Cost Account TND" :disabled="!show_details">

          </div>
          <div class="field">
            <label for="depreciation_period">Depreciation Period </label>

            <input type="number" class="p-inputtext p-component" id="depreciation_period"
              v-model="item.depreciation_period" placeholder="Depreciation Period" :disabled="!show_details">
          </div>
          <div class="field">
            <label for="usage">usage </label>

            <input type="number" class="p-inputtext p-component" id="usage" v-model="item.usage" placeholder="usage"
              :disabled="!show_details">
          </div>

          <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog"
              v-show="show_details" />
            <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem" v-show="show_details" />
          </template>
        </Dialog>

        <Dialog v-model:visible="deleteItemDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
          <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span v-if="item">Are you sure you want to delete
              <b>{{ selecteditem.idimmo }} : {{ selecteditem.description }} </b> ?</span>
          </div>
          <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteItemDialog = false" />
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedItem" />
          </template>
        </Dialog>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.product-badge {
  border-radius: 2px;
  padding: 0.25em 0.5rem;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 12px;
  letter-spacing: 0.3px;

  &.status-instock {
    background: #c8e6c9;
    color: #256029;
  }

  &.status-outofstock {
    background: #ffcdd2;
    color: #c63737;
  }

  &.status-lowstock {
    background: #feedaf;
    color: #8a5340;
  }
}
</style>
