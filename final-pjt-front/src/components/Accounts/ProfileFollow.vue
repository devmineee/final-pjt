<template>
  <div class="p-3 mb-3 bg-secondary-subtle text-emphasis-secondary">
    <div class="mb-3 d-flex justify-content-between ">
        <div class="p-2 fw-bold" >
            <p> following: <span id="followings-count">{{  followingsCount }}</span></p> 
            <p> followers:<span id="followers-count">{{ followerCount }}</span> </p>
        </div>
        <div class="p-2 ">
            <form v-if="store.UserId != profileId" @submit.prevent="follow">
                <input class="btn btn-primary" v-if="isFollowing" type="submit" value="UnFollow">
                <input class="btn btn-primary" v-else type="submit" value="Follow">
            </form>
        </div>
    </div>

    <h4>팔로잉하는 유저</h4>
        <div v-for="following in followings" class="m-2 bg-body-tertiary d-flex justify-content-between">
            <p class="fw-bold">{{ following.username }}</p>
            <button type="button" class="btn btn-secondary" @click="goAnotherProfile(following.id)">Profile</button>
        </div>
    </div>

</template>

<script setup>
    import { useAccountStore } from '@/stores/auth_movie'
    import { ref, computed, watch, onMounted } from 'vue' 
    import axios from 'axios'
    import { useRoute,useRouter,onBeforeRouteUpdate} from 'vue-router'; 

    const store = useAccountStore()
    const route = useRoute()
    const router = useRouter()

    const profileId = ref(route.params.id) 
    const username = ref(null)
    const isFollowing = ref(false)
    const followingsCount = ref(null)
    const followerCount = ref(null)
    const followings = ref([])
    const followers = ref([])


    const getCustomUserInfo = function(){
        axios({
            url: `${store.API_URL}/accounts/${profileId.value}/profile/`,
            method:'get',
            headers: {  // token이 필요하지 않다고 하심???이유??
                Authorization: `Token ${store.token}`
            }
        })
        .then((res)=>{
            console.log(res.data)
            username.value = res.data.username
            followingsCount.value = res.data.followings_count
            followerCount.value = res.data.followers_count
            followings.value = res.data.followings
            followers.value = res.data.followers
        })
        .catch(err=>{
            console.log(err)
        })
    }
    onMounted(()=>{
        store.getCurrentUserInfo()
        getCustomUserInfo()
    })
    
    watch(() => followers,(newValue,oldValue)=>{
        const ids = newValue.value.map(item => item.id)
        isFollowing.value= ids.includes(store.UserId) ? true : false
        },{deep:true})

        
    const follow = function(){
        axios({
            url: `${store.API_URL}/accounts/${profileId.value}/follow/`,
            method:'post',
            headers: {
                Authorization: `Token ${store.token}`
            }
        })
            .then((res)=>{
                console.log(res)
                followingsCount.value = res.data.followings_count
                followerCount.value = res.data.followers_count
                isFollowing.value = res.data.is_followed //변수명 바꿔야??is_following(가독성)
            })
            .catch((err)=>{
                console.log(err)
            })
    }


    const goAnotherProfile = function(id){
        console.log('test')
        router.push({ name: 'UserView', params: { id: id }})
    }
    onBeforeRouteUpdate((to,from) => {
        profileId.value = to.params.id
        getCustomUserInfo()
    })



</script>

<style scoped>

</style>