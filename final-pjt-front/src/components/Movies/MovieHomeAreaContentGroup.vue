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
])
areas.value = store.areas
</script>

<style scoped>

</style>