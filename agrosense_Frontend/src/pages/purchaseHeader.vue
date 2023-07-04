<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | Purchase Order Header'
});
const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/purchaseorderheader/";

const auth = useCookie("token", { HttpOnly: true });
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
let itemDialog = ref(false);

let deleteItemsDialog = ref(false);
const form = ref({
  order_no: 0,
  order_type: '',
  company: 0,
  supplier_id: 0,
  requested_date: 0,
  order_date: null,
  scheduled_pick_date: null,
  actual_ship_date: null,
  cancel_date: null,
  date_received: null,
  price_effective_date: null,
  promised_shipment_date: null,
  remark: '',
  order_gross_amount: 0,
  currency_mode: '',
  foreign_open_amount: 0,
  status: 0
})

const dt = ref(null);
let selecteditem = ref({
  order_no: 0,
  order_type: '',
  company: 0,
  supplier_id: 0,
  requested_date: 0,
  order_date: null,
  scheduled_pick_date: null,
  actual_ship_date: null,
  cancel_date: null,
  date_received: null,
  price_effective_date: null,
  promised_shipment_date: null,
  remark: '',
  order_gross_amount: 0,
  currency_mode: '',
  foreign_open_amount: 0,
  status: 0
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
  //submitted.value = false;
  form.value = {}
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

  $fetch(url + data.order_no + "/", {
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
  $fetch(url + data.order_no + "/", {
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

    updateItem(form.value);

  } else {

    addItem(form.value);

  }

  itemDialog.value = false;
  form.value = {};
  refresh();
};

const editItem = () => {
  form.value = selecteditem.value
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
const orders_values = ref();
const print_flag = ref(false)
const order_no = ref()
const ShipDate = ref()
const company = ref()
const to = ref()
async function print (order) {
  to.value = order.company
  order_no.value = order.order_no
  ShipDate.value = order.date_received
  const purchaseorderdetail_url = config.public.apiBase + "/purchaseorderdetail/";
  const {
    data: orders
  } = await useFetch(purchaseorderdetail_url, {
    responseType: "json",
    headers: {
      "Authorization": `Token ${auth.value}`,
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    transform: (orders) => {
      return orders.filter(el => el.order_no == order.order_no);
    }
  });
  orders_values.value = orders.value.map(el => Object.values({ item: el.item_id, quantity: el.quantity, unit_cost: el.unit_cost, unit: el.unit, cost: el.order_gross_amount }))
  let total = 0;
  for (let i = 0; i < orders_values.value.length; i++) {
    total += orders_values.value[i][4];
  }
  orders_values.value.push(["Total", ' ', ' ', ' ', total])

  print_flag.value = true
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
                <Button label="Print" icon="pi pi-print" class=" p-button-text" @click="print(selecteditem)" />
              </span>
            </div>
          </template>

          <template #end>
            <FileUpload mode="basic" accept="text/*" :max-file-size="1000000" label="Import" choose-label="Import"
              class="mr-2 inline-block p-button-text" />
            <Button label="Export" icon="pi pi-upload" class="p-button-help p-button-text" @click="exportCSV"></Button>
          </template>
        </Toolbar>



        <DataTable ref="dt" v-model:selection="selecteditem" :value="dataitems" data-key="order_no" :paginator="true"
          :rows="10" :filters="filters"
          paginator-template="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          :rows-per-page-options="[5, 10, 25]"
          current-page-report-template="Showing {first} to {last} of {totalRecords} products" responsive-layout="scroll">
          <template #header>
            <div class="flex flex-column md:flex-row md:justify-content-between md:align-items-center">
              <h5 class="m-0">Purchase Order Header</h5>
              <span class="block mt-2 md:mt-0 p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
              </span>
            </div>
          </template>

          <Column selection-mode="single" header-style="width: 3rem" />
          <Column field="order_no" header="Id" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">order no</span>
              {{ slotProps.data.order_no }}
            </template>
          </Column>
          <Column field="order_type" header="order_type" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">order_type</span>
              {{ slotProps.data.order_type }}
            </template>
          </Column>
          <Column field="company" header="company" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">company</span>
              {{ slotProps.data.company }}
            </template>
          </Column>
          <Column field="supplier_id" header="cost" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">supplier_id</span>
              {{ slotProps.data.supplier_id }}
            </template>
          </Column>
          <Column field="requested_date" header="requested_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Date requested</span>
              {{ slotProps.data.requested_date }}
            </template>
          </Column>
          <Column field="order_date" header="order_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">Date order_date</span>
              {{ slotProps.data.order_date }}
            </template>
          </Column>
          <Column field="scheduled_pick_date" header="scheduled_pick_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">scheduled_pick_date</span>

              {{ slotProps.data.scheduled_pick_date }}
            </template>
          </Column>
          <Column field="actual_ship_date" header="actual_ship_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">actual_ship_date</span>

              {{ slotProps.data.actual_ship_date }}
            </template>
          </Column>
          <Column field="actual_ship_date" header="actual_ship_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">actual_ship_date</span>

              {{ slotProps.data.actual_ship_date }}
            </template>
          </Column>
          <Column field="cancel_date" header="cancel_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">cancel_date</span>

              {{ slotProps.data.cancel_date }}
            </template>
          </Column>
          <Column field="date_received" header="date_received" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">date_received</span>

              {{ slotProps.data.date_received }}
            </template>
          </Column>
          <Column field="price_effective_date" header="price_effective_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">price_effective_date</span>

              {{ slotProps.data.price_effective_date }}
            </template>
          </Column>
          <Column field="price_effective_date" header="price_effective_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">price_effective_date</span>

              {{ slotProps.data.price_effective_date }}
            </template>
          </Column>
          <Column field="price_effective_date" header="price_effective_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">price_effective_date</span>

              {{ slotProps.data.price_effective_date }}
            </template>
          </Column>
          <Column field="promised_shipment_date" header="promised_shipment_date" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">promised_shipment_date</span>

              {{ slotProps.data.promised_shipment_date }}
            </template>
          </Column>
          <Column field="remark" header="remark" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">remark</span>

              {{ slotProps.data.remark }}
            </template>
          </Column>
          <Column field="order_gross_amount" header="order_gross_amount" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">order_gross_amount</span>

              {{ slotProps.data.currency_mode }}
            </template>
          </Column>

          <Column field="foreign_open_amount" header="foreign_open_amount" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">foreign_open_amount</span>

              {{ slotProps.data.foreign_open_amount }}
            </template>
          </Column>
          <Column field="status" header="status" :sortable="true">
            <template #body="slotProps">
              <span class="p-column-title">status</span>

              {{ slotProps.data.status }}
            </template>
          </Column>
        </DataTable>

        <Dialog v-model:visible="itemDialog" :style="{ width: '450px' }" header="Create Order" class="p-fluid" modal>

          <div>

            <div class="p-field">
              <label for="order_no">Order No</label>
              <InputText v-model="form.order_no" id="order_no" />
            </div>

            <div class="p-field">
              <label for="order_type">Order Type</label>
              <InputText v-model="form.order_type" id="order_type" />
            </div>

            <div class="p-field">
              <label for="company">Company</label>
              <InputText v-model="form.company" id="company" />
            </div>

            <div class="p-field">
              <label for="supplier_id">Supplier ID</label>
              <InputText v-model="form.supplier_id" id="supplier_id" />
            </div>

            <div class="p-field">
              <label for="requested_date">Requested Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.requested_date" id="requested_date"
                dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="order_date">Order Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.order_date" id="order_date"
                dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="scheduled_pick_date">Scheduled Pick Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.scheduled_pick_date"
                id="scheduled_pick_date" dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="actual_ship_date">Actual Ship Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.actual_ship_date" id="actual_ship_date"
                dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="cancel_date">Cancel Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.cancel_date" id="cancel_date"
                dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="date_received">Date Received</label>
              <input type="date" class="p-inputtext p-component" v-model="form.date_received" id="date_received"
                dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="price_effective_date">Price Effective Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.price_effective_date"
                id="price_effective_date" dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="promised_shipment_date">Promised Shipment Date</label>
              <input type="date" class="p-inputtext p-component" v-model="form.promised_shipment_date"
                id="promised_shipment_date" dateFormat="yy-mm-dd" />
            </div>

            <div class="p-field">
              <label for="remark">Remark</label>

              <InputText v-model="form.remark" id="remark" rows="4" cols="4" />
            </div>

            <div class="p-field">
              <label for="order_gross_amount">Order Gross Amount</label>
              <InputNumber v-model="form.order_gross_amount" id="order_gross_amount" />
            </div>

            <div class="p-field">
              <label for="currency_mode">Currency Mode</label>
              <InputText v-model="form.currency_mode" id="currency_mode" />
            </div>

            <div class="p-field">
              <label for="foreign_open_amount">Foreign Open Amount</label>
              <InputNumber v-model="form.foreign_open_amount" id="foreign_open_amount" />
            </div>

            <div class="p-field">
              <label for="status">Status</label>
              <InputText v-model="form.status" id="status" />
            </div>


          </div>


          <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-outlined p-button-danger" @click="hideDialog" />
            <Button label="Save" icon="pi pi-check" class="p-button-outlined" @click="saveItem()" />
          </template>
        </Dialog>

        <Dialog v-model:visible="deleteItemsDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
          <div class="flex align-items-center justify-content-center">
            <i class="pi pi-exclamation-triangle mr-3" style="font-size: 2rem" />
            <span v-if="form">Are you sure you want to delete Order Number
              <b>{{ selecteditem.order_no }}</b>?</span>
          </div>
          <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteItemsDialog = false" />
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedItem" />
          </template>
        </Dialog>
      </div>
    </div>
    <div class="col-12">
      <div v-if="print_flag">
        <commonInvoice :values="orders_values" :to="to" :ShipDate="ShipDate" :order="order_no"></commonInvoice>
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
