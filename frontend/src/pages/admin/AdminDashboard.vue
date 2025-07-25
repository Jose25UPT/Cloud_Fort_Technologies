<template>
  <div class="space-y-6">
    <!-- Welcome Message -->
    <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl p-6 text-white">
      <h1 class="text-2xl font-bold mb-2">¡Bienvenido de vuelta!</h1>
      <p class="text-blue-100">
        Gestiona el contenido de Cloud Fort Technologies desde este panel de administración.
      </p>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <WrenchScrewdriverIcon class="h-8 w-8 text-blue-500" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-400">Servicios</p>
            <p class="text-2xl font-semibold text-white">{{ adminStore.services.length }}</p>
          </div>
        </div>
      </div>

      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <BriefcaseIcon class="h-8 w-8 text-green-500" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-400">Proyectos</p>
            <p class="text-2xl font-semibold text-white">{{ adminStore.projects.length }}</p>
          </div>
        </div>
      </div>

      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <ChatBubbleLeftRightIcon class="h-8 w-8 text-yellow-500" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-400">Testimonios</p>
            <p class="text-2xl font-semibold text-white">{{ adminStore.testimonials.length }}</p>
          </div>
        </div>
      </div>

      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <InboxIcon class="h-8 w-8 text-purple-500" />
          </div>
          <div class="ml-4">
            <p class="text-sm font-medium text-gray-400">Solicitudes</p>
            <p class="text-2xl font-semibold text-white">{{ adminStore.contactRequests.length }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <h2 class="text-xl font-semibold text-white mb-4">Acciones Rápidas</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <router-link
          to="/admin/hero"
          class="flex items-center p-4 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <PhotoIcon class="h-6 w-6 text-blue-500 mr-3" />
          <div>
            <h3 class="text-sm font-medium text-white">Editar Hero</h3>
            <p class="text-xs text-gray-400">Actualizar sección principal</p>
          </div>
        </router-link>

        <router-link
          to="/admin/servicios"
          class="flex items-center p-4 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <PlusIcon class="h-6 w-6 text-green-500 mr-3" />
          <div>
            <h3 class="text-sm font-medium text-white">Añadir Servicio</h3>
            <p class="text-xs text-gray-400">Crear nuevo servicio</p>
          </div>
        </router-link>

        <router-link
          to="/admin/proyectos"
          class="flex items-center p-4 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <PlusIcon class="h-6 w-6 text-yellow-500 mr-3" />
          <div>
            <h3 class="text-sm font-medium text-white">Añadir Proyecto</h3>
            <p class="text-xs text-gray-400">Crear nuevo proyecto</p>
          </div>
        </router-link>

        <router-link
          to="/admin/testimonios"
          class="flex items-center p-4 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <PlusIcon class="h-6 w-6 text-purple-500 mr-3" />
          <div>
            <h3 class="text-sm font-medium text-white">Añadir Testimonio</h3>
            <p class="text-xs text-gray-400">Crear nuevo testimonio</p>
          </div>
        </router-link>

        <router-link
          to="/admin/contacto"
          class="flex items-center p-4 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <BuildingOfficeIcon class="h-6 w-6 text-blue-500 mr-3" />
          <div>
            <h3 class="text-sm font-medium text-white">Editar Contacto</h3>
            <p class="text-xs text-gray-400">Actualizar información</p>
          </div>
        </router-link>

        <router-link
          to="/admin/solicitudes"
          class="flex items-center p-4 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors"
        >
          <InboxIcon class="h-6 w-6 text-red-500 mr-3" />
          <div>
            <h3 class="text-sm font-medium text-white">Ver Solicitudes</h3>
            <p class="text-xs text-gray-400">Revisar mensajes</p>
          </div>
        </router-link>
      </div>
    </div>

    <!-- Recent Contact Requests -->
    <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-xl font-semibold text-white">Solicitudes Recientes</h2>
        <router-link
          to="/admin/solicitudes"
          class="text-blue-400 hover:text-blue-300 text-sm font-medium"
        >
          Ver todas →
        </router-link>
      </div>

      <div v-if="recentRequests.length === 0" class="text-center py-8">
        <InboxIcon class="h-12 w-12 text-gray-600 mx-auto mb-4" />
        <p class="text-gray-400">No hay solicitudes recientes</p>
      </div>

      <div v-else class="space-y-4">
        <div
          v-for="request in recentRequests"
          :key="request.id"
          class="flex items-start space-x-4 p-4 bg-gray-800 rounded-lg"
        >
          <div class="flex-shrink-0">
            <div class="h-8 w-8 bg-blue-600 rounded-full flex items-center justify-center">
              <span class="text-sm font-medium text-white">{{ request.nombre[0] }}</span>
            </div>
          </div>
          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between">
              <p class="text-sm font-medium text-white truncate">{{ request.nombre }}</p>
              <p class="text-xs text-gray-400">{{ formatDate(request.timestamp) }}</p>
            </div>
            <p class="text-sm text-gray-400">{{ request.correo }}</p>
            <p class="text-sm text-gray-300 mt-1 truncate">{{ request.mensaje }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useAdminStore } from '@/stores/admin'
import {
  WrenchScrewdriverIcon,
  BriefcaseIcon,
  ChatBubbleLeftRightIcon,
  InboxIcon,
  PhotoIcon,
  PlusIcon,
  BuildingOfficeIcon
} from '@heroicons/vue/24/outline'

const adminStore = useAdminStore()

const recentRequests = computed(() => {
  return adminStore.contactRequests.slice(0, 5)
})

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    day: 'numeric',
    month: 'short',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  // Load data for dashboard
  await Promise.all([
    adminStore.fetchServices(),
    adminStore.fetchProjects(),
    adminStore.fetchTestimonials(),
    adminStore.fetchContactRequests()
  ])
})
</script>
