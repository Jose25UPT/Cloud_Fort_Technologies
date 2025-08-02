<template>
  <div class="min-h-screen bg-black text-white">
    <!-- Header con navegación interna -->
    <div class="bg-gradient-to-r from-purple-900 to-blue-900 p-6 border-b border-gray-700">
      <div class="max-w-7xl mx-auto">
        <h1 class="text-4xl font-bold mb-4 text-center">
          🏢 CLOUD FORT TECHNOLOGIES - PANEL ADMINISTRATIVO
        </h1>
        
        <!-- Navegación interna -->
        <div class="flex justify-center space-x-4 mb-4">
          <button
            @click="activeSection = 'bandeja'"
            :class="[
              'px-6 py-3 rounded-lg font-medium transition-all',
              activeSection === 'bandeja' 
                ? 'bg-blue-600 text-white shadow-lg' 
                : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
            ]"
          >
            📨 BANDEJA DE ENTRADA ({{ contacts.length }})
          </button>
          <button
            @click="activeSection = 'dashboard'"
            :class="[
              'px-6 py-3 rounded-lg font-medium transition-all',
              activeSection === 'dashboard' 
                ? 'bg-purple-600 text-white shadow-lg' 
                : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
            ]"
          >
            📊 DASHBOARD DE VISITAS
          </button>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto p-6">
      <!-- SECCIÓN BANDEJA DE ENTRADA -->
      <div v-if="activeSection === 'bandeja'">
        <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
          <div class="flex items-center justify-between mb-6">
            <h2 class="text-3xl font-bold text-white flex items-center">
              📨 BANDEJA DE ENTRADA
              <span v-if="contacts.length > 0" class="ml-3 bg-red-500 text-white text-sm px-3 py-1 rounded-full animate-pulse">
                {{ contacts.length }} NUEVAS
              </span>
            </h2>
            <div class="flex space-x-3">
              <button
                @click="downloadAllContactsPDF"
                class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg font-medium"
              >
                📄 DESCARGAR TODO (PDF)
              </button>
              <button
                @click="loadContacts"
                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium"
              >
                🔄 ACTUALIZAR
              </button>
            </div>
          </div>

          <!-- Filtros y búsqueda -->
          <div class="bg-gray-800 rounded-lg p-4 mb-6">
            <div class="flex flex-wrap items-center gap-4">
              <div class="flex items-center space-x-2">
                <label class="text-sm text-gray-300">🔍 Buscar:</label>
                <input 
                  v-model="searchTerm"
                  type="text" 
                  placeholder="Nombre, email, empresa..."
                  class="bg-gray-700 text-white px-3 py-2 rounded text-sm w-64"
                >
              </div>
              <div class="flex items-center space-x-2">
                <label class="text-sm text-gray-300">🎯 Tipo:</label>
                <select 
                  v-model="selectedType" 
                  class="bg-gray-700 text-white px-3 py-2 rounded text-sm"
                >
                  <option value="">Todos</option>
                  <option v-for="type in contactTypes" :key="type" :value="type">{{ type }}</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Loading -->
          <div v-if="loading" class="text-center py-12">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
            <p class="text-gray-400 text-lg">Cargando solicitudes...</p>
          </div>

          <!-- Error -->
          <div v-else-if="error" class="text-center py-12">
            <div class="text-red-500 text-6xl mb-4">⚠️</div>
            <p class="text-red-400 mb-6 text-lg">{{ error }}</p>
            <button @click="loadContacts" class="px-6 py-3 bg-blue-600 text-white rounded-lg">
              🔄 Reintentar
            </button>
          </div>

          <!-- Solicitudes -->
          <div v-else-if="filteredContacts.length > 0" class="space-y-6">
            <div 
              v-for="(contact, index) in filteredContacts" 
              :key="contact.id"
              class="bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 transition-all"
            >
              <div class="flex items-start space-x-4">
                <!-- Avatar mejorado -->
                <div class="flex-shrink-0">
                  <div class="h-16 w-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                    <span class="text-xl font-bold text-white">{{ contact.name[0]?.toUpperCase() || '?' }}</span>
                  </div>
                </div>
                
                <!-- Contenido principal -->
                <div class="flex-1 min-w-0">
                  <div class="flex items-start justify-between mb-4">
                    <div>
                      <h3 class="text-2xl font-bold text-white mb-2">
                        📝 Solicitud #{{ index + 1 }}: {{ contact.name }}
                      </h3>
                      <p class="text-gray-400 text-sm">
                        📅 {{ formatDate(contact.created_at) }}
                      </p>
                    </div>
                    
                    <!-- Botones de acción -->
                    <div class="flex space-x-2">
                      <button
                        @click="downloadContactPDF(contact, index + 1)"
                        class="px-3 py-2 bg-green-600 hover:bg-green-700 text-white rounded text-sm font-medium"
                        title="Descargar PDF"
                      >
                        📄 PDF
                      </button>
                      <button
                        @click="replyToContact(contact)"
                        class="px-3 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm font-medium"
                        title="Responder por email"
                      >
                        📧 Responder
                      </button>
                    </div>
                  </div>
                  
                  <!-- Información de contacto -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
                    <div class="flex items-center space-x-2">
                      <span class="text-blue-400">📧</span>
                      <a :href="`mailto:${contact.email}`" class="text-blue-400 hover:text-blue-300 font-medium">
                        {{ contact.email }}
                      </a>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-green-400">📱</span>
                      <a :href="`tel:${contact.phone}`" class="text-green-400 hover:text-green-300 font-medium">
                        {{ contact.phone }}
                      </a>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-yellow-400">🏢</span>
                      <span class="text-white font-medium">{{ contact.company }}</span>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-purple-400">💰</span>
                      <span class="text-white font-medium">{{ contact.budget }}</span>
                    </div>
                  </div>
                  
                  <!-- Mensaje -->
                  <div class="mb-4">
                    <h4 class="text-sm font-medium text-gray-300 mb-2">💬 Mensaje:</h4>
                    <div class="bg-gray-700 rounded-lg p-4">
                      <p class="text-gray-200 leading-relaxed">{{ contact.message }}</p>
                    </div>
                  </div>

                  <!-- Imagen adjunta si existe -->
                  <div v-if="contact.file_path" class="mb-4">
                    <h4 class="text-sm font-medium text-gray-300 mb-2">📎 Archivo adjunto:</h4>
                    <div class="bg-gray-700 rounded-lg p-4">
                      <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                          <img 
                            v-if="isImageFile(contact.file_path)"
                            :src="getImageUrl(contact.file_path)" 
                            :alt="`Imagen de ${contact.name}`"
                            class="h-20 w-20 object-cover rounded-lg cursor-pointer"
                            @click="openImageModal(contact.file_path)"
                          />
                          <div v-else class="h-20 w-20 bg-gray-600 rounded-lg flex items-center justify-center">
                            <span class="text-gray-400">�</span>
                          </div>
                          <div>
                            <p class="text-white font-medium">{{ getFileName(contact.file_path) }}</p>
                            <p class="text-gray-400 text-sm">Archivo adjunto</p>
                          </div>
                        </div>
                        <button
                          @click="downloadFile(contact.file_path)"
                          class="px-4 py-2 bg-orange-600 hover:bg-orange-700 text-white rounded text-sm font-medium"
                        >
                          📥 Descargar
                        </button>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Tags -->
                  <div class="flex items-center space-x-2">
                    <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-purple-900 text-purple-200">
                      🎯 {{ contact.type }}
                    </span>
                    <span v-if="contact.referral" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-orange-900 text-orange-200">
                      👥 {{ contact.referral }}
                    </span>
                    <span v-if="contact.file_path" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-900 text-green-200">
                      📎 Con archivo
                    </span>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Resumen -->
            <div class="bg-gray-800 rounded-lg p-4 text-center">
              <p class="text-gray-400">
                📊 Mostrando {{ filteredContacts.length }} de {{ contacts.length }} solicitudes
              </p>
            </div>
          </div>

          <!-- Empty -->
          <div v-else class="text-center py-12">
            <div class="text-gray-500 text-6xl mb-4">📭</div>
            <p class="text-gray-400 text-lg">No hay solicitudes aún</p>
            <p class="text-gray-500 text-sm mt-2">Las solicitudes aparecerán aquí cuando los usuarios envíen el formulario</p>
          </div>
        </div>
      </div>

      <!-- SECCIÓN DASHBOARD DE VISITAS -->
      <div v-if="activeSection === 'dashboard'">
        <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
          <h2 class="text-3xl font-bold text-white mb-6">� DASHBOARD DE VISITAS Y ESTADÍSTICAS</h2>
          
          <!-- Stats Cards -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-6 text-white">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-blue-100 text-sm">Visitas Hoy</p>
                  <p class="text-3xl font-bold">{{ dashboardStats.visitasHoy }}</p>
                </div>
                <div class="text-4xl">👁️</div>
              </div>
            </div>

            <div class="bg-gradient-to-r from-green-600 to-green-700 rounded-xl p-6 text-white">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-green-100 text-sm">Total Solicitudes</p>
                  <p class="text-3xl font-bold">{{ contacts.length }}</p>
                </div>
                <div class="text-4xl">📨</div>
              </div>
            </div>

            <div class="bg-gradient-to-r from-purple-600 to-purple-700 rounded-xl p-6 text-white">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-purple-100 text-sm">Visitas Esta Semana</p>
                  <p class="text-3xl font-bold">{{ dashboardStats.visitasSemana }}</p>
                </div>
                <div class="text-4xl">📈</div>
              </div>
            </div>

            <div class="bg-gradient-to-r from-orange-600 to-orange-700 rounded-xl p-6 text-white">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-orange-100 text-sm">Tasa Conversión</p>
                  <p class="text-3xl font-bold">{{ dashboardStats.tasaConversion }}%</p>
                </div>
                <div class="text-4xl">🎯</div>
              </div>
            </div>
          </div>

          <!-- Gráficos simulados -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="bg-gray-800 rounded-xl p-6">
              <h3 class="text-xl font-bold text-white mb-4">📊 Visitas por Día (Últimos 7 días)</h3>
              <div class="space-y-3">
                <div v-for="(dia, index) in dashboardStats.visitasPorDia" :key="index" class="flex items-center justify-between">
                  <span class="text-gray-300">{{ dia.fecha }}</span>
                  <div class="flex items-center space-x-3">
                    <div class="w-32 bg-gray-700 rounded-full h-2">
                      <div 
                        class="bg-blue-500 h-2 rounded-full transition-all duration-300"
                        :style="{ width: `${(dia.visitas / Math.max(...dashboardStats.visitasPorDia.map(d => d.visitas))) * 100}%` }"
                      ></div>
                    </div>
                    <span class="text-white font-medium w-12 text-right">{{ dia.visitas }}</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="bg-gray-800 rounded-xl p-6">
              <h3 class="text-xl font-bold text-white mb-4">🌍 Países de Origen</h3>
              <div class="space-y-3">
                <div v-for="pais in dashboardStats.paisesMasVisitas" :key="pais.nombre" class="flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-2xl">{{ pais.bandera }}</span>
                    <span class="text-gray-300">{{ pais.nombre }}</span>
                  </div>
                  <div class="flex items-center space-x-3">
                    <div class="w-24 bg-gray-700 rounded-full h-2">
                      <div 
                        class="bg-green-500 h-2 rounded-full transition-all duration-300"
                        :style="{ width: `${(pais.visitas / Math.max(...dashboardStats.paisesMasVisitas.map(p => p.visitas))) * 100}%` }"
                      ></div>
                    </div>
                    <span class="text-white font-medium w-12 text-right">{{ pais.visitas }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Información del sistema -->
          <div class="mt-8 bg-gray-800 rounded-xl p-6">
            <h3 class="text-xl font-bold text-white mb-4">⚙️ Información del Sistema</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="text-center">
                <div class="text-3xl mb-2">�</div>
                <p class="text-gray-300 text-sm">Estado del Servidor</p>
                <p class="text-green-400 font-bold">OPERATIVO</p>
              </div>
              <div class="text-center">
                <div class="text-3xl mb-2">🔄</div>
                <p class="text-gray-300 text-sm">Última Actualización</p>
                <p class="text-white font-bold">{{ new Date().toLocaleTimeString('es-ES') }}</p>
              </div>
              <div class="text-center">
                <div class="text-3xl mb-2">💾</div>
                <p class="text-gray-300 text-sm">Base de Datos</p>
                <p class="text-blue-400 font-bold">CONECTADA</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para ver imagen completa -->
    <div v-if="showImageModal" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50" @click="closeImageModal">
      <div class="max-w-4xl max-h-full p-4">
        <div class="relative">
          <img 
            :src="modalImageSrc" 
            alt="Imagen completa" 
            class="max-w-full max-h-full object-contain rounded-lg"
          />
          <button 
            @click="closeImageModal"
            class="absolute top-4 right-4 bg-gray-900 text-white p-2 rounded-full hover:bg-gray-800"
          >
            ❌
          </button>
          <button 
            @click="downloadFile(modalImageSrc)"
            class="absolute bottom-4 right-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            📥 Descargar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import axios from 'axios'

interface Contact {
  id: number
  name: string
  email: string
  phone: string
  company: string
  type: string
  budget: string
  referral: string
  message: string
  file_path?: string
  created_at: string
}

const authStore = useAuthStore()
const contacts = ref<Contact[]>([])
const loading = ref(false)
const error = ref('')

// Navigation state
const activeSection = ref('bandeja')

// Filter and search state
const selectedType = ref('')
const searchTerm = ref('')

// Modal state
const showImageModal = ref(false)
const modalImageSrc = ref('')

// Dashboard stats (simulados por ahora)
const dashboardStats = ref({
  visitasHoy: 127,
  visitasSemana: 892,
  tasaConversion: 12.5,
  visitasPorDia: [
    { fecha: 'Lun', visitas: 145 },
    { fecha: 'Mar', visitas: 132 },
    { fecha: 'Mié', visitas: 167 },
    { fecha: 'Jue', visitas: 98 },
    { fecha: 'Vie', visitas: 203 },
    { fecha: 'Sáb', visitas: 87 },
    { fecha: 'Dom', visitas: 60 }
  ],
  paisesMasVisitas: [
    { nombre: 'Colombia', bandera: '🇨🇴', visitas: 342 },
    { nombre: 'Estados Unidos', bandera: '🇺🇸', visitas: 198 },
    { nombre: 'México', bandera: '🇲🇽', visitas: 156 },
    { nombre: 'España', bandera: '🇪🇸', visitas: 89 },
    { nombre: 'Argentina', bandera: '🇦🇷', visitas: 67 }
  ]
})

// Computed properties
const contactTypes = computed(() => {
  const types = contacts.value.map(contact => contact.type)
  return [...new Set(types)]
})

const filteredContacts = computed(() => {
  let filtered = contacts.value

  // Filter by type
  if (selectedType.value) {
    filtered = filtered.filter(contact => contact.type === selectedType.value)
  }

  // Filter by search term
  if (searchTerm.value) {
    const search = searchTerm.value.toLowerCase()
    filtered = filtered.filter(contact => 
      contact.name.toLowerCase().includes(search) ||
      contact.email.toLowerCase().includes(search) ||
      contact.company.toLowerCase().includes(search) ||
      contact.message.toLowerCase().includes(search)
    )
  }

  return filtered
})

const loadContacts = async () => {
  loading.value = true
  error.value = ''
  
  try {
    console.log('🚀 CARGANDO CONTACTOS...')
    
    const token = authStore.token
    if (!token) {
      error.value = 'No hay token de autenticación'
      return
    }

    const headers = { 
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
    
    const response = await axios.get('http://localhost:8000/api/admin/contacts', { headers })
    
    console.log('✅ RESPUESTA:', response.data)
    
    if (response.data && response.data.contacts) {
      contacts.value = response.data.contacts
      console.log(`🎯 SE CARGARON ${contacts.value.length} CONTACTOS`)
    } else if (Array.isArray(response.data)) {
      contacts.value = response.data
      console.log(`🎯 SE CARGARON ${contacts.value.length} CONTACTOS (array directo)`)
    } else {
      error.value = 'Formato de respuesta inválido'
      console.error('❌ Formato inválido:', response.data)
    }
    
  } catch (err: any) {
    console.error('❌ ERROR:', err)
    if (err.response?.status === 401) {
      error.value = 'Sesión expirada'
    } else {
      error.value = err.response?.data?.detail || err.message || 'Error desconocido'
    }
  } finally {
    loading.value = false
  }
}

// Utility functions
const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const isImageFile = (filePath: string) => {
  if (!filePath) return false
  const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']
  return imageExtensions.some(ext => filePath.toLowerCase().includes(ext))
}

const getImageUrl = (filePath: string) => {
  // Construir URL completa para la imagen
  return `http://localhost:8000/uploads/${filePath.split('/').pop()}`
}

const getFileName = (filePath: string) => {
  if (!filePath) return 'Archivo'
  return filePath.split('/').pop() || 'Archivo'
}

const downloadFile = async (filePath: string) => {
  try {
    const url = getImageUrl(filePath)
    const response = await fetch(url)
    const blob = await response.blob()
    
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = getFileName(filePath)
    link.click()
    
    URL.revokeObjectURL(link.href)
  } catch (error) {
    console.error('Error al descargar archivo:', error)
    alert('Error al descargar el archivo')
  }
}

const openImageModal = (filePath: string) => {
  modalImageSrc.value = getImageUrl(filePath)
  showImageModal.value = true
}

const closeImageModal = () => {
  showImageModal.value = false
  modalImageSrc.value = ''
}

const replyToContact = (contact: Contact) => {
  const subject = `Re: ${contact.type} - ${contact.name}`
  const body = `Hola ${contact.name},\n\nGracias por contactarnos respecto a ${contact.type}.\n\nNos pondremos en contacto contigo pronto.\n\nSaludos,\nEquipo de Cloud Fort Technologies`
  const mailtoLink = `mailto:${contact.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
  window.open(mailtoLink, '_blank')
}

const downloadContactPDF = async (contact: Contact, index: number) => {
  try {
    // Generar contenido HTML para el PDF
    const htmlContent = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <title>Solicitud ${index} - ${contact.name}</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; color: #333; }
          .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
          .company { font-size: 24px; font-weight: bold; margin-bottom: 5px; }
          .title { font-size: 18px; opacity: 0.9; }
          .section { margin-bottom: 25px; }
          .section-title { font-size: 16px; font-weight: bold; color: #667eea; margin-bottom: 10px; border-bottom: 2px solid #667eea; padding-bottom: 5px; }
          .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
          .info-item { padding: 10px; background: #f8f9fa; border-radius: 5px; }
          .info-label { font-weight: bold; color: #555; }
          .message-box { background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #667eea; }
          .footer { text-align: center; margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; }
          .date { color: #666; font-size: 14px; }
        </style>
      </head>
      <body>
        <div class="header">
          <div class="company">☁️ CLOUD FORT TECHNOLOGIES</div>
          <div class="title">Solicitud de Contacto #${index}</div>
        </div>
        
        <div class="section">
          <div class="section-title">📋 Información del Cliente</div>
          <div class="info-grid">
            <div class="info-item">
              <div class="info-label">👤 Nombre:</div>
              <div>${contact.name}</div>
            </div>
            <div class="info-item">
              <div class="info-label">📧 Email:</div>
              <div>${contact.email}</div>
            </div>
            <div class="info-item">
              <div class="info-label">📱 Teléfono:</div>
              <div>${contact.phone}</div>
            </div>
            <div class="info-item">
              <div class="info-label">🏢 Empresa:</div>
              <div>${contact.company}</div>
            </div>
            <div class="info-item">
              <div class="info-label">🎯 Tipo de Servicio:</div>
              <div>${contact.type}</div>
            </div>
            <div class="info-item">
              <div class="info-label">💰 Presupuesto:</div>
              <div>${contact.budget}</div>
            </div>
          </div>
          ${contact.referral ? `
          <div class="info-item">
            <div class="info-label">👥 Referencia:</div>
            <div>${contact.referral}</div>
          </div>
          ` : ''}
        </div>
        
        <div class="section">
          <div class="section-title">💬 Mensaje</div>
          <div class="message-box">
            ${contact.message}
          </div>
        </div>
        
        ${contact.file_path ? `
        <div class="section">
          <div class="section-title">📎 Archivo Adjunto</div>
          <div class="info-item">
            <div class="info-label">Archivo:</div>
            <div>${getFileName(contact.file_path)}</div>
          </div>
        </div>
        ` : ''}
        
        <div class="footer">
          <div class="date">📅 Fecha de solicitud: ${formatDate(contact.created_at)}</div>
          <div class="date">📄 Documento generado: ${new Date().toLocaleString('es-ES')}</div>
        </div>
      </body>
      </html>
    `
    
    // Crear un blob con el contenido HTML
    const blob = new Blob([htmlContent], { type: 'text/html' })
    const url = URL.createObjectURL(blob)
    
    // Crear y descargar el archivo
    const link = document.createElement('a')
    link.href = url
    link.download = `Solicitud_${index}_${contact.name.replace(/\s+/g, '_')}.html`
    link.click()
    
    URL.revokeObjectURL(url)
    
    alert(`📄 Descargando solicitud de ${contact.name} como archivo HTML`)
  } catch (error) {
    console.error('Error al generar PDF:', error)
    alert('Error al generar el PDF')
  }
}

const downloadAllContactsPDF = async () => {
  try {
    const htmlContent = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <title>Todas las Solicitudes - Cloud Fort Technologies</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; color: #333; }
          .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; text-align: center; }
          .company { font-size: 28px; font-weight: bold; margin-bottom: 10px; }
          .subtitle { font-size: 18px; opacity: 0.9; }
          .summary { background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 30px; text-align: center; }
          .contact { margin-bottom: 40px; padding: 20px; border: 2px solid #667eea; border-radius: 8px; page-break-inside: avoid; }
          .contact-header { font-size: 20px; font-weight: bold; color: #667eea; margin-bottom: 15px; }
          .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
          .info-item { padding: 10px; background: #f8f9fa; border-radius: 5px; }
          .info-label { font-weight: bold; color: #555; }
          .message-box { background: #f0f8ff; padding: 15px; border-radius: 8px; border-left: 4px solid #667eea; margin-top: 15px; }
          .footer { text-align: center; margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; }
        </style>
      </head>
      <body>
        <div class="header">
          <div class="company">☁️ CLOUD FORT TECHNOLOGIES</div>
          <div class="subtitle">Reporte Completo de Solicitudes</div>
        </div>
        
        <div class="summary">
          <h2>📊 Resumen General</h2>
          <p><strong>Total de solicitudes:</strong> ${contacts.value.length}</p>
          <p><strong>Fecha del reporte:</strong> ${new Date().toLocaleString('es-ES')}</p>
        </div>
        
        ${contacts.value.map((contact, index) => `
          <div class="contact">
            <div class="contact-header">📝 Solicitud #${index + 1}: ${contact.name}</div>
            <div class="info-grid">
              <div class="info-item">
                <div class="info-label">📧 Email:</div>
                <div>${contact.email}</div>
              </div>
              <div class="info-item">
                <div class="info-label">📱 Teléfono:</div>
                <div>${contact.phone}</div>
              </div>
              <div class="info-item">
                <div class="info-label">🏢 Empresa:</div>
                <div>${contact.company}</div>
              </div>
              <div class="info-item">
                <div class="info-label">🎯 Tipo:</div>
                <div>${contact.type}</div>
              </div>
              <div class="info-item">
                <div class="info-label">💰 Presupuesto:</div>
                <div>${contact.budget}</div>
              </div>
              <div class="info-item">
                <div class="info-label">📅 Fecha:</div>
                <div>${formatDate(contact.created_at)}</div>
              </div>
            </div>
            ${contact.referral ? `
            <div class="info-item">
              <div class="info-label">👥 Referencia:</div>
              <div>${contact.referral}</div>
            </div>
            ` : ''}
            <div class="message-box">
              <div class="info-label">💬 Mensaje:</div>
              <div>${contact.message}</div>
            </div>
            ${contact.file_path ? `
            <div style="margin-top: 10px;">
              <div class="info-label">📎 Archivo adjunto:</div>
              <div>${getFileName(contact.file_path)}</div>
            </div>
            ` : ''}
          </div>
        `).join('')}
        
        <div class="footer">
          <p>� Documento generado automáticamente por Cloud Fort Technologies</p>
          <p>📅 ${new Date().toLocaleString('es-ES')}</p>
        </div>
      </body>
      </html>
    `
    
    const blob = new Blob([htmlContent], { type: 'text/html' })
    const url = URL.createObjectURL(blob)
    
    const link = document.createElement('a')
    link.href = url
    link.download = `Todas_las_Solicitudes_${new Date().toISOString().split('T')[0]}.html`
    link.click()
    
    URL.revokeObjectURL(url)
    
    alert(`📄 Descargando reporte completo de ${contacts.value.length} solicitudes`)
  } catch (error) {
    console.error('Error al generar reporte:', error)
    alert('Error al generar el reporte')
  }
}

onMounted(() => {
  console.log('🔍 Bandeja de Entrada montada, cargando contactos...')
  loadContacts()
})
</script>
