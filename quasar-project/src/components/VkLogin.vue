<template>
  <div class="q-pa-md q-gutter-sm">
    <div class="avatar-card">
      <q-avatar size="120px" font-size="52px" color="teal" text-color="white" :icon="icon" />
      <div class="name-desc">
        <p class="name"> {{name}} </p>
        <p class="desc"> {{dest}} </p>
        <q-btn color="primary" icon="lock" :disabled="loggedin" @click="openoauth" label="Войти" />
      </div>
    </div>
  </div>
</template>


<script>
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'VkLogin',
  setup() {

    const loggedin = ref(false);
    const name = ref('VKontakte');
    const dest = ref('Вход не выполнен');
    const icon = ref('warning')
    axios.get("api/vk/getMe").then(({data}) => {
      console.log(data.me)
      if (data.me === "true") {
        loggedin.value = true;
        dest.value = "Вход выполнен";
        icon.value = "check"
      }
    })

    function openoauth(){
      window.open("https://oauth.vk.com/authorize?client_id=51790768&display=page&redirect_uri=http://localhost:7000/api/vk/callback&response_type=code&v=5.131", '_blank').focus();
    };
    return {
      openoauth,
      name,
      dest,
      loggedin,
      icon
    }
  }
});
</script>

<style>
.avatar-card {
  display: flex;
  gap: 1rem;
}

.name-desc {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

p {
  margin-bottom: 0%;
}

.name {
  flex: 1 0 auto;
  font-size: 32px;
}

.desc {
  flex: 2 0 auto;
}
</style>

