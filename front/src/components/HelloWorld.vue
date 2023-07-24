<script setup>




</script>

<template>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  <div class="row">
    <ul class="list-group"> <h1>Nombres</h1>
      <li class="list-group-item" v-for="name in names" :key="name.id">{{ name.name }} is {{ name.age }} years old</li>
    </ul>
  </div>


</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data() {
    return{
      names: []
    }
  },
  mounted(){
    axios.get('http://127.0.0.1:8000/api/v1/nombres')
    .then(response => {
      this.names = response.data
    })
    .then((response) => console.log(response))
  }
}

</script>

<style scoped>

</style>
