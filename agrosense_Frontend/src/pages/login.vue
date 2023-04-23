<template>
  <div class="card flex justify-content-center">
    <form @submit="onSubmit" class="flex flex-column gap-2">
      <InputComp></InputComp>
      <Toast />
    </form>
  </div>
</template>

<script setup>
import { useToast } from "primevue/usetoast";
import { useField, useForm } from "vee-validate";
import InputComp from "../components/common/InputComp.vue";

const { handleSubmit, resetForm } = useForm();
const { value, errorMessage } = useField("value", validateField);
const toast = useToast();

function validateField(value) {
  if (!value) {
    return "Name - Surname is required.";
  }

  return true;
}

const onSubmit = handleSubmit((values) => {
  if (values.value && values.value.length > 0) {
    toast.add({
      severity: "info",
      summary: "Form Submitted",
      detail: values.value,
      life: 3000,
    });
    resetForm();
  }
});
</script>
