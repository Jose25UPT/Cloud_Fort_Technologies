import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'admin-login',
      component: () => import('@/pages/admin/AdminLogin.vue')
    },
    {
      path: '/admin',
      name: 'admin-dashboard',
      component: () => import('@/pages/admin/AdminDashboard.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/bandeja_entrada_cloudforttechnologies',
      name: 'bandeja-entrada',
      component: () => import('@/pages/admin/TestBandeja.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/admin/dashboard',
      redirect: '/admin'
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/pages/NotFound.vue')
    }
  ],
  scrollBehavior(to, _from, savedPosition) {
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

// Navigation Guard for Authentication
router.beforeEach(async (to, _from, next) => {
  const authStore = useAuthStore()
  
  // Check if the route requires authentication
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Check if user is authenticated
    if (!authStore.isAuthenticated) {
      // User is not authenticated, redirect to login
      next({ name: 'admin-login', query: { redirect: to.fullPath } })
      return
    }
    
    // Verify token is still valid
    const isValidToken = await authStore.checkAuth()
    if (!isValidToken) {
      // Token is invalid, redirect to login
      next({ name: 'admin-login', query: { redirect: to.fullPath } })
      return
    }
  }
  
  // If going to login and already authenticated, redirect to admin
  if (to.name === 'admin-login' && authStore.isAuthenticated) {
    next({ name: 'admin-dashboard' })
    return
  }
  
  next()
})

export default router
