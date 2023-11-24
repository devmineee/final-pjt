<template>
  <ul class="tab-content" id="pills-tabContent">
    <MovieHomeAreaContent
    v-for="area in areas"
    :key="area"
    :area="area"/>
  </ul>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie.js'
import MovieHomeAreaContent from '@/components/Movies/MovieHomeAreaContent.vue'
const store = useMovieStore()
const areas = ref([
  {
    "id": 2,
    "name": "서유럽"
  },
  {
      "id": 1,
      "name": "아시아"
  },
    {
        "id": 3,
        "name": "동유럽 및 중동"
    },
    {
        "id": 4,
        "name": "남미 및 북미"
    }
])
</script>

<style scoped>

</style>