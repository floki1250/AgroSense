import { defineNuxtRouteMiddleware, navigateTo, useCookie } from "nuxt/app";

export default defineNuxtRouteMiddleware((to, from) => {
  const auth = useCookie("token", { HttpOnly: true });

  if (!auth.value) {
    return navigateTo("/login");
  }
});
