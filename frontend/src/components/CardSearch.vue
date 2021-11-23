<template>
    <b-card
        title="유튜브 동영상에서"
        :img-src="require('../assets/img2.jpg')"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 276px;"
        class="text-center shadow d-flex h-100"
    >
        <b-card-text>
        유튜브 동영상으로부터 음악 장르를 분석할 수도 있습니다!
        </b-card-text>
        <label for="formFile">뮤직비디오 id를 입력해주세요</label>
        <b-form-input class="mb-3" v-model="v_id" placeholder="Enter V_id"></b-form-input>
        <b-button class="float-end" type="submit" variant="outline-primary" @click="search(v_id)">Button</b-button>

    </b-card>
</template>
<script>
export default {
    props:["clicked"],
    name:"cardsearch",
    data(){
        return {
            v_id:"",
            search:this.clicked,
        };
    },
    methods:{
    }
};
</script>
