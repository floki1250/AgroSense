<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Stock Transactions'
});
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/stocktransactions/";
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const auth = useCookie('token')
let itemDialog = ref(false);
let deleteItemDialog = ref(false);
let deleteItemsDialog = ref(false);
let transactionData = ref({
  "item_id": null,
  "transaction_type": "",
  "quantity": null,
  "cost": null,
  "transaction": null,
  "user_id": null,
  "rmk": ""
});
const {
  data: itemsList,
} = await useFetch(config.public.apiBase + "/items/", {
  responseType: "json",
  transform: (itemsList) => {
    return itemsList.map(el => ({ id: el.item_id, description: el.item_description }))
  },
  headers: {
    "Authorization": `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
const dt = ref(null);
let selecteditem = ref({
  "item_id": null,
  "transaction_type": "",
  "quantity": null,
  "cost": null,
  "transaction": null,
  "user_id": null,
  "rmk": ""
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
const openNew = () => {

  transactionData.value = {};
  //submitted.value = false;
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
    });

}
async function deleteItem (data) {
  console.log(data)
  $fetch(url + data.transaction_id + "/", {
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
    });

}
async function updateItem (data) {
  console.log(data);

  $fetch(url + data.transaction_id + "/", {
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
    });

}
const saveItem = () => {
  if (selecteditem.value.item_id > 0) {

    updateItem(transactionData.value);

  } else {

    addItem(transactionData.value);

  }

  itemDialog.value = false;
  transactionData.value = {};
  refresh();
};

const editItem = () => {
  transactionData = selecteditem.value
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

        <DataTable ref="dt" v-model:selection="selecteditem" :value="dataitems" data-key="item_id" :paginator="true"
          :rows="10" :filters="filters"
          paginator-template="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rows-per-page-options="[5, 10, 25]"
          current-page-report-template="Showing {first} to {last} of {totalRecords} products" responsive-layout="scroll">
          <template #header>
            <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
              <h5 class="m-0">Stock Transactions</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="transaction_id" header="Id" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Id</span>
              {{ slotProps.data.transaction_id }}
            </template>
          </Column>
          <Column field="transaction_type" header="transaction_type" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">transaction_type</span>
              {{ slotProps.data.transaction_type }}
            </template>
          </Column>
          <Column field="quantity" header="quantity" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">quantity</span>
              {{ slotProps.data.quantity }}
            </template>
          </Column>
          <Column field="cost" header="cost" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">cost</span>
              {{ slotProps.data.cost }}
            </template>
          </Column>
          <Column field="transaction" header="transaction" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Date transaction</span>
              {{ slotProps.data.transaction }}
            </template>
          </Column>
          <Column field="created" header="created" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Date created</span>
              {{ slotProps.data.created }}
            </template>
          </Column>
          <Column field="modified" header="modified" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Date modified</span>
              {{ slotProps.data.modified }}
            </template>
          </Column>
          <Column field="user_id" header="User" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">User</span>

              {{ slotProps.data.user_id }}
            </template>
          </Column>
          <Column field="rmk" header="Remark" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Remark</span>

              {{ slotProps.data.rmk }}
            </template>
          </Column>
        </DataTable>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Transaction Details" class="p-fluid"
          modal>
          <div>
            <label for="itemId">Item ID:</label>

            <select v-model="transactionData.item_id"
              class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
              <option v-for="el in itemsList" :value="el.id">{{ el.id }} | {{ el.description }} </option>
            </select>

            <label for="transactionType">Transaction Type:</label>

            <select v-model="transactionData.transaction_type"
              class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
              <option value="Sale">Sale</option>
              <option value="Purchase">Purchase</option>
            </select>

            <label for="quantity">Quantity:</label>
            <InputNumber v-model="transactionData.quantity" id="quantity" />

            <label for="cost">Cost:</label>
            <InputNumber v-model="transactionData.cost" id="cost" />

            <label for="transaction">Transaction:</label>

            <input type="date" class="p-inputtext p-component" v-model="transactionData.transaction" id="transaction"
              dateFormat="yy-mm-dd" />

            <label for="userId">User ID:</label>
            <InputNumber v-model="transactionData.user_id" id="userId" />

            <label for="remarks">Remarks:</label>
            <InputText v-model="transactionData.rmk" id="remarks" />
          </div>
          <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog" />
            <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem" />
          </template>
        </Dialog>

        <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
          <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span v-if="transactionData">Are you sure you want to delete transaction id :
              <b>{{ selecteditem.transaction_id }}</b>?</span>
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
