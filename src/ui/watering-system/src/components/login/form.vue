<script setup>
import { useAuthenticationStore } from "./store.js";

const jwt = defineModel();
const store = useAuthenticationStore();

function authenticate() {
  store.authenticate(jwt.value);
}
</script>

<template>
  <article
    class="medium middle-align center-align"
    data-testid="authentication-form"
  >
    <div>
      <i class="extra">person</i>
      <h5>You are not authenticated</h5>
      <p>Add your JWT to authenticate</p>
      <div class="space"></div>
      <nav class="no-space">
        <div
          v-bind:class="[
            store.jwt !== null && !store.valid ? 'invalid' : '',
            'max field border left-round',
          ]"
        >
          <input v-model="jwt" type="password" name="jwt" aria-label="jwt" />
        </div>
        <button @click="authenticate" class="large right-round">
          Authenticate
        </button>
      </nav>
    </div>
  </article>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 1 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: right;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
main {
  display: flex;
  place-items: absolute center;
  padding-right: calc(var(--section-gap) / 2);
}
</style>
