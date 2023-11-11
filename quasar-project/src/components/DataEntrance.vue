<template>
  <div class="q-pa-md">
    <q-layout view="lHh lpr lFf" container class="shadow-2 rounded-borders">
      <q-header elevated>
        <q-toolbar>
          <q-icon style="font-size: 2em;" :name="icon" />
          <q-toolbar-title>{{ ttitle }}</q-toolbar-title>
        </q-toolbar>
      </q-header>
      <q-page-container>
        <q-page class="q-pa-md">
          <slot></slot>
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>


<script>
import { defineComponent, ref } from 'vue'
export default defineComponent({

  name: 'DataEntrance',
  props: {
    icon: {
      type: String,
      default: 'loyalty'
    },
    ttitle: {
      type: String,
      default: ''
    }
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
}

.topform__input {
  background-color: white;
  border-radius: 5%;
}
</style>

