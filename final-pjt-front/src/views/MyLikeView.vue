<template>
    <div>
        <h1>{{ store.UserName }}님이 찜한 콘텐츠</h1>
    </div>
</template>

<script setup>
    import { useCounterStore } from '@/stores/counter';
    const store = useCounterStore()
</script>

<style scoped>

</style>