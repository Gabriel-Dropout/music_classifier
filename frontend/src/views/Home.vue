<template>
  <div>
    <b-container class="col text-center">
      <transition name="fade" appear>
        <div>
          <p class="h1 mb-2 mt-4">음악 장르 분류기</p>
          <p class="h5 mb-5">Made by 여경민&박성원</p>
        </div>
      </transition>
      <b-row class="row justify-content-center" style="height:420px;">
        <transition name="fade" appear>
          <div class="justify-content-center align-items-center d-flex" style="width:320px">
            <Card v-bind:clicked="imageUpload" />
          </div>
        </transition>

        <transition name="fade" appear>
          <div class="justify-content-center align-items-center d-flex" style="width:320px">
            <CardSearch v-bind:clicked="imageSearch" />
          </div>
        </transition>
      </b-row>

      <transition name="fade" appear>
        <b-img v-show="loading" src="https://c.tenor.com/l6u0sCzYdiwAAAAC/gura-roomba-gawr-gura.gif"></b-img>
      </transition>
    </b-container>
  </div>
</template>

<script>
  import Card from "../components/Card.vue"
  import CardSearch from "../components/CardSearch.vue"

  const axios = require('axios')
  export default {
    data() {
      return {
        loading: false,
      };
    },
    methods: {
      async imageUpload(e) {
        this.loading = true;

        console.log(e.target);
        let formData = new FormData();
        await formData.append('file', e.target.files[0]);
        try {
          let res = await axios.post(process.env.VUE_APP_BACKEND_BASE_URL+'/upload',
            formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }
          );
          this.loading = false;
          alert(res.data);
        } catch (e) {
          this.loading = false;
          console.log("FAILURE!!!");
        }
      },
      async imageSearch(e) {
        this.loading = true;
        try {
          let res = await axios.get(
            process.env.VUE_APP_BACKEND_BASE_URL+'/search?v=' + e
          );
          this.loading = false;
          alert(res['data']);
        } catch (e) {
          this.loading = false;
          console.log("FAILURE!!!");
        }
      },
    },
    components: {
      Card,
      CardSearch,
    }
  };
</script>

<style>
  .fade-enter {
    opacity: 0;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease-out;
  }

  .fade-leave-to {
    opacity: 0;
  }
</style>