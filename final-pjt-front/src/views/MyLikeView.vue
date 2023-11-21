<template>
    <div>
        <h1>{{ store.UserName }}님이 찜한 콘텐츠</h1>
    </div>
</template>

<script setup>
    import { useAccountStore } from '@/stores/auth_movie.js'
    const store = useAccountStore()
</script>

<style scoped>

</style>