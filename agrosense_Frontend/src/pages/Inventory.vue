<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Inventory'
});
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/inventory/";
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
let itemDialog = ref(false);

let deleteItemsDialog = ref(false);
const item = ref({
  quantity: 0,
  unit_cost: 0,
  total_cost: 0,
  warehouse: '',
  item_type: '',
  item_measure: '',
  item_id: 0
});

const dt = ref(null);
let selecteditem = ref();
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
  selecteditem.value = {};
  item.value = {}
  itemDialog.value = true;
};

const hideDialog = () => {
  itemDialog.value = false;
  submitted = false;
};
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
async function addItem (data) {


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
      console.log("Error: " + error);
      //loading.value = false;
    });

}
async function deleteItem (data) {

  $fetch(url + data.id + "/", {
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


  $fetch(url + data.id + "/", {
    method: "PUT",
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
const saveItem = () => {
  if (selecteditem.value.item_id > 0) {

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
                  class="p-button-rounded p-button-info p-button-text mr-2" @click="editItem()" />
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
              <h5 class="m-0">Inventory</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="item_id" header="Id" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Id</span>
              {{ slotProps.data.id }}
            </template>
          </Column>
          <Column field="quantity" header="quantity" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">quantity</span>
              {{ slotProps.data.quantity }}
            </template>
          </Column>
          <Column field="unit_cost" header="unite Cost" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Unite Cost</span>
              {{ slotProps.data.unit_cost }}
            </template>
          </Column>
          <Column field="total_cost" header="Total Cost" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Total Cost</span>
              {{ slotProps.data.total_cost }}
            </template>
          </Column>
          <Column field="warehouse" header=" warehouse" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">warehouse </span>
              {{ slotProps.data.warehouse }}
            </template>
          </Column>
          <Column field="item_type" header="Type" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Type</span>
              {{ slotProps.data.item_type }}
            </template>
          </Column>
        </DataTable>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Inventory Details" class="p-fluid" modal>
          <div class="p-fluid">
            <div class="p-field">
              <label for="quantity">Quantity</label>
              <InputNumber v-model="item.quantity" id="quantity" />
            </div>

            <div class="p-field">
              <label for="unit_cost">Unit Cost</label>
              <InputNumber v-model="item.unit_cost" id="unit_cost" />
            </div>

            <div class="p-field">
              <label for="total_cost">Total Cost</label>
              <InputNumber v-model="item.total_cost" id="total_cost" />
            </div>

            <div class="p-field">
              <label for="warehouse">Warehouse</label>
              <InputText v-model="item.warehouse" id="warehouse" />
            </div>

            <div class="p-field">
              <label for="item_type">Item Type</label>
              <InputText v-model="item.item_type" id="item_type" />
            </div>

            <div class="p-field">
              <label for="item_measure">Item Measure</label>
              <InputText v-model="item.item_measure" id="item_measure" />
            </div>

            <div class="p-field">
              <label for="item_id">Item ID</label>
              <InputNumber v-model="item.item_id" id="item_id" />
            </div>
          </div>
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
