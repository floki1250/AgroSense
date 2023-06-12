<script setup>
definePageMeta({
  middleware: [
    'auth'
  ]

});
useHead({
  title: 'Agrosense | Dashboard'
});
const auth = useCookie('token')

const config = useRuntimeConfig();
const url = config.public.apiBase + "/stocktransactions/";
const {
  data: stock_transactions,
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

</script>

<template>
  <div class="grid">


    <div class="col-12 lg:col-4 ">
      <div class="card flex align-items-center justify-content-center" style="height:21rem;padding: 15px;">
        <div class="flex align-items-center justify-content-center">
          <commonWeatherWidget></commonWeatherWidget>
        </div>
      </div>
    </div>
    <div class="col-12 lg:col-8 ">
      <div class="card" style="height: 21rem;padding: 15px;">

      </div>
    </div>

    <div class="col-12 lg:col-6 xl:col-3">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-3">
          <div>
            <span class="block text-500 font-medium mb-3">Orders</span>
            <div class="text-900 font-medium text-xl">
              152
            </div>
          </div>
          <div class="flex align-items-center justify-content-center bg-blue-100 border-round"
            style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-shopping-cart text-blue-500 text-xl" />
          </div>
        </div>
        <span class="text-green-500 font-medium">24 new </span>
        <span class="text-500">since last visit</span>
      </div>
    </div>

    <div class="col-12 lg:col-6 xl:col-3">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-3">
          <div>
            <span class="block text-500 font-medium mb-3">Revenue</span>
            <div class="text-900 font-medium text-xl">
              $2.100
            </div>
          </div>
          <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
            style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-map-marker text-orange-500 text-xl" />
          </div>
        </div>
        <span class="text-green-500 font-medium">%52+ </span>
        <span class="text-500">since last week</span>
      </div>
    </div>
    <div class="col-12 lg:col-6 xl:col-3">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-3">
          <div>
            <span class="block text-500 font-medium mb-3">Customers</span>
            <div class="text-900 font-medium text-xl">
              28441
            </div>
          </div>
          <div class="flex align-items-center justify-content-center bg-cyan-100 border-round"
            style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-inbox text-cyan-500 text-xl" />
          </div>
        </div>
        <span class="text-green-500 font-medium">520 </span>
        <span class="text-500">newly registered</span>
      </div>
    </div>
    <div class="col-12 lg:col-6 xl:col-3">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-3">
          <div>
            <span class="block text-500 font-medium mb-3">Comments</span>
            <div class="text-900 font-medium text-xl">
              152 Unread
            </div>
          </div>
          <div class="flex align-items-center justify-content-center bg-purple-100 border-round"
            style="width: 2.5rem; height: 2.5rem">
            <i class="pi pi-comment text-purple-500 text-xl" />
          </div>
        </div>
        <span class="text-green-500 font-medium">85 </span>
        <span class="text-500">responded</span>
      </div>
    </div>

    <div class="col-12 xl:col-6">
      <div class="card">
        <h5>Stock Transactions</h5>
        <DataTable :value="stock_transactions" :rows="5" :paginator="true" responsive-layout="scroll">
          <Column field="transaction_id" header="Id" :sortable="true" v-if="stock_transactions">
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
        </DataTable>
      </div>

    </div>
    <div class="col-12 xl:col-6">
      <div class="card">
        <h5>Chart Overview</h5>
        <Chart type="line" :data="lineData" />
      </div>

    </div>
  </div>
</template>
