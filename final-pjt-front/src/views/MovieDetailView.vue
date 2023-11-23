<template>
    <div>
        <NavBar />
        <h1>무비 디테일</h1>
        <p>title {{ movie }}</p>
        
        <CommentList :movieId="movieId"/>
    </div>
</template>

<script setup>
import CommentList from '@/components/Movies/CommentList.vue'
import { ref, onMounted} from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
import NavBar from '../components/NavBar.vue';
const route = useRoute()
const API_URL = 'http://127.0.0.1:8000'
const movieId = route.params.id
const movie = ref(null)
const getDetail = function () {
    axios({
    method:'get',
    url : `${API_URL}/api/v1/movies/detail/${movieId}`,
    })
    .then((res)=>{
        movie.value = res.data
        console.log(res.data)
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