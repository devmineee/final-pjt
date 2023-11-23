<template>
  <div id="carouselExampleAutoplaying" class="carousel slide text-center" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <div class="carousel-caption">
          <h1>지금 가고 싶은 여행지가 있나요??</h1>
          <h1>영화로 먼저 여행하세요.  </h1>
          <p class="fs-3 font-weight-bold">"Tripflix 와 함께"</p>
        </div>
        <img src="@/assets/index_carousel1.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="@/assets/index_carousel2.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption">
          <h1>인생 여행지를 찾으시나요?</h1>
          <h1>영화로 먼저 느껴보는 것은 어떨까요? </h1>
          <p class="fs-3 font-weight-bold">"Tripflix 와 함께"</p>
        </div>
      </div>
      <div class="carousel-item ">
        <img src="@/assets/index_carousel3.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption text-center">
          <h1>그곳의 사람들의 문화는 어떨까요?</h1>
          <h1> 영화를 통해 알아봐요</h1>
          <p class="fs-3 font-weight-bold">"Tripflix 와 함께"</p>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>

    <!-- 투명한 백그라운드를 가진 div 요소 추가 -->
      <div class="d-flex overlay-background  justify-content-center ">
        <!-- 버튼을 이미지 위에 배치 -->
        <div class="overlay-buttons  d-flex flex-column  justify-content-center">
          <button id="login-button" @click="goLogIn" class="m-3 btn btn-primary">Login</button>
          <button id="signup-button" @click="goSignUp" class="m-3 btn btn-secondary">Sign Up</button>
        </div>
      </div>
    </div>
</template>


<script setup>
  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goLogIn = function(){
    router.push({name:'LogInView'})
  }

  const goSignUp = function(){
    router.push({name:'SignUpView'})
  }
</script>


<style>
.overlay-background {
  position: absolute;
  top: 35%; /* 백그라운드를 이미지 중앙으로 위치시키려면 조절 */
  left: 50%; /* 백그라운드를 이미지 중앙으로 위치시키려면 조절 */
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.3); /* 투명한 검정색 백그라운드, 마지막 값 (0.3)을 조절하여 투명도 조절 가능 */
  padding: 20px; /* 원하는 패딩 값으로 조절 */
  border-radius: 10px; /* 원하는 테두리 반경 값으로 조절 */
}

.carousel-caption{
  position: absolute;
  top: 10%; /* 백그라운드를 이미지 중앙으로 위치시키려면 조절 */
  left: 15%; /* 백그라운드를 이미지 중앙으로 위치시키려면 조절 */
} 

#login-button {
  height:60px;
  width:300px;
}

#signup-button {
  height:60px;
  width:300px;
}

</style>