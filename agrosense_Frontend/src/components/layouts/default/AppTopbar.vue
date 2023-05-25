<script setup>
import { defineEmits } from "vue";

const emits = defineEmits(["topbar-menu-toggle", "menu-toggle"]);
const hover = ref(false);
const auth = useCookie("token", { HttpOnly: true });
const logout = () => {
  auth.value = null;
  navigateTo("/login");
};
const onMenuToggle = (event) => {
  emits("menu-toggle", event);
};
</script>

<template>
  <div class="layout-topbar" style="padding: 0px">
    <button
      class="p-link layout-menu-button layout-topbar-button"
      @click="onMenuToggle"
      style="margin-right: 10px"
    >
      <Icon name="tabler:menu-2" width="30" height="30"></Icon>
      <!-- <i class="pi pi-bars" /> -->
    </button>
    <NuxtLink to="/" class="layout-topbar-logo">
      <img alt="Logo" src="/images/agro.svg" />
      <span style="color: #45c295" class="title">AgroSense</span>
    </NuxtLink>

    <button
      v-styleclass="{
        selector: '@next',
        enterClass: 'hidden',
        enterActiveClass: 'scalein',
        leaveToClass: 'hidden',
        leaveActiveClass: 'fadeout',
        hideOnOutsideClick: true,
      }"
      class="p-link layout-topbar-menu-button layout-topbar-button"
    >
      <i class="pi pi-ellipsis-v" />
    </button>

    <TransitionGroup
      name="fade"
      tag="ul"
      class="layout-topbar-menu hidden lg:flex origin-top transition-delay-100 transition-duration-300"
      style="
        background-color: whitesmoke;
        border-radius: 2rem;
        margin-right: 0.5rem;
      "
      @mouseover="hover = true"
      @mouseleave="hover = false"
    >
      <li class="m-2" :key="1">
        <button class="p-link p-button-rounded">
          <Icon name="fluent-emoji:alien-monster" width="30" height="30"></Icon>
        </button>
      </li>

      <li class="m-2" v-if="hover" :key="2">
        <button class="p-link p-button-rounded" @click="logout">
          <Icon name="solar:logout-line-duotone" width="30" height="30"></Icon>
        </button>
      </li>
    </TransitionGroup>
  </div>
</template>
<style scoped>
/* 1. declare transition */
.fade-move,
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

/* 2. declare enter from and leave to state */
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scaleY(0.01) translate(30px, 0);
}

/* 3. ensure leaving items are taken out of layout flow so that moving
      animations can be calculated correctly. */
.fade-leave-active {
  position: absolute;
}

.layout-topbar {
  background-color: rgba(255, 255, 255, 0);
  backdrop-filter: blur(10px);
  box-shadow: none;
}
</style>
