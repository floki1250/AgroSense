<script setup>
import { FilterMatchMode } from "primevue/api";
import { ref } from "vue";
import { useToast } from "primevue/usetoast";

const toast = useToast();
const config = useRuntimeConfig();
const url = config.public.apiBase + "/immo/";
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const selectedDate = ref(null);

const selectedDateFormatted = computed(() => {
  if (selectedDate.value) {
    const date = new Date(selectedDate.value);
    const day = date.getDate().toString().padStart(2, "0");
    const month = (date.getMonth() + 1).toString().padStart(2, "0");
    const year = date.getFullYear().toString().substr(-2);
    return `${day}-${month}-${year}`;
  } else {
    return "";
  }
});
let itemDialog = ref(false);
let deleteItemDialog = ref(false);
let deleteItemsDialog = ref(false);
let item = {
  idimmo: "",
  description: "",
  date_of_commissioning: selectedDateFormatted,
  cost_account: null,
  depreciation_period: null,
  amount_per_hour: null,
  usage: null,
};
const show_details = ref(false);
let selecteditem = ref();

let submitted = false;
const {
  data: dataitems,
  pending,
  refresh,
  error,
} = await useFetch(url, {
  responseType: "json",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});
const openNew = () => {
  let item = {
    idimmo: "",
    description: "",
    date_of_commissioning: selectedDateFormatted,
    cost_account: null,
    depreciation_period: null,
    amount_per_hour: null,
    usage: null,
  };
  show_details.value = true;
  itemDialog.value = true;
};

const hideDialog = () => {
  itemDialog.value = false;
  submitted = false;
};
async function addItem(data) {
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
async function deleteItem(data) {
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
async function updateItem(data) {
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
  show_details.value = true;
};
const details = (it) => {
  item = { ...it };
  itemDialog.value = true;
  show_details.value = false;
};
const confirmDeleteItem = (item) => {
  item = item;
  deleteItemDialog.value = true;
};
function exportToCSV(dataObj, filename) {
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
                <Button
                  label="New"
                  icon="pi pi-plus"
                  class="p-button-info p-button-text"
                  @click="openNew"
                />

                <Button
                  label="Refresh"
                  icon="pi pi-refresh"
                  class="p-button-warning p-button-text"
                  @click="refresh"
                />
              </span>
            </div>
          </template>

          <template #end>
            <FileUpload
              mode="basic"
              accept="text/*"
              :max-file-size="1000000"
              label="Import"
              choose-label="Import"
              class="mr-2 inline-block p-button-text"
            />
            <Button
              label="Export"
              icon="pi pi-upload"
              class="p-button-help p-button-text"
              @click="exportCSV"
            ></Button>
          </template>
        </Toolbar>
        <div v-if="pending">
          <div class="card flex justify-content-center">
            <ProgressSpinner />
          </div>
        </div>
        <div v-else-if="error">
          {{ error }}
        </div>

        <div v-else class="grid">
          <div v-for="el in dataitems" class="col">
            <commonCard
              :id="el.idimmo"
              :usage="el.usage"
              :title="el.description"
              @delete="deleteItemsDialog = true"
              @edit="editItem(el)"
              @details="details(el)"
            />
          </div>
        </div>

        <Dialog
          v-model:visible="itemDialog"
          :style="{ width: '450px' }"
          header="Immo Details"
          class="p-fluid"
          modal
        >
          <div class="field">
            <label for="idimmo">Immo Id</label>
            <InputText
              id="idimmo"
              v-model.trim="item.idimmo"
              required="true"
              autofocus
              :disabled="!show_details"
            />
            <small v-if="submitted && !item.idimmo" class="p-invalid"
              >idimmo is required.</small
            >
          </div>
          <div class="field">
            <label for="description">Immo description</label>
            <InputText
              id="description"
              v-model.trim="item.description"
              required="true"
              autofocus
              :class="{
                'p-invalid': submitted && !selecteditem.description,
              }"
              :disabled="!show_details"
            />
            <small v-if="submitted && !item.description" class="p-invalid"
              >description is required.</small
            >
          </div>
          {{ item }}
          <div class="field">
            <label for="date_of_commissioning">date of commissioning</label>
            <Calendar
              id="date_of_commissioning"
              v-model="selectedDate"
              showIcon
              dateFormat="dd-mm-yy"
              :disabled="!show_details"
            />
          </div>
          <div class="field">
            <label for="cost_account">cost account</label>
            <InputNumber
              id="cost_account"
              v-model="item.cost_account"
              required="true"
              locale="tn-TN"
              :minFractionDigits="3"
              mode="currency"
              currency="TND"
              :disabled="!show_details"
            />
          </div>
          <div class="field">
            <label for="depreciation_period">depreciation period </label>
            <InputNumber
              id="depreciation_period"
              v-model="item.depreciation_period"
              required="true"
              suffix=" Hours"
              :disabled="!show_details"
            />
          </div>
          <div class="field">
            <label for="amount_per_hour">amount/hour </label>
            <InputNumber
              id="amount_per_hour"
              v-model="item.amount_per_hour"
              suffix=" TND"
              disabled
            />
          </div>
          <div class="field">
            <label for="usage">usage </label>
            <InputNumber
              id="usage"
              v-model="item.usage"
              suffix=" Hours"
              disabled
            />
          </div>
          <template #footer>
            <Button
              label="Cancel"
              icon="pi pi-times"
              class="p-button-outlined p-button-danger"
              @click="hideDialog"
              v-show="show_details"
            />
            <Button
              label="Save"
              icon="pi pi-check"
              class="p-button-outlined"
              @click="saveItem"
              v-show="show_details"
            />
          </template>
        </Dialog>

        <Dialog
          v-model:visible="deleteItemsDialog"
          :style="{ width: '450px' }"
          header="Confirm"
          :modal="true"
        >
          <div class="flex align-items-center justify-content-center">
            <i
              class="pi pi-exclamation-triangle mr-3"
              style="font-size: 2rem"
            />
            <span v-if="item"
              >Are you sure you want to delete
              <b>{{ item.idimmo }} : {{ item.description }} </b> ?</span
            >
          </div>
          <template #footer>
            <Button
              label="No"
              icon="pi pi-times"
              class="p-button-text"
              @click="deleteItemsDialog = false"
            />
            <Button
              label="Yes"
              icon="pi pi-check"
              class="p-button-text"
              @click="deleteSelectedItem"
            />
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
