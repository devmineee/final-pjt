<template>
    <div class="row">
        <div class="mb-4">
            <div class="col d-inline-flex" v-for="country in movie?.countries">
                <h1>{{ country?.korean_name}}</h1>
            </div>
            <h1 class="col d-inline-flex">의 영화</h1>
        </div>
        <img class="col-4" :src="`https://image.tmdb.org/t/p/w500${movie?.poster_path}`" alt="" >
        <div class="col-8 px-5">
            <div id="movietitle">
                <h1 class=" fw-bold text-body-emphasis">{{ movie?.title }}</h1>
            </div>
            <hr>
                <div class="align-items-center">
                    <h4 class="col d-inline-flex me-5">개봉일 : {{ movie?.release_date }}</h4>
                    <h4 class="col d-inline-flex me-3">평점 :</h4>
                    <div class="col d-inline-flex me-4">
                    <font-awesome-icon v-for="n in scoreFloor" id="solidstar" icon="fa-solid fa-star" size="lg" style="color: #ffdd00;"  />
                    <font-awesome-icon v-if="isHalf" id="halfstar" icon="fa-solid fa-star-half-stroke" size="lg" style="color: #ffdd00;"  />
                    <font-awesome-icon v-else id="regularstar" icon="fa-regular fa-star" size="lg" style="color: #ffdd00;"  />
                    <font-awesome-icon v-for="n in leftStar" id="regularstar" icon="fa-regular fa-star" size="lg" style="color: #ffdd00;"  />
                    </div>
                
                        <h4 class="col d-inline-flex me-3">장르 :</h4>
                        <div class="col d-inline-flex">
                            <button v-for="genre in movie?.genres" type="button" class="btn btn-outline-secondary me-3">{{genre.name}}</button>
                        </div>

               
                </div>
            <hr>
            <div>
                <p class="lead">{{ movie?.overview }}</p>
            </div>
            <hr>
            
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
const route = useRoute()
const API_URL = 'http://127.0.0.1:8000'
const movieId = route.params.id
const movie = ref(null)
const scoreFloor = ref()
const isHalf = ref()
const leftStar = ref()


const getDetail = function () {
    axios({
    method:'get',
    url : `${API_URL}/api/v1/movies/detail/${movieId}`,
    })
    .then((res)=>{

        movie.value = res.data
        console.log(movie.value)
        scoreFloor.value = Math.floor(movie.value.vote_average/2)

        if (movie.value.vote_average - scoreFloor.value <= 0.5 ) {
            isHalf.value = false
            leftStar.value = 5-scoreFloor.value
        }
        else {
            isHalf.value = true
            leftStar.value = 5-scoreFloor.value-1
        }

        
    })
    .catch((err)=>{
    console.log(err)
    })
}

onMounted(()=>{
    getDetail()
})

</script>

<style scoped>
h1 {
    font-family: serif;
}
</style>


