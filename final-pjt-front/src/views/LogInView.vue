<template>
  <div>
    <div class="background-container">
      <img src="@/assets/login2.jpg" class="d-block w-100" alt="...">
    </div>
    
    <div class="overlay-background text-white w-25">
    <p>Tripflix 로그인</p>
    <h1 class="text-center m-3">Tripflix</h1>

    <div class="d-flex justify-content-center m-4">
      <form class="d-flex flex-column" @submit.prevent="logIn">
        <div class="row mb-3">
          <div class="w-100 col-sm-10">
            <input type="text" id='id' placeholder=" 아이디" v-model.trim="username" class="form-control">
          </div>
        </div>
        <div class="row mb-3">
          <div class="w-100 col-sm-10">
            <input type="password" class="form-control" placeholder="비밀번호" id="password" v-model.trim="password">
          </div>
        </div>
        <div class="d-flex justify-content-center">
          <button type="submit" class="btn btn-primary ">로그인하기</button>
        </div>
      </form>
      </div>
      <div class="d-flex flex-column align-items-center m-5">
        <p>Tripflix가 처음이신가요?</p>
        <button type="button" class="btn btn-outline-dark"  @click="goSignUp">Tripflix 회원가입하기</button>
      </div>
    </div>
    </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/auth_movie';
  import { useRouter } from 'vue-router';
  
  const router = useRouter()
  const store = useAccountStore()
  const username = ref(null)
  const password = ref(null)

  const logIn = function(){
    const payload = {
      username: username.value,
      password: password.value,
    }
    store.logIn(payload)
  }

  const goSignUp = function(){
    router.push({name:'SignUpView'})
  }
</script>

<style scoped>
  .overlay-background {
  position: absolute;
  top: 50%; /* 백그라운드를 이미지 중앙으로 위치시키려면 조절 */
  left: 50%; /* 백그라운드를 이미지 중앙으로 위치시키려면 조절 */
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.2); /* 투명한 검정색 백그라운드, 마지막 값 (0.3)을 조절하여 투명도 조절 가능 */
  padding: 20px; /* 원하는 패딩 값으로 조절 */
  border-radius: 10px; /* 원하는 테두리 반경 값으로 조절 */
}
</style>