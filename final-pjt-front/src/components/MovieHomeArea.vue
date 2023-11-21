<template>
  <div>
    <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
      <MovieHomeAreaButton 
        v-for="area in areas"
        :key="area.id"
        :area="area"
        />
    </ul>

    <div class="tab-content" id="pills-tabContent">
      <MovieHomeAreaContent
      v-for="area in areas"
      :key="area.id"
      :area="area"/>
    </div>

  </div>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue';
import { useMovieStore } from '@/stores/movie.js'
import MovieHomeAreaButton from '@/components/MovieHomeAreaButton.vue';
import MovieHomeAreaContent from '@/components/MovieHomeAreaContent.vue'


// store 에서 area 정보 가져오기
// 해당 View가 onmount 될 때 실행
const store = useMovieStore()
const areas = ref([])

onBeforeMount(()=> {
  store.getAreas()
  areas.value = store.areas
})

</script>

<style scoped>

</style>