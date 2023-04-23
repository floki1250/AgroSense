<script setup>
import { useField } from "vee-validate";

const props = defineProps({
  name: string,
});

// Validator function
const isRequired = (value) => (value ? true : "This field is required");

const { value, errorMessage } = useField(props.name, isRequired);
</script>

<template>
  <span class="p-float-label">
    <Password v-model="value" toggleMask />
    <label for="Password">Password</label>
    <small class="p-error" id="text-error">{{
      errorMessage || "&nbsp;"
    }}</small>
  </span>
</template>
