<template>
  <div>
    Login
    <form @submit.prevent="logIn">
      <label for="id">ID: </label>
      <input type="text" id="id" v-model.trim = 'username'>
      <label for="password">Password: </label>
      <input type="password" id="password" v-model.trim="password">
      <input type="submit" value="Log In">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/auth_movie';

  const store = useAccountStore()
  const username = ref(null)
  const password = ref(null)

  const logIn = function(){
    const payload = {
      username: username.value,
      password: password.value,
    }
    store.logIn(payload)
  }
</script>

<style scoped>

</style>