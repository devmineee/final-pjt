<template>
  <div>
    <h1>메인-배경 넣기</h1>
    <button @click="goLogIn">Login </button>
    <button @click="goSignUp">Sign Up</button>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goLogIn = function(){
    router.push({name:'LogInView'})
  }

  const goSignUp = function(){
    router.push({name:'SignUpView'})
  }
</script>

<style scoped>

</style>