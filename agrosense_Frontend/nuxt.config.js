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
      apiBase:
        process.env.NODE_ENV === "development"
          ? "http://127.0.0.1:8000"
          : process.env.BASE_URL,
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
    "@nuxtjs/device",
    "@nuxt/image-edge",
    "nuxt-vuefire",
    "nuxt-pdfeasy",
  ],
  /* ignore */
  vuefire: {
    config: {
      apiKey: process.env.apiKey,
      authDomain: "esp32tempo.firebaseapp.com",
      databaseURL: "https://esp32tempo-default-rtdb.firebaseio.com",
      projectId: "esp32tempo",
      storageBucket: "esp32tempo.appspot.com",
      messagingSenderId: "550194135824",
      appId: "1:550194135824:web:fa4cd9720ab3a89189db95",
      measurementId: "G-7N2Q7D1CJJ",
    },
    admin: {
      serviceAccount: {
        type: "service_account",
        project_id: "esp32tempo",
        private_key_id: "87da354a4ace52aadf5fafef8018df890680f172",
        private_key: process.env.private_key,
        client_email:
          "firebase-adminsdk-h536l@esp32tempo.iam.gserviceaccount.com",
        client_id: "116411128440932554309",
        auth_uri: "https://accounts.google.com/o/oauth2/auth",
        token_uri: "https://oauth2.googleapis.com/token",
        auth_provider_x509_cert_url:
          "https://www.googleapis.com/oauth2/v1/certs",
        client_x509_cert_url:
          "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-h536l%40esp32tempo.iam.gserviceaccount.com",
        universe_domain: "googleapis.com",
      },
    },
  },

  mapbox: {
    accessToken: process.env.MapBoxToken,
  },

  nitro: {
    preset: "node-server",
  },

  srcDir: "src/",
  vite: {
    build: {
      sourcemap: false,
    },
    clearScreen: true,
    logLevel: "info",
  },
});
