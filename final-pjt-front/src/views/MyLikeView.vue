<template>
    <div>
        <h1>내가 찜한 영화</h1>
        <div v-for="likeMovie in likeMovies">
            <p>title: {{ likeMovie.title }}</p>
            <p>overview: {{ likeMovie.overview }}</p>
        </div>
    </div>
</template>

<script setup>
    import { ref , onMounted } from 'vue'
    import axios from 'axios'
    import { useAccountStore } from '@/stores/auth_movie'
    import { useMovieStore } from '@/stores/movie';

    const accountStore = useAccountStore()
    const movieStore = useMovieStore()

    const likeMovies = ref(null)

    const getLikeMovies = function(){
        axios({
                url: `${movieStore.API_URL}/accounts/${accountStore.UserId}/like_movies/`,
                method:'get',
                headers: {  // token이 필요하지 않다고 하심???이유??
                    Authorization: `Token ${accountStore.token}`
                }
            })
            .then((res)=>{
                console.log(res.data)
                likeMovies.value = res.data
            })
            .catch(err=>{
                console.log(err)
            })
    }

    onMounted(()=>{
        getLikeMovies()
    })
</script>

<style scoped>

</style>