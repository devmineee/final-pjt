<template>
    <div @click="goDetail" class="card">
      <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{movie.title}}</h5>
        <p class="card-text">{{ movie.overview }}</p>
        <button>하트</button>
      </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({
  movie:Object,
})

const router = useRouter()
const goDetail = function(){
  console.log('------------')
  router.push({name:'MovieDetailView', params:{id:props.movie.id}})
}
</script>

<style scoped>

</style>