<script setup>
import { useField } from "vee-validate";

const props = defineProps({
  name: String,
});

// Validator function
const isRequired = (value) => (value ? true : "This field is required");

const { value, errorMessage } = useField(props.name, isRequired);
</script>

<template>
  <span class="p-float-label">
    <InputText
      id="value"
      v-model="value"
      type="text"
      :class="{ 'p-invalid': errorMessage }"
      aria-describedby="text-error"
      v-validate="'required|email'"
    />
    <label for="value">Name - Surname</label>
  </span>
  <small class="p-error" id="text-error">{{ errorMessage || "&nbsp;" }}</small>
</template>
