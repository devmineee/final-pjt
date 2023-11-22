<template>
  <div>
    <h1>{{ username }}님의 프로필</h1>
    <ProfileMovieLike />
    <ProfileFollow />

  </div>
</template>

<script setup>
import ProfileMovieLike from '@/components/Accounts/ProfileMovieLike.vue'
import ProfileFollow from '@/components/Accounts/ProfileFollow.vue'

import { useAccountStore } from '@/stores/auth_movie'
import { ref, onMounted } from 'vue' 
import axios from 'axios'
import { useRoute,onBeforeRouteUpdate} from 'vue-router'; 


const accountStore = useAccountStore()
const route = useRoute()

const profileId = ref(route.params.id) 
const username = ref(null)

// const isSameUser= computed(()=>{
//     return profileId.value == accountStore.UserId ? true : false 
// })


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

</script>

<style scoped>

</style>