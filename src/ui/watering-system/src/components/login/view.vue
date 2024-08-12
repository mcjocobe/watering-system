<script setup>
import { useAuthenticationStore } from "./store.js";
import AuthenticationForm from "./form.vue";

const store = useAuthenticationStore();
</script>

<template>
  <h2>Authentication</h2>
  <AuthenticationForm v-if="!store.authenticated"></AuthenticationForm>
</template>
