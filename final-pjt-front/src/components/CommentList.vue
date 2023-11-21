<template>
    <div>
        댓글
        <ul>
            <li v-for="comment in comments">{{ comment.content }}</li>
        </ul>
        <form @submit.prevent="commentCreate">
            <input type="text" id="comment" placeholder="영화에 대한 댓글을 입력하세요" v-model.trim="content">
            <input type="submit"  value="등록">
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie';
const props = defineProps(['movieId'])

const movieStore = useMovieStore();
const comments = ref(null)

const getComments = function(){
    axios({
      method:'get',
      url: `${movieStore.API_URL}/api/v1/movies/${props.movieId}/comments/`,
    })
    .then ((res)=>{
      console.log(res)
      comments.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }
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
        console.log(res.data)
        getComments()
    })
    .catch((err) => {
        console.log(err);
    })
}
onMounted(()=>{
    getComments()
})
</script>

<style scoped>

</style>