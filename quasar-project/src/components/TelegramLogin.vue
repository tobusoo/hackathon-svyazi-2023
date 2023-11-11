<template>
  <div class="q-pa-md q-gutter-sm">
    <div class="avatar-card">
      <q-avatar size="120px" font-size="52px" color="teal" text-color="white" :icon="icon" />
      <div class="name-desc">
        <p class="name"> {{name}} </p>
        <p class="desc"> {{dest}} </p>
        <q-btn color="primary" icon="lock" :disabled="loggedin"  label="Войти" />
      </div>
    </div>
  </div>
</template>


<script>
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'TelegramLogin',
  setup() {

    const loggedin = ref(false);
    const name = ref('Telegram');
    const dest = ref('Вход не выполнен');
    const icon = ref('warning')
    axios.get("api/telegram/getMe").then(({data}) => {
      console.log(data.me)
      if (data.me === "true") {
        loggedin.value = true;
        dest.value = "Вход выполнен";
        icon.value = "check"
      }
    })

    return {
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

