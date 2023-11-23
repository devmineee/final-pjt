<template>
  <div>
  디테일 메인
  <CountryDetailMovieList />
    <div class="background-container" :style="{ background: getGradient() }">
      <img :src="getImage()" class="d-block w-100" alt="...">
    </div>

  </div>
</template>

<script setup>
  import CountryDetailMovieList from '@/components/Movies/CountryDetailMovieList.vue'
  import { ref , onMounted } from 'vue'
  import { useRoute } from 'vue-router';

  const route= useRoute()

  const countryName = route.params.country
  const imageRoute = ref(null)

  const getGradient = function () {
    // 그라데이션 스타일 설정
    return `linear-gradient(to bottom, #3498db, #2c3e50)`;
  };

  const getImage = function(){
    if (countryName==="프랑스") {
      imageRoute.value = "/src/assets/france.jpg"
      return imageRoute.value
    } else {
      return ""
    }
  }
onMounted(()=>{
  getImage()
})
</script>
  
<style scoped>
  .background-container {
    position: relative;
    height: 100px; /* 원하는 높이로 조절 */
  }
</style>