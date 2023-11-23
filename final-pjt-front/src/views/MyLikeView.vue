<template>
    <div>
        <NavBar />
        <div class="p-3 m-3 bg-secondary-subtle text-emphasis-secondary">
            <h1>내가 찜한 영화</h1>
            <div class="row row-cols-2 row-cols-lg-3 row-cols-xxl-4 g-4">
                <MovieCard v-for="movie in likeMovies"
                :key="movie.id"
                :movie="movie"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
    import MovieCard from '@/components/Movies/MovieCard.vue';
    import NavBar from '@/components/NavBar.vue'
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
                headers: {  
                    Authorization: `Token ${accountStore.token}`
                }
            })
            .then((res)=>{
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