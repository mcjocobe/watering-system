import { decodeJwt } from "jose";
import { defineStore } from "pinia";

function jwtToPayload(jwt) {
  try {
    return decodeJwt(jwt);
  } catch (_) {
    return {};
  }
}

const useAuthenticationStore = defineStore("authentication", {
  state: () => ({ jwt: null }),
  getters: {
    authenticated: (state) => state.valid,
    email: (state) => (state.valid ? state.payload.user : null),
    payload: (state) => (state.jwt !== null ? jwtToPayload(state.jwt) : {}),
    valid: (state) => "role" in state.payload && "user" in state.payload,
  },
  actions: {
    authenticate(jwt) {
      this.jwt = jwt;
    },
    logout() {
      this.jwt = null;
    },
  },
});

export { useAuthenticationStore };
