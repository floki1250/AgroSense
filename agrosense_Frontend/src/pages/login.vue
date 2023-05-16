<template>
  <div class="login_container  h-screen w-screen flex align-items-center justify-content-center">
    <div class="grid login_card flex align-items-center justify-content-center  ">
      <div class="col-6 container h-full" v-if="$device.isDesktop">
        <div class="content img">

        </div>
      </div>
      <div class="col-6 flex align-items-center justify-content-center p-fluid ">
        <div>
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
              <Password v-model="password" inputId="password" :feedback="false" toggleMask />
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

    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: "empty",
});
useHead({
  title: 'Agrosense | Login'
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
