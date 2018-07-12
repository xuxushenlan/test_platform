import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Function from '@/components/Function'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login,
    },
    {
      path: '/function',
      name: 'Function',
      component: Function,
    }
  ]
})
