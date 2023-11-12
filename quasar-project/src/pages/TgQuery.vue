<template>
  <DataEntrance style="height: 240px" icon="group" ttitle="Поиск">
    <div class="topform">
      <q-input class="topform__input idbox" outlined v-model.number="groupID" label="ID канала" />
      <q-input class="topform__input idbox" outlined v-model.number="userID" label="ID отправителя" />
      <q-input class="topform__input searchbox" outlined v-model.number="search_words" label="Ключевые слова" />
      <q-btn square color="primary" @click="tgsearch" icon="search" />
    </div>
  </DataEntrance>

  <div class="deflx" v-if="contentavail">
    <DataEntrance class="bottom_box" ttitle="Сообщения">
      <q-spinner-cube v-if="loading" color="primary" style="display: block;
                                                                margin:auto;" size="5.5em" />
      <div v-for="(item, index) in itemsRef" :key="index" class="caption">
        <q-card flat bordered>
          <div class="text-h5 q-mt-sm q-mb-xs" style="padding-left: 10px;">{{ item['date'] }}</div>
          <q-card-section vertical>
            <p>{{ item['text'] }}</p>
          </q-card-section>
          <div class="text-grey" style="padding-left: 10px;">Просмотров: {{ item['views'] }}
            <div>
              Реакции:
              <span v-for="em in item['reactions']" :key="em">
                {{ em['emoticon'] }} {{ em['count'] }}
              </span>
            </div>
          </div>
          <q-btn v-if="item['message_url']" color="primary" icon="web" target="_blank" :href="item['message_url']"
            label="Ссылка на пост" style="margin-left: 80%; margin-top: -5%;"></q-btn>
        </q-card>
      </div>
      <template v-slot:loading>
        <div class=" row justify-center q-my-md">
          <q-spinner-dots color="primary" size="40px" />
        </div>
      </template>
    </DataEntrance>

  </div>
</template>


<script>
import axios from "axios";
import DataEntrance from "../components/DataEntrance.vue"
// import SocialsInfo from "../components/SocialsInfo.vue"
import { defineComponent, ref } from 'vue'
import { loadConfig } from "browserslist";

export default defineComponent({
  components: { DataEntrance },
  setup() {
    const userID = ref('');
    const groupID = ref('');
    const itemsRef = ref([]);
    const search_words = ref('');
    const contentavail = ref(false);
    const loading = ref(true)
    function tgsearch() {
      contentavail.value = true
      loading.value = true
      itemsRef.value = []

      axios.get("api/vk/getMe").then(({ data }) => {
        console.log(data.me);
        if (!(data["_"] === "User")) {
          $q.notify('Пожалуста, авторизируйтесь!');
          return;
        }
      })

      axios.get('/api/telegram/getMessages', {
        params: {
          channel_name: groupID.value,
          userid: userID.value,
          search: search_words.value
        }
      }).then(({ data }) => {
        // const message = { 'message_url': 'https://t.me/sndkgram/1290', 'reactions': [{ 'emoticon': '🤨', 'count': 220202 }, { 'emoticon': '❤️', 'count': 2 }], 'date': '2023-11-11 10:35:06+00:00', 'user_url': 'https://web.telegram.org/k/#@Hordinar', 'text': 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).', 'message_id': 31213, 'views': 312 };
        // for (let i = 0; i < 2; i++) {
        //   itemsRef.value.push(message)
        // }
        const messages = data['messages']
        for (const elem of messages) {
          itemsRef.value.push(elem)
        }
        loading.value = false;
      })

    }

    return {
      itemsRef,
      userID,
      groupID,
      loading,
      search_words,
      contentavail,
      tgsearch,
    }
  }
});
</script>

<style>
.deflx {
  display: flex;
  flex-direction: row;
  justify-items: stretch;

}

.bottom_box {
  flex: 0 1 calc(50% - 0px);
  height: 65vh;
}

.FormCollection {
  display: inline-flex;
  flex-direction: row;
  display: flex;
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
  flex: 0 2 14%;
}

.searchbox {
  flex: 3 0 auto;
}

.deflx {
  display: flex;
  flex-direction: row;
  justify-items: stretch;

}

.bottom_box {
  flex: 0 1 calc(70% - 0px);
  margin: 0 auto;
  height: 63vh;
}
</style>

