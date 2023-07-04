<script lang="ts" setup>
const error = useError()
</script>

<template>
  <div>
    <h1>ERROR </h1>
    <h1>{{ error.statusCode }} </h1>
    <p>
      {{ error.message }}
    </p>
    <div style="text-align: center">
      <NuxtLink to="/">
        <Button label="Home" icon="pi pi-fw pi-home" class="p-button-outlined mr-2 mb-2">
        </Button>
      </NuxtLink>
    </div>
  </div>
</template>
<style scoped lang="scss">
h1 {
  text-align: center;
  font-size: 11em;
}

p {
  text-align: center;
}
</style>
