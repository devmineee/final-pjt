<template>
  <li class="nav-item" role="presentation">
    <button class="nav-link" data-bs-toggle="pill"
    :data-bs-target="`#${area.name}`" type="button" role="tab" 
    :aria-controls="area.name" aria-selected="true">{{ area.name }}</button>
  </li>
</template>

<script setup>
const props = defineProps({
  area:Object
})
</script>

<style scoped>

</style>