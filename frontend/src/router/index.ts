import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/admin',
      name: 'admin-dashboard',
      component: () => import('@/pages/admin/AdminDashboard.vue')
    },
    {
      path: '/admin/login',
      name: 'admin-login',
      component: () => import('@/pages/admin/AdminLogin.vue')
    },
    {
      path: '/admin/hero',
      name: 'admin-hero',
      component: () => import('@/pages/admin/AdminHero.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/pages/NotFound.vue')
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    // If there's a saved position (e.g., when using back button)
    if (savedPosition) {
      return savedPosition
    }
    
    // If the route has a hash, scroll to that element
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
        top: 80 // Account for any fixed header
      }
    }
    
    // Otherwise, scroll to top
    return { top: 0, behavior: 'smooth' }
  }
})

export default router
