<template>
  <DataEntrance style="height: 240px" icon="radar" ttitle="Координаты">
    <div class="topform">
      <q-input class="topform__input" outlined type="number" v-model.number="coords[0]" label="Широта" />
      <q-input class="topform__input" outlined type="number" v-model.number="coords[1]" label="Долгота" />
      <q-input class="topform__input" type="number" outlined v-model.number="rad" label="Радиус (м)" />
      <q-btn square color="primary" icon="search" label="Поиск" @click="search" />
    </div>
  </DataEntrance>
  <div class="deflx">
    <DataEntrance class="bottom_box" icon="list" ttitle="Таблица"> asdr </DataEntrance>
    <DataEntrance class="bottom_box" icon="map" ttitle="Карта">
      <YandexMap :settings="settings" :coordinates="coords">
        <YandexMarker :coordinates="coords" marker-id="radMarker" :radius="rad" type="Circle">
        </YandexMarker>
      </YandexMap>
    </DataEntrance>
  </div>
</template>


<script>
import DataEntrance from "../components/DataEntrance.vue"
import { YandexMap, YandexMarker } from 'vue-yandex-maps'
import { defineComponent, ref } from 'vue'

export default defineComponent({
  components: { DataEntrance, YandexMap, YandexMarker },
  setup() {
    const coords = ref([0, 0]);
    const rad = ref(0);

    return {
      rad,
      coords,
      settings: {
        apiKey: 'ae584a4b-061d-43f8-ac9d-e241ac0d414a',
        lang: 'ru_RU',
        coordorder: 'latlong',
        enterprise: false,
        version: '2.1'
      },

    }
  },
});
</script>

<style>
.yandex-container {
  height: 52vh;
}

.topform {
  display: flex;
  gap: 1rem;
  background-color: lightblue;
  padding: 2rem;
  align-items: stretch;
}

.topform__input {
  background-color: white;
  border-radius: 5%;
}

.deflx {
  display: flex;
  flex-direction: row;
  justify-items: stretch;

}

.bottom_box {
  flex: 0 1 calc(50% - 0px);
  height: 58vh;
}
</style>

