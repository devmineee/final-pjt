<template>
  <li class="nav-item mt-4" role="presentation">
    <button class="nav-link" data-bs-toggle="pill"
    :data-bs-target="`#${area.name}`" type="button" role="tab" 
    >{{ area.name }}</button>
  </li>
</template>

<script setup>
const props = defineProps({
  area:Object
})
</script>

<style scoped>

</style>