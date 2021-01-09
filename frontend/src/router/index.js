import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Will from '../views/Will.vue'
import Question from '../views/Question.vue'
import Rank from '../views/Rank.vue'
// import FreeWill from '../views/FreeWill.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/will*',
    name: 'Will',
    component: Will
  },
  {
    path: '/question*',
    name: 'Question',
    component: Question
  },
  {
    path: '/rank',
    name: 'Rank',
    component: Rank
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
