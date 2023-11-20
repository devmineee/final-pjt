<template>
  <div 
    class="collapse" :id="area.name">
    <div class="card card-body">
      {{ area.name }} 의 영역입니다.
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  area:Object
})
</script>

<style scoped>

</style>