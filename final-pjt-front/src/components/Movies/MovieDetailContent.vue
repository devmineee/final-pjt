<template>
    <div class="px-4 py-5 my-5 text-center">
        <img class="d-block mx-auto mb-4" :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" alt="" width="720">
        <h1 class="display-5 fw-bold text-body-emphasis">{{ movie.title }}</h1>
        <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">{{ movie.overview }}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
const route = useRoute()
const API_URL = 'http://127.0.0.1:8000'
const movieId = route.params.id
const movie = ref()

const getDetail = function () {
    axios({
    method:'get',
    url : `${API_URL}/api/v1/movies/detail/${movieId}`,
    })
    .then((res)=>{
        movie.value = res.data
        console.log(movie.value)
    })
    .catch((err)=>{
    console.log(err)
    })
}
onMounted(()=>{
    getDetail()
})

</script>

<style scoped>

</style>


