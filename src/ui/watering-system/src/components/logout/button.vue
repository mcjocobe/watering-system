<script setup>
import { useAuthenticationStore } from "./store.js";

const jwt = defineModel();
const store = useAuthenticationStore();
</script>

<template>
  <div class="medium middle-align center-align">
    <button @click="store.logout" class="large round">Logout</button>
  </div>
</template>

<style scoped>
div {
  place-items: center;
}
</style>
