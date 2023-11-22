<template>
  <div>
    <h1 class="col">{{countryName}}의 영화</h1>
    <div class="row row-cols-1 row-cols-md-6 g-4">
    <MovieCard v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      />
    </div>
    <button>더보기</button>

  </div>
  
</template>

<script setup>
import MovieCard from '@/components/Movies/MovieCard.vue';
import axios from 'axios'
import { ref, onMounted } from 'vue';
const props = defineProps({
  countryName:String,
  countryId:Number,
})

const movies = ref()
const API_URL = 'http://127.0.0.1:8000'
const getMovieList = function (country_id) {
    axios({
      method:'get',
      url : `${API_URL}/api/v1/movies/country/${country_id}/`,
    })
    .then((res)=>{
      movies.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  onMounted(()=> {
    getMovieList(props.countryId)
  })


</script>

<style scoped>

</style>