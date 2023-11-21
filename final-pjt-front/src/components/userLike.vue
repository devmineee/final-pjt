<template>
    <div>
        <h1>다른 유저가 찜한 콘텐츠</h1> 
        {{ profileId }} 
    </div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
    profileId: Number,
})
const like_movies = ref([])

const getLikeMovies = function(){
    axios({
            url: `${store.API_URL}/accounts/${profileId.value}/like_movies/`,
            method:'get',
            headers: {  // token이 필요하지 않다고 하심???이유??
                Authorization: `Token ${store.token}`
            }
        })
        .then((res)=>{
            console.log(res.data)
            like_movies.value = res.data.like_movies
        })
        .catch(err=>{
            console.log(err)
        })
}
</script>

<style scoped>

</style>