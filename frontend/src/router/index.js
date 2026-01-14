import { createRouter, createWebHistory } from 'vue-router'
import MainContent from '@/components/MainContent.vue'
import Rules from '@/views/Rules.vue'
export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: MainContent },   // homepage = leaderboard
    { path: '/rules', component: Rules },
  ]
})

