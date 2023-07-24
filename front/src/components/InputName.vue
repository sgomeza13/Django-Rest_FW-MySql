<script setup>
import {ref} from 'vue'   
</script>
<template>
    <form @submit.prevent="submitName">

        <h1>Ingresa Tu Nombre</h1>
        <input id="name" v-model="postData.name" class="form-control form-control-lg" type="text">


        <h1>Ingresa Tu Edad</h1>
        <input id="age" v-model.number="postData.age" class="form-control form-control-lg" type="number">
    <button>Submit Data</button>
    </form>
</template>

<script>
import axios from 'axios'


export default {
    data(){
        return {
            postData: {
                name: '',
                age: 0,
            }
        }
    },
    methods: {
        async submitName(){
        axios.post('http://127.0.0.1:8000/api/v1/nombres/',this.postData)
        .then((response) => window.location.reload())
        
    }
    }
}


</script>