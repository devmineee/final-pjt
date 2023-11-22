<template>
  <nav class="navbar navbar-dark bg-black">
    <div v-if="store.isLogin"
      class="container-fluid">
      <img @click.prevent="goMovieHome" src="@/assets/TRIPFLIX_CROP.png" alt="logo" height="100">
      <div class="d-flex">
        <font-awesome-icon @click.prevent="goUserView" icon="fa-solid fa-user" size="2xl" style="color: #ffffff;" class="m-4"/>
        <font-awesome-icon @click.prevent="goMyLikeView" icon="fa-solid fa-heart" size="2xl" style="color: #ffffff;" class="m-4" />
        <form @click.prevent="store.logOut" >
          <font-awesome-icon icon="fa-solid fa-right-from-bracket" size="2xl" style="color: #ffffff;" class="m-4" />
        </form>
      </div>
    </div>

    <!-- <div v-else>
      <RouterLink :to ="{name:'SignUpView'}" >
        <font-awesome-icon icon="fa-solid fa-right-to-bracket" size="2xl" style="color: #ffffff;" class="m-4"/>
      </RouterLink>|
      <RouterLink :to ="{name:'LogInView'}" > LogIn   </RouterLink>|
    </div> -->
  </nav>
</template>

<script setup>
// import { RouterView, RouterLink } from 'vue-router'
import { useRouter } from "vue-router";
import { useAccountStore } from '@/stores/auth_movie'
const store = useAccountStore()
const router = useRouter()

store.getCurrentUserInfo()

const goMyLikeView = function(){
  router.push({name:'MyLikeView',params:{id:store.UserId}})
}
const goUserView = function(){
  router.push({name:'UserView',params:{id:store.UserId}})
}

const goMovieHome = function(){
  router.push({name:'MovieHomeView'})
}
</script>

<style scoped>
</style>