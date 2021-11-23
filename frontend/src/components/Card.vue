<template>
    <b-card
        title="음원 파일 업로드"
        :img-src="require('../assets/img.jpg')"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 276px;"
        class="text-center shadow d-flex h-100"
    >
        <b-card-text>
        당신이 지금 듣는 음악이 어떤 장르인지 궁금하신가요? 아래 버튼을 눌러 파일을 업로드하고, 장르를 분석해 보세요!
        </b-card-text>
        <label for="formFile">음원 파일(.mp3)를 선택해주세요</label>
        <input class="form-control" type="file" id="formFile" @change="imageUpload" accept=".mp3, .wav, .ogg"/>
    </b-card>
</template>
<script>
export default {
    props:["clicked"],
    name:"card",
    data(){
        return {
            imageUpload:this.clicked,
        };
    },
};
</script>
