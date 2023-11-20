<template>
  <button
      class="btn btn-info" 
      data-bs-toggle="collapse" :data-bs-target="`#${area.name}`"
      aria-expanded="false" :aria-controls="`#${area.name}`">
      {{ area.name }}
  </button>
</template>

<script setup>
const props = defineProps({
  area:Object
})
</script>

<style scoped>

</style>