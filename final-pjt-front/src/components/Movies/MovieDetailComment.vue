<template>
    <div>
        <CommentList :movieId="movieId"/>
    </div>
</template>

<script setup>
import CommentList from '@/components/Movies/CommentList.vue';
import { useRoute } from 'vue-router';
const route = useRoute()
const movieId = route.params.id
</script>

<style scoped>

</style>

        

i



import CommentList from '@/components/Movies/CommentList.vue'
import CommentCreate from '@/components/Movies/CommentCreate.vue'