<template>
  <DataEntrance  style="height: 240px" icon="group" ttitle="Поиск">
    <div class="topform">
      <q-input class="topform__input idbox" outlined v-model.number="groupID" label="ID группы" />
      <q-input class="topform__input idbox" outlined v-model.number="userID" label="ID отправителя" />
      <q-input class="topform__input searchbox" outlined type="text" v-model="query" label="Текст" />
      <q-btn square color="primary" @click="tgsearch" icon="search" />
    </div>
  </DataEntrance>

  <div class="deflx" v-if="contentavail">
    <DataEntrance class="bottom_box" icon=" man" ttitle="Информация">
      <SocialsInfo class="si"> </SocialsInfo>
    </DataEntrance>

    <DataEntrance class="bottom_box" ttitle="Сообщения">
      <div ref="scrollTargetRef" class="infscroll" style="overflow: auto;">
        <q-infinite-scroll @load="onLoadRef" :offset="250" :scroll-target="scrollTargetRef">
          <div v-for="(item, index) in itemsRef" :key="index" class="caption">
            <text-subtitle2 style="margin:0px; font-style: oblique;">13:37 05.04.2018</text-subtitle2>
            <p style="margin-bottom: 10px">Текст сообщения</p>
          </div>
          <template v-slot:loading>
            <div class="row justify-center q-my-md">
              <q-spinner-dots color="primary" size="40px" />
            </div>
          </template>
        </q-infinite-scroll>
      </div>
    </DataEntrance>
  </div>
</template>


<script>
import DataEntrance from "../components/DataEntrance.vue"
import SocialsInfo from "../components/SocialsInfo.vue"
import { defineComponent, ref } from 'vue'

export default defineComponent({
  components: { DataEntrance, SocialsInfo },
  setup() {
    const userID = ref();
    const groupID = ref();
    const itemsRef = ref([{}, {}, {}, {}, {}, {}, {}])
    const itemsId = ref([{}, {}, {}, {}, {}, {}, {}])
    const scrollTargetRef = ref(null)

    function tgsearch() {

    }
    const contentavail = ref(false);
    return {
      itemsRef,
      itemsId,
      scrollTargetRef,
      userID,
      groupID,
      contentavail,
      onLoadRef(index, done) {
        setTimeout(() => {
          itemsRef.value.push({}, {}, {}, {}, {}, {}, {})
          done()
        }, 2000)
      },

      onLoadId(index, done) {
        setTimeout(() => {
          itemsId.value.push({}, {}, {}, {}, {}, {}, {})
          done()
        }, 2000)
      }
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
  flex: 0 1 calc(50% - 0px);
  height: 63vh;
}
</style>

