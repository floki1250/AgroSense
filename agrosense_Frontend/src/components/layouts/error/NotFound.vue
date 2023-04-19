<script lang="ts" setup>
interface Props {
  error: {
    description?: string;
    message?: string;
    statusCode: string;
    statusMessage: string;
    url: string;
  };
}

const { error } = defineProps<Props>();
</script>

<template>
  <div>
    <h1>404</h1>
    <p>
      The page you are looking for does not exist. How you got here is a
      mystery. But you can click the button below to go back to the homepage.
    </p>
    <div style="text-align: center">
      <NuxtLink to="/">
        <Button
          label="Home"
          icon="pi pi-fw pi-home"
          class="p-button-outlined mr-2 mb-2"
        >
        </Button>
      </NuxtLink>
    </div>
  </div>
</template>
<style scoped lang="scss">
h1 {
  text-align: center;
  font-size: 20em;
}
p {
  text-align: center;
}
</style>
