<template>
  <DataEntrance style="height: 240px" icon="group" ttitle="Поиск">
    <div class="FormCollection">
      <div class="topform">
        <q-input class="topform__input" outlined type="number" v-model.number="userID" label="ID пользователя" />
        <q-btn square color="primary" icon="search" label="Поиск пользователя" />
      </div>
      <div class="topform">
        <q-input class="topform__input" outlined type="number" v-model.number="groupID" label="ID группы" />
        <q-btn square color="primary" icon="search" label="Поиск группы" />
      </div>
    </div>
  </DataEntrance>
  <DataEntrance style="height: 61vh" icon="man" ttitle="Информация">
    <SocialsInfo> </SocialsInfo>
  </DataEntrance>
</template>


<script>
import DataEntrance from "../components/DataEntrance.vue"
import SocialsInfo from "../components/SocialsInfo.vue"
import { defineComponent, ref } from 'vue'

export default defineComponent({
  components: { DataEntrance, SocialsInfo },
  setup() {
    const userID = ref(0);
    const groupID = ref(0);
    return {
      userID,
      groupID
    };
  }
});
</script>

<style>
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

