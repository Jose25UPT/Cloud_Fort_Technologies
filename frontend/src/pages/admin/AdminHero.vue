<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white">Sección Hero Principal</h1>
        <p class="text-gray-400 mt-1">
          Edita el contenido principal que aparece en la página de inicio
        </p>
      </div>
    </div>

    <!-- Error Message -->
    <div v-if="adminStore.error" class="bg-red-900/50 border border-red-500 rounded-lg p-4">
      <div class="flex items-center">
        <ExclamationTriangleIcon class="h-5 w-5 text-red-400 mr-2" />
        <p class="text-red-300 text-sm">{{ adminStore.error }}</p>
        <button @click="adminStore.clearError()" class="ml-auto text-red-400 hover:text-red-300">
          <XMarkIcon class="h-5 w-5" />
        </button>
      </div>
    </div>

    <!-- Success Message -->
    <div v-if="showSuccess" class="bg-green-900/50 border border-green-500 rounded-lg p-4">
      <div class="flex items-center">
        <CheckCircleIcon class="h-5 w-5 text-green-400 mr-2" />
        <p class="text-green-300 text-sm">Sección Hero actualizada correctamente</p>
        <button @click="showSuccess = false" class="ml-auto text-green-400 hover:text-green-300">
          <XMarkIcon class="h-5 w-5" />
        </button>
      </div>
    </div>

    <!-- Form -->
    <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <!-- Left Column -->
          <div class="space-y-6">
            <div>
              <label for="titulo" class="block text-sm font-medium text-gray-300 mb-2">
                Título Principal *
              </label>
              <input
                id="titulo"
                v-model="form.titulo"
                type="text"
                required
                class="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                placeholder="Título principal del hero"
              />
            </div>

            <div>
              <label for="subtitulo" class="block text-sm font-medium text-gray-300 mb-2">
                Subtítulo
              </label>
              <textarea
                id="subtitulo"
                v-model="form.subtitulo"
                rows="3"
                class="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                placeholder="Descripción que aparece debajo del título"
              />
            </div>

            <div>
              <label for="cta_texto" class="block text-sm font-medium text-gray-300 mb-2">
                Texto del Botón CTA
              </label>
              <input
                id="cta_texto"
                v-model="form.cta_texto"
                type="text"
                class="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                placeholder="Ej: Contáctanos"
              />
            </div>

            <div>
              <label for="cta_url" class="block text-sm font-medium text-gray-300 mb-2">
                URL del Botón CTA
              </label>
              <input
                id="cta_url"
                v-model="form.cta_url"
                type="text"
                class="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                placeholder="Ej: #contacto"
              />
            </div>
          </div>

          <!-- Right Column -->
          <div class="space-y-6">
            <div>
              <label for="imagen_url" class="block text-sm font-medium text-gray-300 mb-2">
                URL de Imagen de Fondo
              </label>
              <input
                id="imagen_url"
                v-model="form.imagen_url"
                type="text"
                class="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                placeholder="https://ejemplo.com/imagen.jpg"
              />
            </div>

            <!-- Preview -->
            <div class="bg-gray-800 rounded-lg p-4">
              <h3 class="text-sm font-medium text-gray-300 mb-3">Vista Previa</h3>
              <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg p-6 text-white">
                <h2 class="text-xl font-bold mb-2">
                  {{ form.titulo || 'Título del Hero' }}
                </h2>
                <p class="text-sm text-blue-100 mb-4">
                  {{ form.subtitulo || 'Subtítulo descriptivo...' }}
                </p>
                <div v-if="form.cta_texto" class="inline-flex">
                  <span class="px-4 py-2 bg-white text-blue-600 rounded-lg text-sm font-medium">
                    {{ form.cta_texto }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex items-center justify-end space-x-4 pt-6 border-t border-gray-800">
          <button
            type="button"
            @click="resetForm"
            class="px-4 py-2 text-gray-400 hover:text-white transition-colors"
          >
            Resetear
          </button>
          <button
            type="submit"
            :disabled="adminStore.loading"
            class="flex items-center px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-900 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            <svg
              v-if="adminStore.loading"
              class="animate-spin -ml-1 mr-2 h-4 w-4 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ adminStore.loading ? 'Guardando...' : 'Guardar Cambios' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAdminStore } from '@/stores/admin'
import {
  ExclamationTriangleIcon,
  XMarkIcon,
  CheckCircleIcon
} from '@heroicons/vue/24/outline'

const adminStore = useAdminStore()
const showSuccess = ref(false)

const form = ref({
  titulo: '',
  subtitulo: '',
  cta_texto: '',
  cta_url: '',
  imagen_url: ''
})

const handleSubmit = async () => {
  const result = await adminStore.updateHero(form.value)
  
  if (result) {
    showSuccess.value = true
    setTimeout(() => {
      showSuccess.value = false
    }, 3000)
  }
}

const resetForm = () => {
  if (adminStore.hero) {
    form.value = {
      titulo: adminStore.hero.titulo,
      subtitulo: adminStore.hero.subtitulo || '',
      cta_texto: adminStore.hero.cta_texto || '',
      cta_url: adminStore.hero.cta_url || '',
      imagen_url: adminStore.hero.imagen_url || ''
    }
  } else {
    form.value = {
      titulo: '',
      subtitulo: '',
      cta_texto: '',
      cta_url: '',
      imagen_url: ''
    }
  }
}

onMounted(async () => {
  await adminStore.fetchHero()
  resetForm()
})
</script>
