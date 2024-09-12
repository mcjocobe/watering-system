<script setup>
import LoginForm from "./components/login/form.vue";
import LogoutButton from "./components/logout/button.vue";
import { useAuthenticationStore } from "./components/login/store.js";

const store = useAuthenticationStore();
</script>

<template>
  <space></space>
  <div v-if="!store.authenticated" class="middle middle-align">
    <LoginForm />
  </div>
  <div id="logout" v-if="store.authenticated">
    <LogoutButton />
  </div>
  <main v-if="store.authenticated">You are loged in</main>
</template>
