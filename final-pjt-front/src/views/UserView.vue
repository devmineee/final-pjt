<template>
    <div>
        <h1>UserView</h1>
        <h2>{{ username }}님의 프로필</h2>
        <p>
            following: <span id="followings-count">{{  followingsCount }}</span> / followers:<span id="followers-count">{{ followerCount }}</span>
        </p>

        <form v-if="store.UserId != profileId" @submit.prevent="follow">
            <input v-if="isFollowing" type="submit" value="UnFollow">
            <input v-else type="submit" value="Follow">
        </form>

        <template  v-if="!isSameUser" >
            <h3>{{ username }}님이 찜한 영화</h3>
            <userLike/>
        </template>
        
        <h3>팔로잉</h3>
        <ol>
            <li v-for="following in followings" @click="goAnotherProfile(following.id)" >{{ following.username }}/{{ following.id }}</li>
        </ol>

        <h2> 현재 로그인된 유저: pk: {{ store.UserId }}, username:{{ store.UserName }} </h2> 
        <!-- <button @click="goHome">홈으로!</button> -->
        
    </div>
</template>

<script setup>
    import userLike from '@/components/userLike.vue'
    import { useAccountStore } from '@/stores/auth_movie'
    import { ref, computed, watch, onMounted } from 'vue' 
    import axios from 'axios'
    import { useRoute,useRouter,onBeforeRouteUpdate} from 'vue-router'; 

    
    const store = useAccountStore()
    const route = useRoute()

   
    const profileId = ref(route.params.id) 
    const username = ref(null)
    const isFollowing = ref(false)
    const followingsCount = ref(null)
    const followerCount = ref(null)
    const followings = ref([])
    const followers = ref([])

    const isSameUser= computed(()=>{
        return profileId.value == store.UserId ? true : false 
    })

    //프로그래밍 방식 네비게이션
    const router = useRouter()
//     const goHome = function(){
//       router.push({ name : 'home' })
//     }
    

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