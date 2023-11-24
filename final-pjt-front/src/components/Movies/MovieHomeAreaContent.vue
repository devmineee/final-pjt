<template>
  <div 
    class="tab-pane fade" :id="area.name"
    role="tabpanel" :aria-labelledby="area.name"
    tabindex="0">
      <MovieHomeCountry
      v-for="country in countries"
      :key="country.id"
      :country-name="country.korean_name"
      :country-id="country.id"/>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MovieHomeCountry from '@/components/Movies/MovieHomeCountry.vue'
import axios from 'axios'

const props = defineProps({
  area:Object
})

const countries = ref(null)
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

  onMounted(()=> {
    getCountryByArea(props.area.id)
  })

</script>

<style scoped>

</style>