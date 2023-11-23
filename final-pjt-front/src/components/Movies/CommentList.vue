<template>
    <div class="p-3 my-4 bg-secondary-subtle text-emphasis-secondary">
        <h4 class="m-3">댓글</h4>
        <div class="m-2" v-for="comment in comments">
            <div class="d-flex flex-row mb-3">
                <p class="p-3 mb-2 bg-body-secondary">{{ comment.content }}</p>
                <button type="button" class="btn btn-outline-dark" @click="deleteComment(comment.id)">삭제</button>
                <!-- <button @click="deleteComment(comment.id)">삭제</button> -->
            </div>
        </div>

        <div class="container mt-1">
            <form @submit.prevent="commentCreate">
                <div class="row">
                    <div class="col">
                        <input type="text" class="form-control" id="longInput" placeholder="영화에 대한 댓글을 입력하세요" v-model.trim="content">
                    </div>
                    <div class="col-auto">
                        <input type="submit" value="등록" class="btn btn-primary">
                    </div>
                </div>
            </form>
        </div>

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
  const content = ref("");

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
        content.value=""
    })
    .catch((err) => {
        console.log(err);
    })
}


const deleteComment = function (commentId) {
  axios({
    method:'delete',
    url: `${movieStore.API_URL}/api/v1/movies/${props.movieId}/comments/${commentId}`
  })
    .then(()=>{
      console.log('삭제 성공')
      getComments()
    })
    .catch(()=>{
      console.log('삭제 실패')
    })
}





onMounted(()=>{
    getComments()
})
</script>

<style scoped>

</style>