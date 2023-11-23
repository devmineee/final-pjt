<template>
  <div>
    <div>
      <img :src="getImage()" class="d-block w-100 "  style="height: 400px;" alt="...">
    </div>
  <CountryDetailMovieList />
  </div>
</template>

<script setup>
  import CountryDetailMovieList from '@/components/Movies/CountryDetailMovieList.vue'
  import { ref , onMounted } from 'vue'
  import { useRoute } from 'vue-router';

  const route= useRoute()

  const countryName = route.params.country
  const imageRoute = ref(null)


  const getImage = function(){
    if (countryName==="스페인") {
      imageRoute.value = "/src/assets/country/spain.jpg"
    } else if(countryName==="프랑스"){
      imageRoute.value = "/src/assets/country/france.jpg"
    } else if(countryName==="일본"){
      imageRoute.value = "/src/assets/country/japan.jpg"
    } else if(countryName==="태국"){
      imageRoute.value = "/src/assets/country/thai.jpg"
    } else if(countryName==="미국"){
      imageRoute.value = "/src/assets/country/america.jpg"
    } else if(countryName==="브라질"){
      imageRoute.value = "/src/assets/country/brazil.jpg"
    } else if(countryName==="러시아"){
      imageRoute.value = "/src/assets/country/russia.jpg"
    } else if(countryName==="인도"){
      imageRoute.value = "/src/assets/country/india.jpg"
    } else if(countryName==="독일"){
      imageRoute.value = "/src/assets/country/germany.jpg"
    } else if(countryName==="멕시코"){
      imageRoute.value = "/src/assets/country/mexico.jpg"
    } else if(countryName==="네덜란드"){
      imageRoute.value = "/src/assets/country/netherland.jpg"
    } else if(countryName==="그리스"){
      imageRoute.value = "/src/assets/country/greece.jpg"
    } else if(countryName==="영국"){
      imageRoute.value = "/src/assets/country/uk.jpg"
    } else if(countryName==="이탈리아"){
      imageRoute.value = "/src/assets/country/italy.jpg"
    } else if(countryName==="홍콩, 중국 특별행정구"){
      imageRoute.value = "/src/assets/country/hongkong.jpg"
    } else if(countryName==="사우디아라비아"){
      imageRoute.value = "/src/assets/country/saudi.jpg"
    } else if(countryName==="터키"){
      imageRoute.value = "/src/assets/country/turkey.jpg"
    }  else if(countryName==="아르헨티나"){
      imageRoute.value = "/src/assets/country/argentina.jpg"
    } else {
      imageRoute.value = ""
    }
    return imageRoute.value
  }
onMounted(()=>{
  getImage()
})
</script>
  
<style scoped>
</style>