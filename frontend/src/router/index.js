import { createRouter, createWebHistory } from 'vue-router'
import MainContent from '@/components/MainContent.vue'
import PickEm from '@/components/PickEm.vue'
export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: MainContent },   // homepage = leaderboard
    { path: '/pickEm', component: PickEm },
  ]
})
