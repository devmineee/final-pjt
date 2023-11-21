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
import MovieCard from './MovieCard.vue';
import axios from 'axios'
import { ref, onBeforeMount } from 'vue';
const props = defineProps({
  countryName:String,
  countryCode:String,
  countryId:Number,
})

const arr = [0,1,2,3,4]

const movies = ref()
const API_URL = 'http://127.0.0.1:8000'


const getMovieListOne = function (country_code) {
    axios({
      method:'get',
      url : `${API_URL}/api/v1/movies/get_movie_by_country/${country_code}/1`,
    })
    .then((res)=>{
      movies.value = res.data.results
      console.log(movies.value)
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  onBeforeMount(()=> {
    getMovieListOne(props.countryCode)
  })


</script>

<style scoped>

</style>