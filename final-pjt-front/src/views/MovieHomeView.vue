<template>
  <div>
    <!-- 기본적으로 추천해줄 나라들 -->
    <!-- 나라들 2.. -->
    <!-- 나라들 3.. -->
    <div v-for="country in three_country">
      <h1>{{ country }}의 콘텐츠</h1>
      <MovieHomeAreaContentCountry />
    </div>
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
  import MovieHomeAreaContentCountry from '../components/MovieHomeAreaContentCountry.vue';

  const three_country = ["일본","프랑스","인도"]
  


</script>

<style scoped>

</style>