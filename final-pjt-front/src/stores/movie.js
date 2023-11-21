import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios  from 'axios'

export const useMovieStore = defineStore('movie', () => {
  
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const areas = ref([])
  const countries = ref('')

  // 다음 두 함수는 초기에 받아오는 것이 좋을 듯 하다
  // Django 에서 지역 정보를 받아오는 함수
  const getAreas = function () {

    axios({
      method:'get',
      url : `${API_URL}/api/v1/movies/area/`,
    })
    .then((res)=>{
      // areas 정보 받아오기
      areas.value = res.data

    })
    .catch((err)=>{
      console.log(err)
    })
  }

  

  
  
  return { getAreas, areas, countries }
},{persist:true})