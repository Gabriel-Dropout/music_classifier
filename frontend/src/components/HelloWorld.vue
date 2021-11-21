<template>
  <div class="hello">
    <div class="room-file-upload-wrapper">
      <div class="room-file-upload-example">
        <div class="room-file-image-example-wrapper">음악 장르 분류기</div>
        <div class="room-file-notice-item">
          음악 파일을 올려주세요!
        </div>
        <div class="room-file-notice-item room-file-upload-button">
          <div class="image-box">
            <label for="file">UPLOAD</label>
            <input type="file" id="file" ref="files" @change="imageUpload" multiple />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios')
  export default {
    data() {
      return {

      };
    },
    methods: {
      imageUpload() {
        //alert(this.$refs.files.files[0].name);
        this.submitFile();
      },
      submitFile() {
        let formData = new FormData();
        formData.append('file', this.$refs.files.files[0]);
        axios.post('http://localhost:5000/upload',
            formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }
          ).then(function (response) {
            alert(response.data);
          })
          .catch(function () {
            console.log('FAILURE!!');
          });
      }
    },
  };
</script>

<style>
  @import 'css.css';
</style>