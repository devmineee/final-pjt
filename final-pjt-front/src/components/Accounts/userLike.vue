<template>
    <div class="row row-cols-2 row-cols-lg-3 row-cols-xxl-4 g-4">
        <MovieCard v-for="movie in likeMovies"
        :key="movie.id"
        :movie="movie"
        />
    </div>
</template>

<script setup>
import MovieCard from '@/components/Movies/MovieCard.vue';
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