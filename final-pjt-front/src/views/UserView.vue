<template>
    <div>
        <h1>UserView</h1>
        <h2>pk: {{ profileId }}유저의 페이지</h2>
        

        <!-- <h2> 현재 로그인된 유저: pk: {{ store.UserId }}, username:{{ store.UserName }} </h2>  -->
        <userLike v-if="!isSameUser" />
        <!-- <button @click="goHome">홈으로!</button> -->
        
    </div>
</template>

<script setup>
    import userLike from '@/components/userLike.vue'
    import { useCounterStore } from '@/stores/counter';
    import { ref, computed } from 'vue'   //이렇게 할 수도 있음
    import { useRoute,useRouter,onBeforeRouteUpdate} from 'vue-router'; 

    const store = useCounterStore()
    const route = useRoute()
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
</script>

<style scoped>

</style>