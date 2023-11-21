<template>
  <header>
    <nav v-if="store.isLogin">
      <form @submit.prevent="store.logOut" >
        <input type="submit" value="logOut">
      </form>
      <div @click.prevent="goMyLikeView">내가 찜한 콘텐츠</div>
      <div @click.prevent="goUserView">내 프로필 보기</div>
      <!-- <RouterLink :to ="{name:'MyLikeView', params:{id:store?.UserId}}"> 내가 찜한 콘텐츠 </RouterLink>|
      <RouterLink :to="{name:'UserView',params:{id:store?.UserId}}">내 프로필 보기</RouterLink> -->
    </nav>
    <nav v-else>
      <RouterLink :to ="{name:'SignUpView'}" > SignUp   </RouterLink>|
      <RouterLink :to ="{name:'LogInView'}" > LogIn   </RouterLink>|
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { ref } from "vue"
import { RouterView, RouterLink } from 'vue-router'
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

</script>
<style scoped>
</style>