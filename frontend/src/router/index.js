import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// import Todo from '../views/TodoView.vue'
import Will from '../views/Will.vue'
import Question from '../views/Question.vue'
// import FreeWill from '../views/FreeWill.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  // {
  //   path: '/todo',
  //   name: 'Todo',
  //   component: Todo
  // },
  {
    path: '/will*',
    name: 'Will',
    component: Will
  },
  // {
  //   path: '/freewill*',
  //   name: 'FreeWill',
  //   component: FreeWill
  // },
  {
    path: '/question*',
    name: 'Question',
    component: Question
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
