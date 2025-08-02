<template>
  <div class="min-h-screen bg-black flex">
    <!-- Sidebar -->
    <div class="fixed inset-y-0 left-0 z-50 w-64 bg-gray-900 transform lg:transform-none lg:block" :class="sidebarOpen ? 'translate-x-0' : '-translate-x-full'">
      <div class="flex items-center justify-center h-16 px-4 border-b border-gray-800">
        <h1 class="text-lg font-bold text-white">
          Cloud Fort <span class="text-blue-500">Admin</span>
        </h1>
      </div>

      <!-- Navigation Menu -->
      <nav class="mt-8">
        <div class="px-4 space-y-2">
          <router-link
            v-for="item in navigation"
            :key="item.name"
            :to="item.href"
            class="group flex items-center px-3 py-3 text-sm font-medium text-gray-300 rounded-lg hover:bg-gray-800 hover:text-white transition-all duration-200"
            :class="{ 'bg-gray-800 text-white': $route.path === item.href }"
          >
            <component :is="item.icon" class="flex-shrink-0 w-5 h-5 mr-3" />
            {{ item.name }}
          </router-link>
        </div>
      </nav>

      <!-- Logout Button -->
      <div class="absolute bottom-4 left-4 right-4">
        <button
          @click="handleLogout"
          class="w-full flex items-center px-3 py-3 text-sm font-medium text-gray-300 rounded-lg hover:bg-red-600 hover:text-white transition-all duration-200 group"
        >
          <ArrowLeftOnRectangleIcon class="flex-shrink-0 w-5 h-5 mr-3" />
          Cerrar Sesión
        </button>
      </div>
    </div>

    <!-- Mobile sidebar overlay -->
    <div 
      v-if="sidebarOpen" 
      @click="sidebarOpen = false"
      class="fixed inset-0 bg-gray-600 bg-opacity-75 z-40 lg:hidden"
    ></div>

    <!-- Main Content -->
    <div class="flex-1 lg:pl-64">
      <!-- Top navbar -->
      <header class="bg-gray-900 border-b border-gray-800 h-16">
        <div class="flex items-center justify-between h-full px-4 sm:px-6 lg:px-8">
          <div class="flex items-center">
            <!-- Mobile menu button -->
            <button
              @click="sidebarOpen = true"
              class="lg:hidden -ml-0.5 -mt-0.5 h-12 w-12 inline-flex items-center justify-center rounded-md text-gray-500 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
            >
              <Bars3Icon class="h-6 w-6" />
            </button>

            <h1 class="ml-4 lg:ml-0 text-xl font-semibold text-white">{{ pageTitle }}</h1>
          </div>

          <div class="flex items-center space-x-4">
            <!-- User info -->
            <div class="flex items-center space-x-3">
              <div class="text-right">
                <p class="text-sm font-medium text-white">{{ authStore.user?.username }}</p>
                <p class="text-xs text-gray-400">Administrador</p>
              </div>
              <div class="flex-shrink-0">
                <div class="h-8 w-8 rounded-full bg-blue-600 flex items-center justify-center">
                  <span class="text-sm font-medium text-white">CF</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- Page content -->
      <main class="flex-1 p-6">
        <div class="max-w-7xl mx-auto">
          <router-view />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import {
  HomeIcon,
  PhotoIcon,
  WrenchScrewdriverIcon,
  BriefcaseIcon,
  ChatBubbleLeftRightIcon,
  BuildingOfficeIcon,
  InboxIcon,
  ArrowLeftOnRectangleIcon,
  Bars3Icon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const sidebarOpen = ref(false)

const navigation = [
  {
    name: 'Dashboard',
    href: '/admin',
    icon: HomeIcon
  },
  {
    name: 'Hero Principal',
    href: '/admin/hero',
    icon: PhotoIcon
  },
  {
    name: 'Servicios',
    href: '/admin/servicios',
    icon: WrenchScrewdriverIcon
  },
  {
    name: 'Proyectos',
    href: '/admin/proyectos',
    icon: BriefcaseIcon
  },
  {
    name: 'Testimonios',
    href: '/admin/testimonios',
    icon: ChatBubbleLeftRightIcon
  },
  {
    name: 'Contactos',
    href: '/admin/contacts',
    icon: InboxIcon
  },
  {
    name: 'Configuración',
    href: '/admin/configuracion',
    icon: BuildingOfficeIcon
  }
]

const pageTitle = computed(() => {
  const currentItem = navigation.find(item => item.href === route.path)
  return currentItem?.name || 'Panel de Administración'
})

const handleLogout = () => {
  authStore.logout()
  router.push('/admin/login')
}
</script>
