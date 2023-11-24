<template>
  <div class="mx-4">
    <h1 class="text-white pt-4">오늘은 이런 영화들 어떠세요?</h1>
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

const countries = ref([])
const API_URL = 'http://127.0.0.1:8000'


const getCountryByArea = function () {
    function getRandomNumber() {
      // Math.random()은 0 이상 1 미만의 난수를 생성
      // * 4를 하면 0 이상 4 미만의 난수를 생성
      // Math.floor()를 사용하여 소수점 이하를 버림
      // 따라서 0, 1, 2, 3 중 하나의 정수를 얻게 됨
      return Math.floor(Math.random() * 4) + 1;
  }

// 함수 호출하여 랜덤 숫자 얻기
  const randomNumber = getRandomNumber();

    axios({
      method:'get',
      // 2번 미국으로 기본 설정
      url : `${API_URL}/api/v1/movies/area/${randomNumber}`,
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