<template>
  <div 
    class="tab-pane fade" :id="area.name"
    role="tabpanel" :aria-labelledby="area.name"
    tabindex="0">
      <h1>{{ area.name }}</h1>
      <MovieHomeAreaContentCountry 
      v-for="country in countries"
      :key="country.id"
      :country-name="country.korean_name"
      :country-code="country.iso_3166_1"
      :country-id="country.id"/>
  </div>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue';
import MovieHomeAreaContentCountry from './MovieHomeAreaContentCountry.vue';
import axios from 'axios'

const props = defineProps({
  area:Object
})

const countries = ref()
const API_URL = 'http://127.0.0.1:8000'

const getCountryByArea = function (area_id) {
    axios({
      method:'get',
      url : `${API_URL}/api/v1/movies/area/${area_id}`,
    })
    .then((res)=>{
      countries.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  onBeforeMount(()=> {
    getCountryByArea(props.area.id)
  })

</script>

<style scoped>

</style>