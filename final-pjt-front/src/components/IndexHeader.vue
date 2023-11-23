<template>
  <div>
    <nav class="navbar navbar-dark bg-black">
    <div
      class="container-fluid">
      <img @click.prevent="goMovieHome" src="@/assets/TRIPFLIX_CROP.png" alt="logo" height="100">
    </div>

    <!-- <div v-else>
      <RouterLink :to ="{name:'SignUpView'}" >
        <font-awesome-icon icon="fa-solid fa-right-to-bracket" size="2xl" style="color: #ffffff;" class="m-4"/>
      </RouterLink>|
      <RouterLink :to ="{name:'LogInView'}" > LogIn   </RouterLink>|
    </div> -->
  </nav>
  </div>
</template>

<script setup>

</script>

<style scoped>

</style>