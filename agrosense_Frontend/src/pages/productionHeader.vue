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
let deleteItemsDialog = ref(false);
const item = ref({
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
  selecteditem.value = {};
  //item.value = {}
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
async function deleteItem (data) {

  $fetch(url + data.transaction_id + "/", {
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
async function updateItem (data) {


  $fetch(url + data.transaction_id + "/", {
    method: "PUT",
    body: JSON.stringify(data),
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
  item.value = selecteditem.value
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
const total_cost = ref(0)
async function calculate () {
  const url = config.public.apiBase + "/productiondetail/";
  const {
    data: transaction
  } = await useFetch(url, {
    responseType: "json",
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    transform: (transaction) => {
      return transaction.filter(el => el.transaction_id == selecteditem.value.transaction_id);
    }
  });
  transaction.value = transaction.value.map(el => Object.values({ cost: parseFloat(el.real_amount) }))
  const totalarray = transaction._rawValue.flat()
  let total = 0;
  total = totalarray.reduce((a, b) => a + b, 0)
  total_cost.value = total
}
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
                <Button label="Calculate" icon="pi pi-calculator" class=" p-button-text" @click="calculate()" />
              </span>
            </div>
          </template>

          <template #end>
            <FileUpload mode="basic" accept="text/*" :max-file-size="1000000" label="Import" choose-label="Import"
              class="mr-2 inline-block p-button-text" />
            <Button label="Export" icon="pi pi-upload" class="p-button-help p-button-text" @click="exportCSV"></Button>
          </template>
        </Toolbar>
        <Message severity="success" sticky v-if="total_cost">Total Production Cost : <b>{{ total_cost }}</b></Message>
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

          <input type="date" class="p-inputtext p-component" v-model="item.start_date" id="start_date"
            dateFormat="yy-mm-dd" />
          <label for="estimated_end_date">Estimated End Date:</label>

          <input type="date" class="p-inputtext p-component" v-model="item.estimated_end_date" id="estimated_end_date"
            dateFormat="yy-mm-dd" />
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


