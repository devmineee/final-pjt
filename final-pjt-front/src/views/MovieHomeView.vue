<template>
  <div>
    <NavBar />
    <MovieHomeMain />
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { useMovieStore } from '@/stores/movie.js'
  import NavBar from '@/components/NavBar.vue'
  import MovieHomeMain from '@/components/Movies/MovieHomeMain.vue'

  const store = useMovieStore()

  onMounted(()=>{
    store.getAreas()
  })

</script>

<style scoped>

</style>