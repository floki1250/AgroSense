<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: ["auth"],
});
useHead({
  title: "Agrosense | Production Details",
});
const auth = useCookie("token");
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/productiondetail/";
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
let itemDialog = ref(false);
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
    detail: "Item Created",
    life: 3000,
  });
};
let deleteItemsDialog = ref(false);
const item = ref({
  lineno: null,
  lot_number: null,
  item_id: null,
  estimated_quantity: null,
  real_quantity: null,
  estimated_amount: null,
  real_amount: null,
  start_date: null,
  end_date: null,
  transaction_id: null,
});
const dt = ref(null);
let selecteditem = ref({
  lineno: null,
  lot_number: null,
  item_id: null,
  estimated_quantity: null,
  real_quantity: null,
  estimated_amount: null,
  real_amount: null,
  start_date: null,
  end_date: null,
  transaction_id: null,
});

let submitted = false;
const {
  data: dataitems,
  pending,
  refresh,
  error,
} = await useFetch(url, {
  responseType: "json",
  headers: {
    Authorization: `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
const openNew = () => {
  selecteditem.value = {};
  item.value = {}
  itemDialog.value = true;
};

const hideDialog = () => {
  itemDialog.value = false;
  submitted = false;
};
async function addItem (data) {


  $fetch(url, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      Authorization: `Token ${auth.value}`,
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
async function deleteItem (data) {
  $fetch(url + data.id + "/", {
    method: "DELETE",
    headers: {
      Authorization: `Token ${auth.value}`,
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
async function updateItem (data) {


  $fetch(url + data.id + "/", {
    method: "PUT",
    body: JSON.stringify(data),
    headers: {
      Authorization: `Token ${auth.value}`,
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
const saveItem = () => {
  if (selecteditem.value.transaction_id > 0) {
    updateItem(item.value);
  } else {
    addItem(item.value);
  }

  itemDialog.value = false;
  item.value = {};
  refresh();
};

const editItem = () => {
  item.value = selecteditem.value;
  itemDialog.value = true;
};

const exportCSV = () => {
  dt.value.exportCSV();
};

const deleteSelectedItem = () => {
  deleteItem(selecteditem.value);
  selecteditem.value = {};

  deleteItemsDialog.value = false;
  refresh();
};
const {
  data: itemsList,
} = await useFetch(config.public.apiBase + "/inventory/", {
  responseType: "json",
  transform: (itemsList) => {
    return itemsList.map(el => ({ id: el.item_id, description: el.description }))
  },
  headers: {
    "Authorization": `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
const {
  data: transactionsList,
} = await useFetch(config.public.apiBase + "/productionheader/", {
  responseType: "json",
  transform: (transactionsList) => {
    return transactionsList.map(el => ({ id: el.transaction_id }))
  },
  headers: {
    "Authorization": `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
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
                <Button label="Delete" icon="pi pi-trash" class="p-button-danger p-button-text" :disabled="!selecteditem"
                  @click="deleteItemsDialog = true" />
                <Button label="Edit" icon="pi pi-pencil" :disabled="!selecteditem"
                  class="p-button-rounded p-button-info p-button-text mr-2" @click="editItem(selecteditem)" />
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

        <DataTable ref="dt" v-model:selection="selecteditem" :value="dataitems" data-key="id" :paginator="true" :rows="10"
          :filters="filters"
          paginator-template="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rows-per-page-options="[5, 10, 25]"
          current-page-report-template="Showing {first} to {last} of {totalRecords} products" responsive-layout="scroll">
          <template #header>
            <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
              <h5 class="m-0">Productions Orders Details</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="transaction_id" header="Transaction ID"></Column>
          <Column field="lineno" header="Line Number"></Column>
          <Column field="lot_number" header="Lot Number"></Column>
          <Column field="item_id" header="Produced Item"></Column>
          <Column field="estimated_quantity" header="Estimated quantity"></Column>
          <Column field="real_quantity" header="Real quantity"></Column>
          <Column field="estimated_amount" header="Estimated Amount"></Column>
          <Column field="real_amount" header="Real Amount"></Column>
          <Column field="start_date" header="Start Date"></Column>
          <Column field="end_date" header="End Date"></Column>
        </DataTable>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Production Order Detail" class="p-fluid"
          modal>

          <label for="transaction_id">Transaction ID:</label>

          <select v-model="item.transaction_id"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option v-for="el in transactionsList" :value="el.id">{{ el.id }} </option>
          </select>

          <label for="lineno">line Number:</label>
          <InputText id="lineno" v-model="item.lineno" />

          <label for="lot_number">Lot Number:</label>
          <InputText id="lot_number" v-model="item.lot_number" />

          <label for="item_id"> Item Id :</label>

          <select v-model="item.item_id"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option v-for="el in itemsList" :value="el.id">{{ el.id }} | {{ el.description }} </option>
          </select>

          <label for="estimated_quantity">Estimated Quantity:</label>
          <InputText id="estimated_quantity" v-model="item.estimated_quantity" />

          <label for="real_quantity">Real Quantity:</label>
          <InputText id="real_quantity" v-model="item.real_quantity" />
          <label for="estimated_amount">Estimated Amount:</label>
          <InputText id="estimated_amount" v-model="item.estimated_amount" />
          <label for="real_amount">Real Amount:</label>
          <InputText id="real_amount" v-model="item.real_amount" />

          <label for="start_date">Start Date:</label>

          <input type="date" class="p-inputtext p-component" v-model="item.start_date" id="start_date"
            dateFormat="yy-mm-dd" />
          <label for="end_date"> End Date:</label>

          <input type="date" class="p-inputtext p-component" v-model="item.end_date" id="end_date"
            dateFormat="yy-mm-dd" />
          <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog" />
            <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem" />
          </template>
        </Dialog>

        <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
          <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span v-if="item">Are you sure you want to delete transaction Number
              <b>{{ selecteditem.transaction_id }}</b> ?</span>
          </div>
          <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteItemsDialog = false" />
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedItem" />
          </template>
        </Dialog>
      </div>
    </div>
  </div>
</template>
