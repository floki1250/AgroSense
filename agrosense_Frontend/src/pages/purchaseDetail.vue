<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Purchase Order Detail'
});
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/purchaseorderdetail/";
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
const orderData = ref({
  "line_no": null,
  "item_id": null,
  "quantity": null,
  "unit": "",
  "unit_cost": null,
  "order_gross_amount": null,
  "currency_mode": "",
  "foreign_amount": null,
  "status": "",
  "order_no": null
})
const dt = ref(null);
let selecteditem = ref({
  "line_no": null,
  "item_id": null,
  "quantity": null,
  "unit": "",
  "unit_cost": null,
  "order_gross_amount": null,
  "currency_mode": "",
  "foreign_amount": null,
  "status": "",
  "order_no": null
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

  selecteditem.value = {};
  //orderData.value = {}
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

  $fetch(url + data.id + "/", {
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
  if (selecteditem.value.order_no > 0) {
    updateItem(orderData.value);
  } else {
    addItem(orderData.value);
  }
  itemDialog.value = false;
  orderData.value = {};
  refresh();
};

const editItem = () => {
  orderData.value = selecteditem.value
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
  data: orders,
} = await useFetch(config.public.apiBase + "/purchaseorderheader/", {
  responseType: "json",
  transform: (orders) => {
    return orders.map(el => ({ order_no: el.order_no }))
  },
  headers: {
    "Authorization": `Token ${auth.value}`,
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
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
const unitOfMeasureOptions = ref([
  { label: "Piece", value: "piece" },
  { label: "Meter", value: "meter" },
  { label: "Kilogram", value: "kg" },
  { label: "Liter", value: "liter" },
  { label: "Box", value: "box" },
  { label: "Carton", value: "carton" },
  { label: "Gallon", value: "gallon" },
  { label: "Pound", value: "lb" },
  { label: "Ounce", value: "ounce" },
  { label: "Dozen", value: "dozen" },
  { label: "Pack", value: "pack" },
  { label: "Roll", value: "roll" },
  // Add more options as needed
]);
</script>

<template>
  <div class="grid">

    <div class="col-12">

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
            <h5 class="m-0">Purchase Order Detail</h5>
            <span class="block mt-2 md:mt-0 p-input-icon-left">
              <i class="pi pi-search" />
              <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            </span>
          </div>
        </template>

        <Column selection-mode="single" header-style="width: 3rem" />
        <Column field="order_no" header="Order No"></Column>
        <Column field="line_no" header="Line No"></Column>
        <Column field="item_id" header="Item ID"></Column>
        <Column field="quantity" header="Quantity"></Column>
        <Column field="unit" header="Unit"></Column>
        <Column field="unit_cost" header="Unit Cost"></Column>
        <Column field="order_gross_amount" header="Order Gross Amount"></Column>
        <Column field="currency_mode" header="Currency Mode"></Column>
        <Column field="foreign_amount" header="Foreign Amount"></Column>
        <Column field="status" header="Status"></Column>

      </DataTable>

      <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Order Details" class="p-fluid" modal>
        <div>

          <label for="orderNo">Order No:</label>
          <select v-model="orderData.order_no"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option v-for="el in orders" :value="el.order_no">{{ el.order_no }} </option>
          </select>

          <label for="lineNo">Line No:</label>
          <InputNumber v-model="orderData.line_no" id="lineNo" />

          <label for="itemId">Item ID:</label>
          <select v-model="orderData.item_id"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option v-for="el in itemsList" :value="el.id">{{ el.id }} | {{ el.description }} </option>
          </select>

          <label for="quantity">Quantity:</label>
          <InputNumber v-model="orderData.quantity" id="quantity" />

          <label for="unit">Unit:</label>
          <select v-model="orderData.unit"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option v-for="el in unitOfMeasureOptions" :value="el.value">{{ el.label }}</option>
          </select>

          <label for="unitCost">Unit Cost:</label>
          <InputNumber v-model="orderData.unit_cost" id="unitCost" />

          <label for="orderGrossAmount">Order Gross Amount:</label>
          <InputNumber v-model="orderData.order_gross_amount" id="orderGrossAmount" />

          <label for="currencyMode">Currency Mode:</label>
          <select v-model="orderData.currency_mode"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option value="Foreign">Foreign</option>
            <option value="Base">Base</option>
          </select>


          <label for="foreignAmount">Foreign Amount:</label>
          <InputNumber v-model="orderData.foreign_amount" id="foreignAmount" />

          <label for="status">Status:</label>

          <select v-model="orderData.status"
            class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled w-12 h-3rem p-2">
            <option value="Pending">Pending</option>
            <option value="Completed">Completed</option>
          </select>
        </div>

        <template #footer>
          <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog" />
          <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem" />
        </template>
      </Dialog>

      <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
        <div class="flex align-items-center justify-content-center">
          <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
          <span v-if="orderData">Are you sure you want to delete order number <b>{{ selecteditem.line_no }}</b> / line
            N°
            <b>{{ selecteditem.order_no }}</b>
            ?</span>
        </div>
        <template #footer>
          <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteItemsDialog = false" />
          <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedItem" />
        </template>
      </Dialog>

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
