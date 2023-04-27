<script setup>
import { useField } from 'vee-validate';

const props = defineProps({
  name: String
});

// Validator function
const isRequired = value => (value ? true : 'This field is required');

const { value, errorMessage } = useField(props.name, isRequired);
</script>

<template>
  <span class="p-float-label">
    <InputText id="value" v-model="value" v-validate="'required|email'" type="text" :class="{ 'p-invalid': errorMessage }"
      aria-describedby="text-error" />
    <label for="value">Name - Surname</label>
  </span>
  <small id="text-error" class="p-error">{{ errorMessage || "&nbsp;" }}</small>
</template>
