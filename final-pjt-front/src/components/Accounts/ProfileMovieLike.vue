<template  v-if="!isSameUser" >
    <div class="p-3 mb-3 bg-secondary-subtle text-emphasis-secondary">
        <h3>{{ username }}님이 찜한 콘텐츠</h3>
        <userLike :username="username" :profileId="profileId" />
        <div class="d-flex justify-content-end">
            <button @click="goHome" type="button" class=" me-3 btn btn-dark">홈으로!</button>
            <!-- <button @click="goHome">홈으로!</button> -->
        </div>
    </div>
</template>


<script setup>
  import userLike from '@/components/Accounts/userLike.vue'
  import { useAccountStore } from '@/stores/auth_movie'
  
  import { ref, computed, onMounted } from 'vue' 
  import axios from 'axios'
  import { useRoute, useRouter, onBeforeRouteUpdate} from 'vue-router'; 


  const accountStore = useAccountStore()
  const route = useRoute()
  const router = useRouter()
  const profileId = ref(route.params.id) 
  const username = ref(null)

  const isSameUser= computed(()=>{
      return profileId.value == accountStore.UserId ? true : false 
  })


  const getCustomUserInfo = function(){
      axios({
          url: `${accountStore.API_URL}/accounts/${profileId.value}/profile/`,
          method:'get',
          headers: {  
              Authorization: `Token ${accountStore.token}`
          }
      })
      .then((res)=>{
          console.log(res.data)
          username.value = res.data.username
      })
      .catch(err=>{
          console.log(err)
      })
  }
  onMounted(()=>{
    accountStore.getCurrentUserInfo()
      getCustomUserInfo()
  })

  onBeforeRouteUpdate((to,from) => {
      profileId.value = to.params.id
      getCustomUserInfo()
  })

  const goHome = function(){
        router.push({name:'MovieHomeView'})
    }
</script>

<style scoped>

</style>