import { useRuntimeConfig } from "nuxt/app";
const config = useRuntimeConfig();
const url = config.public.apiBase + "/immo?format=json";
export default class ImmobilizationService {
  async getImmo() {
    return fetch(url)
      .then((res) => res.json())
      .then((d) => d);
  }
  async addImmo(data: any) {
    return fetch(url, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }
}
