<template>
  <router-view />
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios';
if (location.port != 7000) {
  axios.defaults.baseURL = 'http://localhost:7000'
}

export default defineComponent({
  name: 'App'
})
</script>
