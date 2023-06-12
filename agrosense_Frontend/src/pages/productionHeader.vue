<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Production Header'
});
const auth = useCookie('token')
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/productionheader/";
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
let itemDialog = ref(false);
let deleteItemDialog = ref(false);
let deleteItemsDialog = ref(false);
let item = {
  "transaction_id": null,
  "lot_number": null,
  "produced_item": "",
  "estimated_amount": null,
  "start_date": null,
  "estimated_end_date": null,
  "surface": null,
  "current_status": "",
  "final_status": ""
};
const dt = ref(null);
let selecteditem = ref({
  "transaction_id": null,
  "lot_number": null,
  "produced_item": "",
  "estimated_amount": null,
  "start_date": null,
  "estimated_end_date": null,
  "surface": null,
  "current_status": "",
  "final_status": ""
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
    "Authorization": `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
const openNew = () => {
  console.log("ok!");
  item = {};
  //submitted.value = false;
  itemDialog.value = true;
};

const hideDialog = () => {
  itemDialog.value = false;
  submitted = false;
};
async function addItem (data) {
  console.log(data);
  const item = await useAsyncData("items", () =>
    $fetch(url, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "accept",
      },
    })
  );
  return item;
}
async function deleteItem (data) {
  const item = await useAsyncData("items", () =>
    $fetch(url + data.item_id + "/", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "accept",
      },
    })
  );
  return item;
}
async function updateItem (data) {
  console.log(data);
  const item = await useAsyncData("items", () =>
    $fetch(url + data.item_id + "/", {
      method: "PUT",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "accept",
      },
    })
  );
  return item;
}
const saveItem = () => {
  submitted = true;
  if (item.item_id) {
    updateItem(item);
    toast.add({
      severity: "success",
      summary: "Successful",
      detail: "Item Updated",
      life: 3000,
    });
  } else {
    addItem(item);
    toast.add({
      severity: "success",
      summary: "Successful",
      detail: "Item Created",
      life: 3000,
    });
  }

  itemDialog.value = false;
  item = {};
  refresh();
};

const editItem = (it) => {
  item = { ...it };

  itemDialog.value = true;
};

const confirmDeleteItem = (item) => {
  item = item;
  deleteItemDialog.value = true;
};

const exportCSV = () => {
  dt.value.exportCSV();
};

const deleteSelectedItem = () => {
  deleteItem(selecteditem._rawValue);
  selecteditem = null;
  toast.add({
    severity: "success",
    summary: "Successful",
    detail: "Item Deleted",
    life: 3000,
  });
  deleteItemsDialog.value = false;
  refresh();
};
</script>

<template>
  <div class="grid">
    <div class="col-12">
      <div>
        <Toast />
        {{ dataitems.value }}{{ error }}
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

        <DataTable ref="dt" v-model:selection="selecteditem" :value="dataitems" data-key="transaction_id"
          :paginator="true" :rows="10" :filters="filters"
          paginator-template="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rows-per-page-options="[5, 10, 25]"
          current-page-report-template="Showing {first} to {last} of {totalRecords} products" responsive-layout="scroll">
          <template #header>
            <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
              <h5 class="m-0">Productions Orders Header</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="transaction_id" header="Transaction ID"></Column>
          <Column field="lot_number" header="Lot Number"></Column>
          <Column field="produced_item" header="Produced Item"></Column>
          <Column field="estimated_amount" header="Estimated Amount"></Column>
          <Column field="start_date" header="Start Date"></Column>
          <Column field="estimated_end_date" header="Estimated End Date"></Column>
          <Column field="surface" header="Surface"></Column>
          <Column field="current_status" header="Current Status"></Column>
          <Column field="final_status" header="Final Status"></Column>
        </DataTable>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Production Order Detail" class="p-fluid"
          modal>
          <label for="transaction_id">Transaction ID:</label>
          <InputText id="transaction_id" v-model="item.transaction_id" />

          <label for="lot_number">Lot Number:</label>
          <InputText id="lot_number" v-model="item.lot_number" />

          <label for="produced_item">Produced Item:</label>
          <InputText id="produced_item" v-model="item.produced_item" />

          <label for="estimated_amount">Estimated Amount:</label>
          <InputText id="estimated_amount" v-model="item.estimated_amount" />

          <label for="start_date">Start Date:</label>
          <Calendar id="start_date" v-model="item.start_date" />

          <label for="estimated_end_date">Estimated End Date:</label>
          <Calendar id="estimated_end_date" v-model="item.estimated_end_date" />

          <label for="surface">Surface:</label>
          <InputText id="surface" v-model="item.surface" />

          <label for="current_status">Current Status:</label>
          <InputText id="current_status" v-model="item.current_status" />

          <label for="final_status">Final Status:</label>
          <InputText id="final_status" v-model="item.final_status" />
          <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog" />
            <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem" />
          </template>
        </Dialog>

        <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
          <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span v-if="item">Are you sure you want to delete
              <b>{{ selecteditem.item_description }}</b>?</span>
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
