<template>
  <DataEntrance style="height: 240px" icon="group" ttitle="Поиск">
    <div class="FormCollection">
      <div class="topform">
        <q-input class="topform__input" outlined type="text" v-model="userID" label="ID пользователя" />
        <q-btn square color="primary" icon="search" label="Поиск пользователя" @click="search_user" />
      </div>
      <div class="topform">
        <q-input class="topform__input" outlined type="text" v-model="groupID" label="ID группы" />
        <q-btn square color="primary" icon="search" label="Поиск группы" @click="search_group" />
      </div>
    </div>
  </DataEntrance>
  <DataEntrance v-if="display_mode === 'user'" style="height: 61vh" icon="man" ttitle="Информация">
    <SocialsInfo :avatar="avatar" :link="link" :name="name" :surname="sname" :desc="desc" :bday="bday"> </SocialsInfo>
  </DataEntrance>
</template>


<script>

import DataEntrance from "../components/DataEntrance.vue"
import SocialsInfo from "../components/SocialsInfo.vue"
import axios from 'axios'
import { defineComponent, devtools, ref } from 'vue'
import { useQuasar } from 'quasar'

export default defineComponent({
  components: { DataEntrance, SocialsInfo },
  setup() {
    const userID = ref('');
    const groupID = ref('');

    const avatar = ref('')
    const name = ref('')
    const sname = ref('')
    const desc = ref('')
    const bday = ref('')
    const link = ref('')
    const display_mode = ref("none");
    const $q = useQuasar()


    function search_user() {
      axios.get("api/vk/getMe").then(({data}) => {
        console.log(data.me);
        if (!(data.me === "true")) {
          $q.notify('Пожалуста, авторизируйтесь!');
          return;
        }
      })

      axios.get("api/vk/getUsers", { params: { userid: userID.value } }).then(({ data }) => {
        console.log(data["response"][0])
        data = data["response"][0]
        display_mode.value = ("user");
        avatar.value = data['photo_200']
        name.value = data['first_name']
        sname.value = data['last_name']
        bday.value = data['bdate']
        desc.value = data['status']
        link.value = ("https://vk.com/id" + data['id'])
      })
    }

    function search_group() {
      axios.get("api/vk/getMe").then(({data}) => {
        console.log(data.me);
        if (!(data.me === "true")) {
          $q.notify('Пожалуста, авторизируйтесь!');
          return;
        }
      })
      axios.get("api/vk/getGroups", { params: { groupid: groupID.value } }).then(({ data }) => {
        console.log(data["response"][0])
        data = data["response"][0]
        display_mode.value = ("user");
        avatar.value = data['photo_200']
        name.value = data['name']
        sname.value = ''
        bday.value = ''
        desc.value = data['status']
        link.value = ("https://vk.com/public" + data['id'])
      })
    }


    return {
      userID,
      groupID,
      search_user,
      search_group,
      avatar,
      name,
      sname,
      desc,
      bday,
      link,
      display_mode
    };
  }
});
</script>

<style>
.FormCollection {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content: center;
}

.topform {
  display: flex;
  gap: 1rem;
  background-color: lightblue;
  padding: 2rem;
  align-items: stretch;
  flex-grow: 2;
}

.topform__input {
  background-color: white;
  border-radius: 5%;
  min-width: 30vh;
}

.deflx {
  display: flex;
  flex-direction: row;
  justify-items: stretch;

}

.bottom_box {
  flex: 0 1 calc(50% - 0px);
  height: 65vh;
}
</style>

