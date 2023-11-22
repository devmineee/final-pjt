<template>
    <div v-for="likeMovie in likeMovies">
    <p>title: {{ likeMovie.title }}</p>
    <p>overview: {{ likeMovie.overview }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAccountStore } from '@/stores/auth_movie'
import { useMovieStore } from '@/stores/movie';

const accountStore = useAccountStore()
const movieStore = useMovieStore()

const props = defineProps({
    profileId: Number,
    username: String,
})

const likeMovies = ref(null)

const getLikeMovies = function(){
    axios({
            url: `${movieStore.API_URL}/accounts/${props.profileId}/like_movies/`,
            method:'get',
            headers: {  // token이 필요하지 않다고 하심???이유??
                Authorization: `Token ${accountStore.token}`
            }
        })
        .then((res)=>{
            console.log(res.data)
            likeMovies.value = res.data
        })
        .catch(err=>{
            console.log(err)
        })
}

onMounted(()=>{
    getLikeMovies()
})
</script>

<style scoped>

</style>