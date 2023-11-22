<template>
  <div class="bg-dark-subtle" v-show="movies">

    <div class="m-4">
      <h1 class="text-white py-4">{{countryName}}의 영화
        <button>더보기</button>
      </h1>
      <hr>
      <div class="row row-cols-2 row-cols-lg-3 row-cols-xxl-4">
      <MovieCard v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>


    </div>

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