<template>
  <div class="mx-4">
    <h1 class="text-white"></h1>
      <MovieHomeCountry
      v-for="country in countries"
      :key="country.id"
      :country-name="country.korean_name"
      :country-id="country.id"/>
  </div>
</template>

<script setup>
import MovieHomeCountry from '@/components/Movies/MovieHomeCountry.vue'
import { ref, onMounted } from 'vue';
import axios from 'axios'

const countries = ref()
const API_URL = 'http://127.0.0.1:8000'

const getCountryByArea = function () {
    axios({
      method:'get',
      // 2번 미국으로 기본 설정
      url : `${API_URL}/api/v1/movies/area/2`,
    })
    .then((res)=>{
      countries.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  onMounted(()=> {
    getCountryByArea()
  })
</script>

<style scoped>

</style>