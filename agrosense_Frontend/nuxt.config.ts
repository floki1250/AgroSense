import { defineNuxtConfig } from "nuxt/config";
const cred = {
  type: "service_account",
  project_id: "esp32tempo",
  private_key_id: "87da354a4ace52aadf5fafef8018df890680f172",
  private_key:
    "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDEEeFLX13Su1KL\ntrwSNRcpelTObp3ZP5tDoikCz+u0F8uGk5ZsEZpvGK3pvnGCVNXiYD1p04dOCfBN\nGwL1HD//iz3iWYHslsF8R0pktha0ek0YMHQI8lGF9dcI87wTRXg0dNAVMLjruahv\nsiRZlZKmzsjNzktoyYL44KnF2yuZ9+o0wB/sxJXk0HvMKHzP9xFbko1gJiwAvdIc\nT67oTL6whBSk261tb0NIKw1Ews21Yk2o8wzivSvg5OZGB9RJOF9d+O6LqzUEXFji\napm/zD5de6dRG7tqin5OQOzMekDpgbKTHgtuG+sQ9FzRfHCGYP4dARzpnCUDwA49\nVvPS3TYjAgMBAAECggEAJ3YJx+ertGvrEx91/pwcy0ZJpzpwHndEwnnykxRRte9M\nEQvHLHzmfhGTfwXLRpXYbjU8Zv4hrz0k1f/nunkzEDVwAQxOr9Uvn9mhSV+0diJf\nPc0SrXJHohR2cODNK3vB05zm/DzQGvFEyyYpVrZZy6S2mWU5nB9icsCUqrOPtO7s\nIgbvcuNedV833rIkEOcU6JjV/qhBGBWvpEz7ZYeDWvg6p7/1d5Osbi1yIL3AjEHd\nZVtRzfNFhlrYBIBh2lEmVqIySEF4BEVCYYjVYZtHHGt7WICHtlH2BOzzmuSJ7l3r\nCtSQ8KINf+H4oh90lfZuWtGgvYAULx7wnaSs9wEIEQKBgQDuj4noeNORJ2Ar4PQd\n5Jta5cREprLXB9tTt4SxfHRqOj1M95a4TUndAwt4M/6r3tVNXnPmzLvyRUAPjmJw\nI0i9dob4D/mL7F52/gyeYUYYeNNzNJfF8SmzgOWueL8BWzPM+gXRajEuyVg8OuKP\n+M+CiqBc5SrN8LKzeY+IWCyQpwKBgQDSZyk5Fi6OfPgv+UuHqEJ8M6CVq4yRZ3XF\nlbq7OlXZDXBmPvBP7Z9m7svPBB0xXWTe7FnSpJk+Y8dXD12IlYQsaIqEMkGq2HY9\n/XVVB1PdnwvQMi2MJXYilvReCzfMBJ9O5RFSVJlLUpr92FEom/MkDal2oXtIkoGe\nEAemkL0CJQKBgQCzlmsDDrJ2O2Yyog4j0s0BCKdP5w4KwmdiBm1mD4Kz1VQAdQKJ\ni+Vm87vWqY22ZPG+ZLRrswRpxagMDewc7vL7bhb890mtBCu4+FcXg7L5CTxlJdp7\nsKjr8MT3Kv7fToEYdb+bfo234usBrHKSX4QXibRfOkWW8vQUGBbtVTN3UQKBgCQ5\nNISqh/tqEoSX4+QIGOIvNT9vWHUUHdeVjp97TJpg0PAZd+Aa5e2fwSDz8V61WI90\nm4ZDZkqyfPhFIfJI44eNvANEb7/NIpZLk66+4zZtkmgWq3bMYElWOd4TClkqlo7L\nqy7Ed9va7eo0GszmBHc5jupopMP6zSv8UIThuFitAoGBAK5ZH2dVH/Vlv3kaT4N/\nQS4U2M+/iJzae+yT8VRB7CPvqN2KanKGcSBqiLOVtCIwD5GwRzdbuYdgTKPsDcgW\n5X/mx7snoyZwGY7EinWOe3j/OeDWJ0BOqfh2NQfQjjZbK/6ph7ynaP5EHRHObKAM\nTDtEZJEeZ4ufpwgidj4lP1y4\n-----END PRIVATE KEY-----\n",
  client_email: "firebase-adminsdk-h536l@esp32tempo.iam.gserviceaccount.com",
  client_id: "116411128440932554309",
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  token_uri: "https://oauth2.googleapis.com/token",
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  client_x509_cert_url:
    "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-h536l%40esp32tempo.iam.gserviceaccount.com",
  universe_domain: "googleapis.com",
};

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
    "@nuxtjs/device",
    "@nuxt/image-edge",
    "nuxt-vuefire",
    "nuxt-pdfeasy",
  ],
  /* ignore */
  vuefire: {
    config: {
      apiKey: "AIzaSyDTEneBJ_dQGKdc5UWoZZ3v20AFl_tV85k",
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
        private_key:
          "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDEEeFLX13Su1KL\ntrwSNRcpelTObp3ZP5tDoikCz+u0F8uGk5ZsEZpvGK3pvnGCVNXiYD1p04dOCfBN\nGwL1HD//iz3iWYHslsF8R0pktha0ek0YMHQI8lGF9dcI87wTRXg0dNAVMLjruahv\nsiRZlZKmzsjNzktoyYL44KnF2yuZ9+o0wB/sxJXk0HvMKHzP9xFbko1gJiwAvdIc\nT67oTL6whBSk261tb0NIKw1Ews21Yk2o8wzivSvg5OZGB9RJOF9d+O6LqzUEXFji\napm/zD5de6dRG7tqin5OQOzMekDpgbKTHgtuG+sQ9FzRfHCGYP4dARzpnCUDwA49\nVvPS3TYjAgMBAAECggEAJ3YJx+ertGvrEx91/pwcy0ZJpzpwHndEwnnykxRRte9M\nEQvHLHzmfhGTfwXLRpXYbjU8Zv4hrz0k1f/nunkzEDVwAQxOr9Uvn9mhSV+0diJf\nPc0SrXJHohR2cODNK3vB05zm/DzQGvFEyyYpVrZZy6S2mWU5nB9icsCUqrOPtO7s\nIgbvcuNedV833rIkEOcU6JjV/qhBGBWvpEz7ZYeDWvg6p7/1d5Osbi1yIL3AjEHd\nZVtRzfNFhlrYBIBh2lEmVqIySEF4BEVCYYjVYZtHHGt7WICHtlH2BOzzmuSJ7l3r\nCtSQ8KINf+H4oh90lfZuWtGgvYAULx7wnaSs9wEIEQKBgQDuj4noeNORJ2Ar4PQd\n5Jta5cREprLXB9tTt4SxfHRqOj1M95a4TUndAwt4M/6r3tVNXnPmzLvyRUAPjmJw\nI0i9dob4D/mL7F52/gyeYUYYeNNzNJfF8SmzgOWueL8BWzPM+gXRajEuyVg8OuKP\n+M+CiqBc5SrN8LKzeY+IWCyQpwKBgQDSZyk5Fi6OfPgv+UuHqEJ8M6CVq4yRZ3XF\nlbq7OlXZDXBmPvBP7Z9m7svPBB0xXWTe7FnSpJk+Y8dXD12IlYQsaIqEMkGq2HY9\n/XVVB1PdnwvQMi2MJXYilvReCzfMBJ9O5RFSVJlLUpr92FEom/MkDal2oXtIkoGe\nEAemkL0CJQKBgQCzlmsDDrJ2O2Yyog4j0s0BCKdP5w4KwmdiBm1mD4Kz1VQAdQKJ\ni+Vm87vWqY22ZPG+ZLRrswRpxagMDewc7vL7bhb890mtBCu4+FcXg7L5CTxlJdp7\nsKjr8MT3Kv7fToEYdb+bfo234usBrHKSX4QXibRfOkWW8vQUGBbtVTN3UQKBgCQ5\nNISqh/tqEoSX4+QIGOIvNT9vWHUUHdeVjp97TJpg0PAZd+Aa5e2fwSDz8V61WI90\nm4ZDZkqyfPhFIfJI44eNvANEb7/NIpZLk66+4zZtkmgWq3bMYElWOd4TClkqlo7L\nqy7Ed9va7eo0GszmBHc5jupopMP6zSv8UIThuFitAoGBAK5ZH2dVH/Vlv3kaT4N/\nQS4U2M+/iJzae+yT8VRB7CPvqN2KanKGcSBqiLOVtCIwD5GwRzdbuYdgTKPsDcgW\n5X/mx7snoyZwGY7EinWOe3j/OeDWJ0BOqfh2NQfQjjZbK/6ph7ynaP5EHRHObKAM\nTDtEZJEeZ4ufpwgidj4lP1y4\n-----END PRIVATE KEY-----\n",
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
    accessToken:
      "pk.eyJ1IjoiYWRhbWRyOTgiLCJhIjoiY2xnbGljZm10MDM1bzNncDIwcGg5cWZuZCJ9.Z6jB1I3mKgGz2sqoIEwxOQ",
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
