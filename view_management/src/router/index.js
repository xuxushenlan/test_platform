import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Function from '@/components/Function'
import store from '../vuex/store'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/function',
      name: 'Function',
      component: Function,
      meta: {
        requireAuth: true, // 该路由项需要登录访问
      }
    }
  ]
});

// 页面刷新时，重新赋值token
if (window.localStorage.getItem('token')) {
  store.commit('login', window.localStorage.getItem('token'))
}

// 导航守卫，控制一些页面登录才能访问
router.beforeEach((to, from, next) => {
  if (to.matched.some(r => r.meta.requireAuth)) {
    if (store.state.token) {
      next();
    }
    else {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    }
  }
  else {
    next();
  }
});

export default router;