<template>
  <div>
    <h1>Photos of Agriculture</h1>
    <ClientOnly>
      <Carousel
        :value="photos.results"
        :numVisible="1"
        :numScroll="1"
        :responsiveOptions="responsiveOptions"
        v-if="photos"
      >
        <template #item="slotProps">
          {{ slotProps }}
          <div>
            <img :src="slotProps.urls.full" alt="" />
          </div>
        </template>
      </Carousel>
    </ClientOnly>
  </div>
</template>
<script setup>
const { data: photos, error } = await useLazyAsyncData("photos", () =>
  $fetch(
    "https://api.unsplash.com/search/photos?query=agriculture&client_id=6CVs8P90I6487xoLow6nLTWZTs08P2Iu0G6qId-QYHA"
  )
);

if (error) {
  console.error(error);
}
</script>
