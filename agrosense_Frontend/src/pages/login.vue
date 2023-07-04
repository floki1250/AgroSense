<template>
  <div class="login_container  h-screen w-screen flex align-items-center justify-content-center">
    <Toast />
    <div class="grid login_card flex align-items-center justify-content-center  ">
      <div class="col-6 container h-full" v-if="$device.isDesktop">
        <div class="content img">

        </div>
      </div>
      <div class="col-6 flex align-items-center justify-content-center p-fluid ">
        <div>
          <div class="flex align-items-center justify-content-center m-5">

            <nuxt-img src="/images/agro.svg" width="65" />
            <h2 class="p-3 vertical-align-bottom" style="color: #45c295">AgroSense</h2>
          </div>

          <hr><br>
          <div class="flex flex-column gap-4">
            <span class="p-float-label">
              <InputText id="username" v-model="username" :class="{ 'p-invalid': errorMessage }" />
              <label for="username">Username</label>
            </span>
            <span class="p-float-label">
              <Password v-model="password" inputId="password" :feedback="false" />
              <label for="password">Password</label>
            </span>

            <small class="p-error" id="text-error">{{ errorMessage }}</small>
            <Button rounded :loading="loading" @click="login" label="Sign In" icon="pi pi-sign-in">


            </Button>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useToast } from "primevue/usetoast";

definePageMeta({
  layout: "empty",
});
useHead({
  title: 'Agrosense | Login'
});
const username = ref();
const password = ref();
const config = useRuntimeConfig();
const loading = ref(false);
const toast = useToast();
const showError = () => {
  toast.add({ severity: 'error', summary: 'Error', detail: "User and Password Combination invalid", life: 3000 });
};

const url = config.public.apiBase + "/auth/token/login/";
const auth = useCookie("token", { HttpOnly: true });
const errorMessage = ref("")
function login () {

  let user = new URLSearchParams();
  user.append("username", username.value);
  user.append("password", password.value);
  loading.value = true
  console.log(loading.value)
  $fetch(url, {
    method: "POST",
    responseType: "json",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: user,
  })
    .then((response) => {


      auth.value = response.auth_token;
      loading.value = false;
      navigateTo("/");
    })
    .catch((error) => {
      showError();
      console.log("Error: " + error);
      loading.value = false;
    });
}
</script>
<style scoped>
.login_container {
  background-color: whitesmoke;
}


.container {
  display: flex;
  flex-direction: column;
}

.content {
  flex-grow: 1;
}

.img {
  background-image: url('/images/bg.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: 50% 50%;
  border-radius: 1rem;
  border: 2px solid rgb(250, 250, 250);
}

.login_card {
  border-radius: 1rem;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  background-color: rgba(250, 250, 250, 0.9);
  backdrop-filter: blur(16px);
  border: 2px solid rgb(255, 255, 255);
  height: 90%;
  width: 80%;
}
</style>
