<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Supplier Master'
});
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/suppliermaster/";
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
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
let itemDialog = ref(false);
let deleteItemDialog = ref(false);
let deleteItemsDialog = ref(false);
let supplierData = ref({
  "supplier_name": "",
  "supplier_address": "",
  "supplier_contact": "",
  "supplier_email": ""
})
const dt = ref(null);
let selecteditem = ref({
  "supplier_name": "",
  "supplier_address": "",
  "supplier_contact": "",
  "supplier_email": ""
});

let submitted = false;
const auth = useCookie('token')
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

  supplierData.value = {};
  itemDialog.value = true;
};

const hideDialog = () => {
  itemDialog.value = false;
  submitted = false;
};
async function addItem (data) {
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
async function deleteItem (data) {

  $fetch(url + data.supplier_id + "/", {
    method: "DELETE",
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
async function updateItem (data) {
  console.log(data);

  $fetch(url + data.supplier_id + "/", {
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
const saveItem = () => {

  if (supplierData.value.supplier_id) {
    updateItem(supplierData.value);
  } else {
    addItem(supplierData.value);
  }

  itemDialog.value = false;
  supplierData.value = {};
  refresh();
};

const editItem = () => {

  supplierData.value = selecteditem.value
  itemDialog.value = true;
};



const exportCSV = () => {
  dt.value.exportCSV();
};

const deleteSelectedItem = () => {
  deleteItem(selecteditem._rawValue);
  selecteditem.value = null;

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

        <DataTable ref="dt" v-model:selection="selecteditem" :value="dataitems" data-key="supplier_id" :paginator="true"
          :rows="10" :filters="filters"
          paginator-template="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rows-per-page-options="[5, 10, 25]"
          current-page-report-template="Showing {first} to {last} of {totalRecords} products" responsive-layout="scroll">
          <template #header>
            <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
              <h5 class="m-0">Suppliers</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="supplier_id" header="Id" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Id</span>
              {{ slotProps.data.supplier_id }}
            </template>
          </Column>
          <Column field="supplier_name" header="supplier name" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">supplier_name</span>
              {{ slotProps.data.supplier_name }}
            </template>
          </Column>
          <Column field="supplier_address" header="supplier address" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title"> address</span>
              {{ slotProps.data.supplier_address }}
            </template>
          </Column>
          <Column field="supplier_contact" header="contact" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">contact</span>

              {{ slotProps.data.supplier_contact }}
            </template>
          </Column>
          <Column field="supplier_email" header="Email" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Email</span>

              {{ slotProps.data.supplier_email }}
            </template>
          </Column>
        </DataTable>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Supplier Details" class="p-fluid" modal>
          <div>
            <label for="name">Name:</label>
            <InputText v-model="supplierData.supplier_name" id="name" />

            <label for="address">Address:</label>
            <InputText v-model="supplierData.supplier_address" id="address" />

            <label for="contact">Contact:</label>
            <InputText v-model="supplierData.supplier_contact" id="contact" />

            <label for="email">Email:</label>
            <InputText v-model="supplierData.supplier_email" id="email" type="email" />
          </div>

          <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog" />
            <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem" />
          </template>
        </Dialog>

        <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
          <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span v-if="selecteditem">Are you sure you want to delete user :
              <b>{{ selecteditem.supplier_name }}</b>?</span>
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
