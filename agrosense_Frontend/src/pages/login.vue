<template>
  <div class="h-screen w-screen flex align-items-center justify-content-center" style="background-image:url('/images/bg.jpg');  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;">

    <div class="card gap-1 p-fluid m-5 w-10 xl:w-4">
      <div class="flex align-items-center justify-content-center m-5">
        <img alt="Logo" src="/images/agro.svg" />
        <h2 class="p-3" style="color: #45c295">AgroSense</h2>
      </div>

      <hr>
      <div class="m-5">
        <span class="p-float-label">
          <InputText id="username" v-model="username" />
          <label for="username">Username</label>
        </span>
      </div>
      <div class="m-5">
        <span class="p-float-label">
          <Password v-model="password" inputId="password" />
          <label for="password">Password</label>
        </span>
      </div>
      <div class="m-5"><Button rounded :loading="false" @click="login">
          <Icon name="solar:login-2-bold-duotone" width="20" height="20"></Icon>
          <span class="px-3">Log In</span>
        </Button></div>

      <b>{{ token }}</b>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: "empty",
});
const username = ref();
const password = ref();
const config = useRuntimeConfig();
let token = ref();

const url = config.public.apiBase + "/auth/token/login/";
const auth = useCookie("token", { HttpOnly: true });

function login () {
  console.log(url);
  let user = new URLSearchParams();
  user.append("username", username.value);
  user.append("password", password.value);
  console.log(user);
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: user,
  })
    .then((response) => response.json())
    .then((data) => {
      token = data.auth_token;
      auth.value = token;
      console.log("token Store : ", auth.value);
      navigateTo("/");
    })
    .catch((error) => console.error(error));
}
</script>
