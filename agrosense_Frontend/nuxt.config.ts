import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  app: {
    head: {
      title: "AgroSense",
      meta: [
        { "http-equiv": "x-ua-compatible", content: "IE=edge" },
        { name: "viewport", content: "width=device-width, initial-scale=1.0" },
      ],
      link: [{ rel: "icon", href: "/favicon.ico" }],
    },
  },
  runtimeConfig: {
    // The private keys which are only available server-side
    apiSecret: "123",
    // Keys within public are also exposed client-side
    public: {
      apiBase: "http://127.0.0.1:8000",
    },
  },
  build: {
    transpile: ["chart.js", "primevue"],
  },

  components: [
    { path: "~/components/common", prefix: "common" },
    "~/components",
  ],

  css: [
    "primevue/resources/primevue.css",
    "primeflex/primeflex.css",
    "primeicons/primeicons.css",
    "~/assets/styles/theme.css",
    "~/assets/styles/layout.scss",
    "~/assets/demo/flags/flags.css",
  ],

  dir: {
    public: "../public/",
  },

  experimental: {
    reactivityTransform: false,
    treeshakeClientOnly: false,
  },

  imports: {
    autoImport: true,
    addons: {
      vueTemplate: true,
    },
  },

  modules: [
    "@pinia/nuxt",
    "@vueuse/nuxt",
    "~/modules/primevue",
    "nuxt-icon",
    "nuxt-mapbox",
  ],
  /* ignore */
  mapbox: {
    accessToken:
      "pk.eyJ1IjoiYWRhbWRyOTgiLCJhIjoiY2xnbGljZm10MDM1bzNncDIwcGg5cWZuZCJ9.Z6jB1I3mKgGz2sqoIEwxOQ",
  },
  nitro: {
    preset: "node-server",
  },

  srcDir: "src/",
  vue: {
    compilerOptions: {
      isCustomElement: (tag) => tag === "vue-weather",
    },
  },
  vite: {
    build: {
      sourcemap: false,
    },
    clearScreen: true,
    logLevel: "info",
  },
});
