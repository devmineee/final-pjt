<template>
  <ul class="nav nav-pills mb-3 justify-content-center" id="pills-tab" role="tablist">
    <MovieHomeAreaButton 
      v-for="area in areas"
      :key="area.id"
      :area="area"
      />
  </ul>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie.js'
import MovieHomeAreaButton from '@/components/Movies/MovieHomeAreaButton.vue'
const store = useMovieStore()
const areas = ref([])
areas.value = store.areas
</script>

<style scoped>

</style>