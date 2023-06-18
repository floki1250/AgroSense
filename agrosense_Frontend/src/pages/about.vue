<template>
  <div class="card">
    <iframe src="https://adamdr.vercel.app/" frameborder="0" class=" h-screen w-full"></iframe>
  </div>
</template>
<script setup>
definePageMeta({
  middleware: [
    'auth'
  ]

}); useHead({
  title: 'Agrosense | About'
});
</script>
