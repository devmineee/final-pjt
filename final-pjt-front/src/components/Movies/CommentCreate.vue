<template>
    <div>
        <form @submit.prevent="commentCreate">
            <input type="text" id="comment" placeholder="영화에 대한 댓글을 입력하세요" v-model.trim="content">
            <input type="submit"  value="등록">
        </form>
    </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';
import axios from 'axios';
import { useAccountStore } from '@/stores/auth_movie';
import { useMovieStore } from '@/stores/movie';

const props = defineProps(['movieId']); // Define the prop here

const accountStore = useAccountStore();
const movieStore = useMovieStore();

const content = ref(null);

const commentCreate = function() {
    axios({
        method: 'post',
        url: `${movieStore.API_URL}/api/v1/movies/${props.movieId}/comments/`,
        data: {
            content: content.value,
        }
    })
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err);
    })
}
</script>


<style scoped>

</style>