<template>
  <div class="q-pa-md q-gutter-sm">
    <div class="avatar-card">
      <q-avatar size="120px" font-size="52px" color="teal" text-color="white" :icon="icon" />
      <div class="name-desc">
        <p class="name"> {{ name }} </p>
        <p class="desc"> {{ dest }} </p>
        <div style="display: flex;" class="inputButton">
          <q-input outlined v-if="login_stage == 1" v-model="text" label="Номер телефона" />
          <q-input outlined style="width: 20vh;" v-if="login_stage == 2" type="text" v-model.number="otp"
            label="Одноразовый ключ" />
          <q-input outlined style="width: 40vh;" v-if="login_stage == 2" type="password" v-model="tfa"
            label="Пароль 2FA (если нет, оставьте пустым)" />
          <q-btn color="primary" icon="forward" :disabled="loggedin" :label="b_label" @click="submitAction" />
        </div>
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
    const label = ref('Номер телефона');
    const b_label = ref('Войти');

    const text = ref('');
    const otp = ref();
    const tfa = ref('');

    const login_stage = ref(1);
    var phone_code;

    axios.get("api/telegram/signin").then(({ data }) => {
      console.log(data)
      if (data["_"] === "User") {
        login_stage.value = 3;
        b_label.value = "Вход выполнен";
        dest.value = data["username"];
        loggedin.value = true;
        icon.value = "check"
      }
    })

    function submitAction() {
      b_label.value = "Подождите..."
      if (login_stage.value == 1) {
        axios.get("api/telegram/requestcode", { params: { phone: text.value } }).then(({ data }) => {
          console.log(data);
          phone_code = data_result;
        })
      }
      if (login_stage.value == 2) {
        axios.get("api/telegram/signin",
          {
            params: {
              code: otp.value,
              password: tfa.value
            }
          }).then(({ data }) => {
            console.log(data);
          })
      }
      if (login_stage.value == 3) {
        b_label.value = "Вход выполнен";

        return;
      }
      b_label.value = "Далее";
      login_stage.value++;
    }



    return {
      name,
      dest,
      loggedin,
      icon,
      label,
      b_label,
      submitAction,
      text,
      login_stage,
      otp,
      tfa
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

