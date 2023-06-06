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
let deleteItemDialog = ref(false);
let deleteItemsDialog = ref(false);
let orderData = {
  "order_type": "",
  "company": null,
  "line_no": null,
  "item_id": null,
  "supplier_id": null,
  "requested_date": null,
  "date_received": null,
  "order_date": null,
  "scheduled_pick_date": null,
  "actual_ship_date": null,
  "cancel_date": null,
  "promised_shipment_date": null,
  "remark": "",
  "quantity": null,
  "unit": "",
  "unit_cost": null,
  "order_gross_amount": null,
  "currency_mode": "",
  "foreign_amount": null,
  "status": "",
  "order_no": null
}
const dt = ref(null);
let selecteditem = ref({
  "order_type": "",
  "company": null,
  "line_no": null,
  "item_id": null,
  "supplier_id": null,
  "requested_date": null,
  "date_received": null,
  "order_date": null,
  "scheduled_pick_date": null,
  "actual_ship_date": null,
  "cancel_date": null,
  "promised_shipment_date": null,
  "remark": "",
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
  orderData = selecteditem.value

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
              <h5 class="m-0">Items</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="order_no" header="Order No"></Column>
          <Column field="order_type" header="Order Type"></Column>
          <Column field="company" header="Company"></Column>
          <Column field="line_no" header="Line No"></Column>
          <Column field="item_id" header="Item ID"></Column>
          <Column field="supplier_id" header="Supplier ID"></Column>
          <Column field="requested_date" header="Requested Date"></Column>
          <Column field="date_received" header="Date Received"></Column>
          <Column field="order_date" header="Order Date"></Column>
          <Column field="scheduled_pick_date" header="Scheduled Pick Date"></Column>
          <Column field="actual_ship_date" header="Actual Ship Date"></Column>
          <Column field="cancel_date" header="Cancel Date"></Column>
          <Column field="promised_shipment_date" header="Promised Shipment Date"></Column>
          <Column field="remark" header="Remark"></Column>
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
            <InputText v-model="orderData.order_no" id="orderNo" />

            <label for="orderType">Order Type:</label>
            <InputText v-model="orderData.order_type" id="orderType" />

            <label for="company">Company:</label>
            <InputText v-model="orderData.company" id="company" />

            <label for="lineNo">Line No:</label>
            <InputText v-model="orderData.line_no" id="lineNo" />

            <label for="itemId">Item ID:</label>
            <InputText v-model="orderData.item_id" id="itemId" />

            <label for="supplierId">Supplier ID:</label>
            <InputText v-model="orderData.supplier_id" id="supplierId" />

            <label for="requestedDate">Requested Date:</label>
            <Calendar v-model="orderData.requested_date" id="requestedDate" />

            <label for="dateReceived">Date Received:</label>
            <Calendar v-model="orderData.date_received" id="dateReceived" />

            <label for="orderDate">Order Date:</label>
            <Calendar v-model="orderData.order_date" id="orderDate" />

            <label for="scheduledPickDate">Scheduled Pick Date:</label>
            <Calendar v-model="orderData.scheduled_pick_date" id="scheduledPickDate" />

            <label for="actualShipDate">Actual Ship Date:</label>
            <Calendar v-model="orderData.actual_ship_date" id="actualShipDate" />

            <label for="cancelDate">Cancel Date:</label>
            <Calendar v-model="orderData.cancel_date" id="cancelDate" />

            <label for="promisedShipmentDate">Promised Shipment Date:</label>
            <Calendar v-model="orderData.promised_shipment_date" id="promisedShipmentDate" />

            <label for="remark">Remark:</label>
            <InputText v-model="orderData.remark" id="remark" />

            <label for="quantity">Quantity:</label>
            <InputText v-model="orderData.quantity" id="quantity" />

            <label for="unit">Unit:</label>
            <InputText v-model="orderData.unit" id="unit" />

            <label for="unitCost">Unit Cost:</label>
            <InputText v-model="orderData.unit_cost" id="unitCost" />

            <label for="orderGrossAmount">Order Gross Amount:</label>
            <InputText v-model="orderData.order_gross_amount" id="orderGrossAmount" />

            <label for="currencyMode">Currency Mode:</label>
            <InputText v-model="orderData.currency_mode" id="currencyMode" />

            <label for="foreignAmount">Foreign Amount:</label>
            <InputText v-model="orderData.foreign_amount" id="foreignAmount" />

            <label for="status">Status:</label>
            <InputText v-model="orderData.status" id="status" />


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
