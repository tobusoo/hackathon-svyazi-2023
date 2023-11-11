<template>
  <div class="q-pa-md q-gutter-sm">
    <div class="avatar-card">
      <q-avatar size="120px" font-size="52px" color="teal" text-color="white" icon="warning" />
      <div class="name-desc">
        <p class="name"> Имярек Имярек </p>
        <p class="desc"> Описание </p>
        <q-btn color="primary" icon="web" label="На страницу" />
      </div>
    </div>
  </div>
  <!--
  <div class="q-pa-md q-gutter-md">
    <q-list bordered class="rounded-borders" style="max-width: 350px">
      <q-item-label header>Друзья</q-item-label>

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar2.jpg">
          </q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label lines="1">Brunch this weekend?</q-item-label>
        </q-item-section>
      </q-item>

      <q-separator inset="item" />

      <q-item clickable v-ripple>
        <q-item-section avatar>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar4.jpg">
          </q-avatar>
        </q-item-section>
        <q-item-section>
          <q-item-label lines="1">Linear Project</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
  -->
</template>


<script>
import { defineComponent, ref } from 'vue'
export default defineComponent({
  name: 'SocialsInfo',
  setup() {
    const itemsRef = ref([{}, {}, {}, {}, {}, {}, {}])
    const itemsId = ref([{}, {}, {}, {}, {}, {}, {}])
    const scrollTargetRef = ref(null)

    return {
      itemsRef,
      itemsId,
      scrollTargetRef,

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

