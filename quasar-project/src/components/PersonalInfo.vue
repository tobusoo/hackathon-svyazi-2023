<template>
  <div class="q-pa-md q-gutter-sm">
    <div class="avatar-card">
      <q-avatar size="120px" font-size="52px" color="teal" text-color="white" icon="warning" />
      <div class="name-desc">
        <p class="name"> Имярек Имярек </p>
        <p class="desc"> Описание </p>
        <q-btn color="primary" icon="lock" label="Вход в учетную запись" />
      </div>
    </div>
  </div>
</template>


<script>
import { defineComponent, ref } from 'vue'
export default defineComponent({
  name: 'PersonalInfo',
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

