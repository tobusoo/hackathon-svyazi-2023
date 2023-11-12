<template>
  <DataEntrance style="height: 240px" icon="radar" ttitle="Координаты">
    <div class="topform">
      <q-input class="topform__input" outlined type="number" v-model.number="coords[0]" label="Широта" />
      <q-input class="topform__input" outlined type="number" v-model.number="coords[1]" label="Долгота" />
      <q-input class="topform__input" type="number" outlined v-model.number="rad" label="Радиус (м)" />
      <q-btn square color="primary" icon="search" label="Поиск" @click="geo_search" />
    </div>
  </DataEntrance>
  <div class="deflx" v-if="show">
    <DataEntrance class="bottom_box" icon="list" ttitle="Найденные адреса (Максимум 20)">
      <!-- {{ adresses_count }} -->
      <div v-for="adress in adresses" :key="adress">
        <q-card class="my-card" flat bordered>
          <q-card-section horizontal>
            <q-card-section class="q-pt-xs">
              <div class="text-overline">{{ adress['postal_code'] }}</div>
              <div class="text-h5 q-mt-sm q-mb-xs">{{ adress['country'] }}, {{ adress['city'] }}, {{ adress['street'] }},
                {{ adress['house'] }}</div>
              <div class="text-caption text-grey">
                Широта: {{ adress['geo_lat'] }}
                Долгота: {{ adress['geo_lon'] }}
              </div>
            </q-card-section>
          </q-card-section>
        </q-card>
      </div>
    </DataEntrance>

    <DataEntrance class="bottom_box" icon="list" ttitle="Ближайшие почтовые отделения">
      <div v-for="postal in postals" :key="postal">
        <q-card class="my-card" flat bordered>
          <q-card-section horizontal>
            <q-card-section class="q-pt-xs">
              <div class="text-overline">{{ postal['postal_code'] }}</div>
              <div class="text-h5 q-mt-sm q-mb-xs"> {{ postal['address_str'] }} </div>
              <div class="text-h6">График работы:</div>
              <div class="text-overline">Пон: {{ postal['schedule_mon'] }}</div>
              <div class="text-overline">Вт: {{ postal['schedule_tue'] }}</div>
              <div class="text-overline">Ср: {{ postal['schedule_wed'] }}</div>
              <div class="text-overline">Чет: {{ postal['schedule_thu'] }}</div>
              <div class="text-overline">Пят: {{ postal['schedule_fri'] }}</div>
              <div class="text-overline">Субб: {{ postal['schedule_sat'] }}</div>
              <div class="text-overline">Вск: {{ postal['schedule_sun'] }}</div>
              <div class="text-caption text-grey">
                Широта: {{ postal['geo_lat'] }}
                Долгота: {{ postal['geo_lon'] }}
              </div>
            </q-card-section>
          </q-card-section>
        </q-card>
      </div>
    </DataEntrance>

    <DataEntrance class="bottom_box" icon="map" ttitle="Карта">
      <YandexMap :settings="settings" :zoom=zoom :coordinates=coords>
        <YandexMarker :coordinates=coords marker-id="radMarker" :radius="rad" type="Circle"
          :options="{ fillColor: 'ff0000', fillOpacity: 0.1, outline: false }">
        </YandexMarker>
        <div v-for=" coord in coords_addresses" :key="coord">
          <YandexMarker :coordinates=coord marker-id="adresses" type="Point" :options="{ iconColor: '#ff0000' }">
          </YandexMarker>
        </div>
        <div v-for="coord in coords_postals" :key="coord">
          <YandexMarker :coordinates=coord marker-id="postals" type="Point" :options="{ iconColor: '#0066cc' }">
          </YandexMarker>
        </div>
      </YandexMap>
    </DataEntrance>
  </div>
</template>


<script>
import DataEntrance from "../components/DataEntrance.vue"
import { YandexMap, YandexMarker } from 'vue-yandex-maps'
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  components: { DataEntrance, YandexMap, YandexMarker },
  setup() {
    const coords = ref([55.013296, 82.950971]);
    const rad = ref(1000);
    const adresses = ref([]);
    const adresses_count = ref('');
    const postals = ref([]);
    const postals_count = ref('');
    const zoom = ref(12);
    const coords_addresses = ref([]);
    const coords_postals = ref([]);
    const show = ref(0);

    function geo_search() {
      adresses.value = [];
      adresses_count.value = '';
      postals.value = [];
      postals_count.value = '';
      coords_addresses.value = [];
      zoom.value = 10;
      coords_postals.value = [];

      show.value = 1;
      axios.get("api/geo/search", { params: { radius: rad.value, lon: coords.value[1], lat: coords.value[0] } }).then(({ data }) => {
        const adrss = data['adresses'];
        const pstls = data['postals'];
        adresses_count.value = 'Найдено ' + adrss['count'] + ' Адрес(а/ов)';
        postals_count.value = 'Найдено ' + pstls['count'] + ' почтовое отделение';
        for (const elem of adrss['adresses']) {
          adresses.value.push(elem)
          coords_addresses.value.push([elem['geo_lat'], elem['geo_lon']]);
        }

        zoom.value = 14

        for (const elem of pstls['postals']) {
          postals.value.push(elem)
          coords_postals.value.push([elem['geo_lat'], elem['geo_lon']]);
        }
      })
    }

    return {
      rad,
      coords,
      adresses,
      adresses_count,
      postals,
      postals_count,
      show,
      zoom,
      coords_addresses,
      coords_postals,
      geo_search,
      settings: {
        apiKey: 'ae584a4b-061d-43f8-ac9d-e241ac0d414a',
        lang: 'ru_RU',
        coordorder: 'latlong',
        enterprise: false,
        version: '2.1'
      },
      properties: {
        fillColor: 'CCFFCC',
      }
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

