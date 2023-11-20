<template>
  <div>
    <nav class="d-inline-flex gap-2" >
      <MovieHomeAreaButton 
        v-for="area in areas"
        :key="area.id"
        :area="area"
        @click.prevent="exampleEvent"/>
    </nav>

    <div>
      <MovieHomeAreaContent
      v-for="area in areas"
      :key="area.id"
      :area="area"/>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter.js'
import MovieHomeAreaButton from '@/components/MovieHomeAreaButton.vue';
import MovieHomeAreaContent from '@/components/MovieHomeAreaContent.vue'


// store 에서 area 정보 가져오기
// 해당 View가 onmount 될 때 실행
const store = useCounterStore()
const areas = ref([])

onMounted(()=> {
  store.getAreas()
  areas.value = store.areas
})

</script>

<style scoped>

</style>