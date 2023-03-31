<script lang="ts">
export default {
  emits: ["topbar-menu-toggle", "menu-toggle"],
  computed: {
    darkTheme() {
      return this.$appState.darkTheme;
    },
  },
  methods: {
    onMenuToggle(event) {
      this.$emit("menu-toggle", event);
    },
    onTopbarMenuToggle(event) {
      this.$emit("topbar-menu-toggle", event);
    },
  },
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
      <span style="color: #45c295">AgroSense</span>
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
    <ul class="layout-topbar-menu hidden lg:flex origin-top">
      <li>
        <div class="col-12 mb-2 lg:col-4 lg:mb-0">
          <span class="p-input-icon-right">
            <InputText type="text" placeholder="Search" />
            <i class="pi pi-search" />
          </span>
        </div>
      </li>
      <li>
        <button
          class="p-link layout-topbar-button"
          style="margin: 5px 20px 0px 5px"
        >
          <Icon name="ph:user-circle" width="30" height="30"></Icon>
          <span>Profile</span>
        </button>
      </li>
    </ul>
  </div>
</template>
<style scoped>
.layout-topbar {
  background-color: rgba(255, 255, 255, 0);
  backdrop-filter: blur(10px);
  box-shadow: none;
}
</style>
