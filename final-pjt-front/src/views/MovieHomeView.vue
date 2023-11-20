<template>
  <div>
    <!-- 기본적으로 추천해줄 나라들 -->
    <!-- 나라들 2.. -->
    <!-- 나라들 3.. -->
    <!-- 권역들 모여있는 버튼 -->
    <!-- 권역 안에 나라들 모음 -->
    
    <div>
      <MovieHomeArea />
    </div>
  
    <div v-for="area in areas" 
      class="collapse" :id="area.name">
      <div class="card card-body">
        {{ area.name }} 의 영역입니다.
      </div>
    </div>

  </div>
</template>

<script setup>
  import MovieCountryView from './MovieCountryView.vue';
  import MovieAreaView from '@/views/MovieAreaView.vue'
  import { useCounterStore } from '@/stores/counter.js'
  import { onMounted, ref } from 'vue';
  import MovieHomeAreaButton from '../components/MovieHomeAreaButton.vue';
  import MovieHomeArea from '@/components/MovieHomeArea.vue';

  
  


</script>

<style scoped>

</style>