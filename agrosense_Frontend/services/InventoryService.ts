import { useRuntimeConfig } from "nuxt/app";

export default class InventoryService {
  async getInventory() {
    const config = useRuntimeConfig();

    // Access public variables
    /*   return $fetch("/items?format=json", {
      baseURL: config.public.apiBase,
      headers: {
        // Access a private variable (only available on the server)
        Authorization: `Bearer ${config.apiSecret}`,
      },
    }).then((d) => d); */

    return fetch(config.public.apiBase + "/inventory?format=json")
      .then((res) => res.json())
      .then((d) => d);
  }
}
