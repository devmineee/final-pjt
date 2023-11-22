<template>
  <div class="col">
    <div class="card h-100">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{movie.title}}</h5>
        <p class="card-text">{{ shortOverview }}</p>
        <button @click="goDetail">더 보기</button>
        <button v-if="!isLiked" @click="movieLike(movie.id)">찜 하기</button>
        <button v-if="isLiked" @click="movieLike(movie.id)">찜 해제</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/auth_movie'
import { useMovieStore } from '@/stores/movie';

const router = useRouter()
const accountStore = useAccountStore()
const movieStore = useMovieStore()
const isLiked = ref(false)

const props = defineProps({
  movie:Object,
})

const shortOverview = ref('')
shortOverview.value = props.movie.overview.substring(0,150) + '....'

const goDetail = function(){
  console.log('------------')
  router.push({name:'MovieDetailView', params:{id:props.movie.id}})
}

  
const movieLike = function(moviePk){
  axios({
    method:'post',
    url : `${movieStore.API_URL}/api/v1/movies/${moviePk}/likes/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
  .then((res)=>{
    console.log('like성공')
    console.log(res.data)
    isLiked.value = res.data.is_liked
  })
  .catch((err)=>{
    console.log(err)
  })
}
 

</script>

<style scoped>

</style>