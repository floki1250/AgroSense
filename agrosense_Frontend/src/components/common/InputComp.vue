<script setup>
const props = defineProps({
  modelValue: Number,
});

</script>

<template>
  <div class="group">
    <Icon name="TND" width="24" height="24"></Icon>
    <input type="number" class="p-inputtext p-component input" :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)">
  </div>
</template>
<style scoped>
.group {
  display: flex;
  line-height: 28px;
  align-items: center;
  position: relative;
  max-width: 190px;
}

.input {

  padding-left: 3rem;
  transition: .3s ease;

}

.input::placeholder {
  color: #ffffff;
}

.icon {
  position: absolute;
  left: 1rem;
  fill: #d4d4d4;
  width: 1rem;
  height: 1rem;
}
</style>
