import { useRuntimeConfig } from "nuxt/app";
const config = useRuntimeConfig();
const url = config.public.apiBase + "/items?format=json";
export default class ItemsService {
  async getItems() {
    return fetch(url)
      .then((res) => res.json())
      .then((d) => d);
  }
  async addItem(data: any) {
    try {
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      });

      return response.json();
    } catch (error) {
      return error;
    }
  }
}
