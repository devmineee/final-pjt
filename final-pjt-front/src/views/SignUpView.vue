<template>
  <div>
    <div>
      <img src="@/assets/signup.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="overlay-background text-white w-25">
    <div>
    <p>Tripflix 회원가입</p>
    <h1 class="text-center m-3">Tripflix</h1>
    <div>
    <p class="text-center">회원정보를 입력해주세요</p>  
    <div class="d-flex justify-content-center">
      <form class="d-flex flex-column" @submit.prevent="signUp">
        <div class="row mb-3">
          <!-- <label for="id" class="col-sm-2 col-form-label">ID</label> -->
          <div class="w-100 col-sm-10">
            <input type="text" id='id' placeholder=" 아이디" v-model.trim="username" class="form-control">
          </div>
        </div>
        <div class="row mb-3">
          <!-- <label for="password1" class="col-sm-2 col-form-label">Password</label> -->
          <div class="w-100 col-sm-10">
            <input type="password" class="form-control" placeholder="비밀번호" id="password1" v-model.trim="password1">
          </div>
        </div>
        <div class="row mb-3">
          <!-- <label for="password2" class="col-sm-2 col-form-label">Password 확인</label> -->
          <div class="w-100 col-sm-10">
            <input type="password" class="form-control" placeholder="비밀번호 확인" id="password2" v-model.trim="password2">
          </div>
        </div>
        <div class="d-flex justify-content-center">
          <button type="submit" class="btn btn-primary ">가입하기</button>
        </div>
      </form>
      </div>
    </div>
    </div>
  </div>
  </div>

</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/auth_movie'  

  const store = useAccountStore()

  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)

  const signUp = function(){
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
    }
    store.signUp(payload)
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