<template>
  <div @click="goDetail" class="col my-3">
    <div class="card h-100">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body bg-body-secondary">
        <h5 class="card-title">{{movie.title}}</h5>
        <p class="card-text">{{ shortOverview }}</p>
          <div class="d-flex justify-content-end">
            <font-awesome-icon v-if="!isLiked" @click.stop="movieLike(movie.id)" icon="fa-regular fa-heart" size="2xl" style="color: #e90707;" />
            <font-awesome-icon v-if="isLiked" @click.stop="movieLike(movie.id)" icon="fa-solid fa-heart" bounce size="2xl" style="color: #e90707;" />
          </div>
      </div>
    </div>
  </div>
</template>

<script setup>  
import { ref, computed, onMounted } from 'vue'
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
    isLiked.value = res.data.is_liked
  })
  .catch((err)=>{
    console.log(err)
  })
}

const getisLikedInfo = function(moviePk){
  axios({
    method:'get',
    url : `${movieStore.API_URL}/api/v1/movies/${moviePk}/likes/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
  .then((res)=>{
    isLiked.value = res.data.is_liked
  })
  .catch((err)=>{
    console.log(err)
  })
}

onMounted(()=>{
  getisLikedInfo(props.movie.id)
})

 

</script>

<style scoped>

</style>