<template>
    <div>
        <h1>UserView</h1>
        <h2>pk: {{ profileId }}유저의 페이지</h2>
        <p>
            following: <span id="followings-count">{{  followingsCount }}</span> / followers:<span id="followers-count">{{ followerCount }}</span>
        </p>
        <form @submit.prevent="follow">
            <input v-if="isFollowing" type="submit" value="UnFollow">
            <input v-else type="submit" value="Follow">
        </form>

        <h2> 현재 로그인된 유저: pk: {{ store.UserId }}, username:{{ store.UserName }} </h2> 
        <userLike v-if="!isSameUser" />
        <!-- <button @click="goHome">홈으로!</button> -->
        
    </div>
</template>

<script setup>
    import userLike from '@/components/userLike.vue'
    import { useCounterStore } from '@/stores/counter'
    import { ref, computed, watch, onMounted } from 'vue' 
    import axios from 'axios'
    import { useRoute,useRouter,onBeforeRouteUpdate} from 'vue-router'; 

    
    const store = useCounterStore()
    const route = useRoute()
    const isFollowing = ref(false)
    // const newArr = ref([])
    const followingsCount = ref(null)
    const followerCount = ref(null)
    const followings = ref([])
    const followers = ref([])
    const profileId = ref(route.params.id)  //Username으로 받아오는 방법


    const isSameUser= computed(()=>{
        return profileId.value == store.UserId ? true : false 
    })

    //프로그래밍 방식 네비게이션
    const router = useRouter()
//     const goHome = function(){
//       router.push({ name : 'home' })
//     }
    store.getUserInfo()

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
        getCustomUserInfo()
    })
    
    watch(() => followers,(newValue,oldValue)=>{
        console.log('----------------')
        // console.log(oldValue)
        const ids = newValue.value.map(item => item.id)
        isFollowing.value= ids.includes(store.UserId) ? true : false
        // newArr.value = newValue.map(function(obj) {  //이게 안되었던 이유??(강사님은 된 이유...)
        //     return obj.key
        },{deep:true})
    // const isFollowing = computed(()=>{
    //     return newArr.value.includes(store.UserId) ? true : false
    // })
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
                isFollowing.value = res.data.is_followed
            })
            .catch((err)=>{
                console.log(err)
            })
    }
</script>

<style scoped>

</style>