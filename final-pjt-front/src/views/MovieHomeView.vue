<template>
  <div>
    <!-- 기본적으로 추천해줄 나라들 -->
    <!-- 나라들 2.. -->
    <!-- 나라들 3.. -->
    <div v-for="country in three_country">
      <MovieHomeAreaContentCountry />
    </div>

    <div>
      <MovieHomeArea />
    </div>

  </div>
</template>

<script setup>
  import MovieHomeArea from '@/components/MovieHomeArea.vue';
  import MovieHomeAreaContentCountry from '../components/MovieHomeAreaContentCountry.vue';
  const three_country = ["일본","프랑스","인도"]
</script>

<style scoped>

</style>