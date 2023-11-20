<template>
  <div 
    class="collapse" :id="area.name">
    <div class="card card-body">
      {{ area.name }} 의 영역입니다.
      <MovieHomeAreaContentCountry />
    </div>
  </div>
</template>

<script setup>
import MovieHomeAreaContentCountry from './MovieHomeAreaContentCountry.vue';
const props = defineProps({
  area:Object
})
</script>

<style scoped>

</style>