<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          Волчий Тон
        </q-toolbar-title>


      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header>
          Сервисы
        </q-item-label>

        <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Обратный геопоиск',
    caption: 'Поиск отделений Почты России',
    icon: 'public',
    link: '/#/pochta'
  },
  {
    title: 'ВКонтакте',
    caption: 'Информация о пользователях и группах',
    icon: 'record_voice_over',
    link: '/#/vk'
  },
  {
    title: 'Telegram',
    caption: 'Получение и фильтрация сообщений в каналах',
    icon: 'chat',
    link: '/#/telegram'
  },
  {
    title: 'Настройки авторизации',
    caption: 'Для использования сервисов требуется авторизация',
    icon: 'settings',
    link: '/#/settings'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },

  setup() {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
