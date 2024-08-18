import "./assets/main.css";

import "material-dynamic-colors";
import { createApp } from "vue";
import App from "./App.vue";
import store from "./store.js";

createApp(App).use(store).mount("#app");
