<template>
  <DataEntrance style="height: 430px" icon="settings" ttitle="Настройки">
    <div style="'
          display: flex;
          flex-direction: row;
          justify-content:center;
          ">
      <PersonalInfo></PersonalInfo>
      <PersonalInfo></PersonalInfo>
    </div>
  </DataEntrance>
</template>


<script>
import DataEntrance from "../components/DataEntrance.vue"

import { defineComponent, ref } from 'vue'
import PersonalInfo from "src/components/PersonalInfo.vue";
export default defineComponent({
  components: { DataEntrance, PersonalInfo },
  setup() {

  }
});
</script>

<style>
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
</style>

