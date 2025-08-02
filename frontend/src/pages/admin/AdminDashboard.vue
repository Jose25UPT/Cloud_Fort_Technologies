<template>
  <AdminLayout>
    <!-- Navigation Tabs -->
    <div class="bg-gray-800 border-b border-gray-700 -mt-6 mb-6">
      <div class="max-w-7xl mx-auto px-4">
        <nav class="flex space-x-1">
          <button
            @click="activeTab = 'dashboard'"
            :class="[
              'px-6 py-4 text-sm font-medium transition-colors border-b-2',
              activeTab === 'dashboard' 
                ? 'text-white border-blue-500 bg-gray-900' 
                : 'text-gray-400 hover:text-white border-transparent hover:border-gray-600'
            ]"
          >
            📊 Dashboard Principal
          </button>
          <button
            @click="activeTab = 'solicitudes'"
            :class="[
              'px-6 py-4 text-sm font-medium transition-colors border-b-2 relative',
              activeTab === 'solicitudes' 
                ? 'text-white border-blue-500 bg-gray-900' 
                : 'text-gray-400 hover:text-white border-transparent hover:border-gray-600'
            ]"
          >
            📨 BANDEJA DE ENTRADA
            <span v-if="contacts.length > 0" class="absolute -top-1 -right-1 bg-red-500 text-white text-xs px-2 py-1 rounded-full font-bold animate-pulse">
              {{ contacts.length }}
            </span>
          </button>
          <button
            @click="activeTab = 'contenido'"
            :class="[
              'px-6 py-4 text-sm font-medium transition-colors border-b-2',
              activeTab === 'contenido' 
                ? 'text-white border-blue-500 bg-gray-900' 
                : 'text-gray-400 hover:text-white border-transparent hover:border-gray-600'
            ]"
          >
            📝 Gestión de Contenido
          </button>
        </nav>
      </div>
    </div>

    <!-- Tab Content -->
    <div v-if="activeTab === 'dashboard'" class="space-y-6">
      <!-- Header Section -->
      <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl p-6 text-white">
        <h1 class="text-3xl font-bold mb-2">🏢 Panel de Administración</h1>
        <p class="text-blue-100">
          Gestiona todos los aspectos de Cloud Fort Technologies desde aquí
        </p>
        <div class="mt-4 flex items-center space-x-6 text-sm">
          <div class="flex items-center">
            <span class="inline-block w-2 h-2 bg-green-400 rounded-full mr-2"></span>
            Sistema operativo
          </div>
          <div class="flex items-center">
            <span class="inline-block w-2 h-2 bg-blue-400 rounded-full mr-2"></span>
            {{ contacts.length }} mensajes pendientes
          </div>
          <div class="flex items-center">
            <span class="inline-block w-2 h-2 bg-yellow-400 rounded-full mr-2"></span>
            Última actualización: {{ new Date().toLocaleTimeString('es-ES') }}
          </div>
        </div>
      </div>

      <!-- Stats Cards -->      <!-- Stats Cards -->
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
              <p class="text-sm font-medium text-gray-400">Mensajes</p>
              <p class="text-2xl font-semibold text-white">{{ contacts.length }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 📨 SOLICITUDES Y MENSAJES -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-semibold text-white">📨 SOLICITUDES DE CONTACTO</h2>
          <div class="flex items-center space-x-3">
            <span class="text-sm text-gray-400">Total: {{ contacts.length }}</span>
            <button
              @click="loadContacts"
              class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm"
            >
              🔄 Actualizar
            </button>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loadingContacts" class="text-center py-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p class="text-gray-400 text-lg">Cargando solicitudes...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="contactsError" class="text-center py-12">
          <div class="text-red-500 text-6xl mb-4">⚠️</div>
          <p class="text-red-400 mb-6 text-lg">{{ contactsError }}</p>
          <button 
            @click="loadContacts" 
            class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            🔄 Reintentar
          </button>
        </div>

        <!-- Empty State -->
        <div v-else-if="contacts.length === 0" class="text-center py-12">
          <div class="text-gray-500 text-6xl mb-4">📭</div>
          <p class="text-gray-400 text-lg">No hay solicitudes aún</p>
          <p class="text-gray-500 text-sm mt-2">Las solicitudes aparecerán aquí cuando los usuarios envíen el formulario</p>
        </div>

        <!-- Contacts List -->
        <div v-else class="space-y-6">
          <!-- Search and Filters -->
          <div class="bg-gray-800 rounded-lg p-4">
            <div class="flex flex-wrap items-center gap-4">
              <div class="flex items-center space-x-2">
                <label class="text-sm text-gray-300">� Buscar:</label>
                <input 
                  v-model="searchTerm"
                  type="text" 
                  placeholder="Nombre, email, empresa..."
                  class="bg-gray-700 text-white px-3 py-2 rounded text-sm w-64"
                >
              </div>
              <div class="flex items-center space-x-2">
                <label class="text-sm text-gray-300">🎯 Filtrar por tipo:</label>
                <select 
                  v-model="selectedType" 
                  class="bg-gray-700 text-white px-3 py-2 rounded text-sm"
                >
                  <option value="">Todos los tipos</option>
                  <option v-for="type in contactTypes" :key="type" :value="type">{{ type }}</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Contacts -->
          <div class="space-y-4">
            <div 
              v-for="(contact, index) in filteredContacts" 
              :key="contact.id"
              class="bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 transition-colors"
            >
              <div class="flex items-start space-x-4">
                <!-- Avatar -->
                <div class="flex-shrink-0">
                  <div class="h-16 w-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                    <span class="text-xl font-bold text-white">{{ contact.name[0]?.toUpperCase() || '?' }}</span>
                  </div>
                </div>
                
                <!-- Content -->
                <div class="flex-1 min-w-0">
                  <div class="flex items-start justify-between mb-3">
                    <div>
                      <h3 class="text-xl font-semibold text-white mb-1">
                        📝 Solicitud #{{ index + 1 }}: {{ contact.name }}
                      </h3>
                      <p class="text-gray-400 text-sm">
                        📅 {{ formatDate(contact.created_at) }}
                      </p>
                    </div>
                  </div>
                  
                  <!-- Contact Details -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
                    <div class="flex items-center space-x-2">
                      <span class="text-blue-400">📧</span>
                      <a :href="`mailto:${contact.email}`" class="text-blue-400 hover:text-blue-300">
                        {{ contact.email }}
                      </a>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-green-400">📱</span>
                      <a :href="`tel:${contact.phone}`" class="text-green-400 hover:text-green-300">
                        {{ contact.phone }}
                      </a>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-yellow-400">🏢</span>
                      <span class="text-white">{{ contact.company }}</span>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-purple-400">💰</span>
                      <span class="text-white">{{ contact.budget }}</span>
                    </div>
                  </div>
                  
                  <!-- Message -->
                  <div class="mb-4">
                    <h4 class="text-sm font-medium text-gray-300 mb-2">💬 Mensaje:</h4>
                    <div class="bg-gray-700 rounded-lg p-4">
                      <p class="text-gray-200">{{ contact.message }}</p>
                    </div>
                  </div>
                  
                  <!-- Tags and Actions -->
                  <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                      <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-purple-900 text-purple-200">
                        🎯 {{ contact.type }}
                      </span>
                      <span v-if="contact.referral" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-orange-900 text-orange-200">
                        👥 {{ contact.referral }}
                      </span>
                      <span v-if="contact.file_path" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-900 text-green-200">
                        📎 Archivo adjunto
                      </span>
                    </div>
                    
                    <!-- Action Buttons -->
                    <div class="flex items-center space-x-3">
                      <button
                        @click="replyToContact(contact)"
                        class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm transition-colors"
                      >
                        📧 Responder
                      </button>
                      <button
                        @click="markAsProcessed(contact)"
                        class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg text-sm transition-colors"
                      >
                        ✅ Marcar como Procesado
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Summary -->
          <div class="bg-gray-800 rounded-lg p-4 text-center">
            <p class="text-gray-400">
              📊 Mostrando {{ filteredContacts.length }} de {{ contacts.length }} solicitudes
            </p>
          </div>
        </div>
      </div>

      <!-- Quick Actions Section -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <h2 class="text-2xl font-semibold text-white mb-6">⚡ Acciones Rápidas</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <router-link
            to="/login/admin"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-blue-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <PhotoIcon class="h-8 w-8 text-blue-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Dashboard</h3>
            </div>
            <p class="text-gray-400 text-sm">Panel principal de administración</p>
          </router-link>

          <router-link
            to="/login/admin/hero"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-green-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <PhotoIcon class="h-8 w-8 text-green-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Hero Principal</h3>
            </div>
            <p class="text-gray-400 text-sm">Editar sección principal del sitio</p>
          </router-link>

          <router-link
            to="/login/admin/servicios"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-yellow-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <WrenchScrewdriverIcon class="h-8 w-8 text-yellow-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Servicios</h3>
            </div>
            <p class="text-gray-400 text-sm">Gestionar servicios ofrecidos</p>
          </router-link>

          <router-link
            to="/login/admin/proyectos"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-purple-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <BriefcaseIcon class="h-8 w-8 text-purple-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Proyectos</h3>
            </div>
            <p class="text-gray-400 text-sm">Gestionar portafolio de proyectos</p>
          </router-link>

          <router-link
            to="/login/admin/testimonios"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-pink-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <ChatBubbleLeftRightIcon class="h-8 w-8 text-pink-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Testimonios</h3>
            </div>
            <p class="text-gray-400 text-sm">Gestionar reseñas de clientes</p>
          </router-link>

          <router-link
            to="/login/admin/contacto"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-indigo-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <BuildingOfficeIcon class="h-8 w-8 text-indigo-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Contactos</h3>
            </div>
            <p class="text-gray-400 text-sm">Información de contacto</p>
          </router-link>

          <div class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-orange-500 transition-all duration-200 cursor-pointer">
            <div class="flex items-center mb-3">
              <InboxIcon class="h-8 w-8 text-orange-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Solicitudes</h3>
            </div>
            <p class="text-gray-400 text-sm">Ver todas las solicitudes aquí mismo</p>
          </div>

          <router-link
            to="/login/admin/configuracion"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-red-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <PlusIcon class="h-8 w-8 text-red-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Configuración</h3>
            </div>
            <p class="text-gray-400 text-sm">Ajustes del sistema</p>
          </router-link>
        </div>
      </div>
    </div>

    <!-- SOLICITUDES TAB -->
    <div v-if="activeTab === 'solicitudes'" class="space-y-6">
      <!-- 📨 SOLICITUDES DE CONTACTO -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-3xl font-bold text-white">📨 BANDEJA DE ENTRADA - SOLICITUDES</h2>
          <div class="flex items-center space-x-3">
            <span class="text-lg text-gray-400">Total: <span class="text-white font-bold">{{ contacts.length }}</span></span>
            <button
              @click="loadContacts"
              class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm font-medium"
            >
              🔄 Actualizar
            </button>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loadingContacts" class="text-center py-12">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p class="text-gray-400 text-lg">Cargando solicitudes...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="contactsError" class="text-center py-12">
          <div class="text-red-500 text-6xl mb-4">⚠️</div>
          <p class="text-red-400 mb-6 text-lg">{{ contactsError }}</p>
          <button 
            @click="loadContacts" 
            class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            🔄 Reintentar
          </button>
        </div>

        <!-- Empty State -->
        <div v-else-if="contacts.length === 0" class="text-center py-12">
          <div class="text-gray-500 text-6xl mb-4">📭</div>
          <p class="text-gray-400 text-lg">No hay solicitudes aún</p>
          <p class="text-gray-500 text-sm mt-2">Las solicitudes aparecerán aquí cuando los usuarios envíen el formulario</p>
        </div>

        <!-- Contacts List -->
        <div v-else class="space-y-6">
          <!-- Search and Filters -->
          <div class="bg-gray-800 rounded-lg p-4">
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
                <label class="text-sm text-gray-300">🎯 Filtrar por tipo:</label>
                <select 
                  v-model="selectedType" 
                  class="bg-gray-700 text-white px-3 py-2 rounded text-sm"
                >
                  <option value="">Todos los tipos</option>
                  <option v-for="type in contactTypes" :key="type" :value="type">{{ type }}</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Contacts -->
          <div class="space-y-4">
            <div 
              v-for="(contact, index) in filteredContacts" 
              :key="contact.id"
              class="bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 transition-colors"
            >
              <div class="flex items-start space-x-4">
                <!-- Avatar -->
                <div class="flex-shrink-0">
                  <div class="h-16 w-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                    <span class="text-xl font-bold text-white">{{ contact.name[0]?.toUpperCase() || '?' }}</span>
                  </div>
                </div>
                
                <!-- Content -->
                <div class="flex-1 min-w-0">
                  <div class="flex items-start justify-between mb-3">
                    <div>
                      <h3 class="text-xl font-semibold text-white mb-1">
                        📝 Solicitud #{{ index + 1 }}: {{ contact.name }}
                      </h3>
                      <p class="text-gray-400 text-sm">
                        📅 {{ formatDate(contact.created_at) }}
                      </p>
                    </div>
                  </div>
                  
                  <!-- Contact Details -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
                    <div class="flex items-center space-x-2">
                      <span class="text-blue-400">📧</span>
                      <a :href="`mailto:${contact.email}`" class="text-blue-400 hover:text-blue-300">
                        {{ contact.email }}
                      </a>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-green-400">📱</span>
                      <a :href="`tel:${contact.phone}`" class="text-green-400 hover:text-green-300">
                        {{ contact.phone }}
                      </a>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-yellow-400">🏢</span>
                      <span class="text-white">{{ contact.company }}</span>
                    </div>
                    <div class="flex items-center space-x-2">
                      <span class="text-purple-400">💰</span>
                      <span class="text-white">{{ contact.budget }}</span>
                    </div>
                  </div>
                  
                  <!-- Message -->
                  <div class="mb-4">
                    <h4 class="text-sm font-medium text-gray-300 mb-2">💬 Mensaje:</h4>
                    <div class="bg-gray-700 rounded-lg p-4">
                      <p class="text-gray-200">{{ contact.message }}</p>
                    </div>
                  </div>
                  
                  <!-- Tags and Actions -->
                  <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                      <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-purple-900 text-purple-200">
                        🎯 {{ contact.type }}
                      </span>
                      <span v-if="contact.referral" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-orange-900 text-orange-200">
                        👥 {{ contact.referral }}
                      </span>
                      <span v-if="contact.file_path" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-900 text-green-200">
                        📎 Archivo adjunto
                      </span>
                    </div>
                    
                    <!-- Action Buttons -->
                    <div class="flex items-center space-x-3">
                      <button
                        @click="replyToContact(contact)"
                        class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm transition-colors"
                      >
                        📧 Responder
                      </button>
                      <button
                        @click="markAsProcessed(contact)"
                        class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg text-sm transition-colors"
                      >
                        ✅ Marcar como Procesado
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Summary -->
          <div class="bg-gray-800 rounded-lg p-4 text-center">
            <p class="text-gray-400">
              📊 Mostrando {{ filteredContacts.length }} de {{ contacts.length }} solicitudes
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- CONTENIDO TAB -->
    <div v-if="activeTab === 'contenido'" class="space-y-6">
      <div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <h2 class="text-2xl font-semibold text-white mb-6">📝 Gestión de Contenido</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <router-link
            to="/login/admin/hero"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-green-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <PhotoIcon class="h-8 w-8 text-green-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Hero Principal</h3>
            </div>
            <p class="text-gray-400 text-sm">Editar sección principal del sitio</p>
          </router-link>

          <router-link
            to="/login/admin/servicios"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-yellow-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <WrenchScrewdriverIcon class="h-8 w-8 text-yellow-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Servicios</h3>
            </div>
            <p class="text-gray-400 text-sm">Gestionar servicios ofrecidos</p>
          </router-link>

          <router-link
            to="/login/admin/proyectos"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-purple-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <BriefcaseIcon class="h-8 w-8 text-purple-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Proyectos</h3>
            </div>
            <p class="text-gray-400 text-sm">Gestionar portafolio de proyectos</p>
          </router-link>

          <router-link
            to="/login/admin/testimonios"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-pink-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <ChatBubbleLeftRightIcon class="h-8 w-8 text-pink-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Testimonios</h3>
            </div>
            <p class="text-gray-400 text-sm">Gestionar reseñas de clientes</p>
          </router-link>

          <router-link
            to="/login/admin/configuracion"
            class="group bg-gray-800 border border-gray-700 rounded-lg p-6 hover:bg-gray-750 hover:border-red-500 transition-all duration-200"
          >
            <div class="flex items-center mb-3">
              <PlusIcon class="h-8 w-8 text-red-500 mr-3 group-hover:scale-110 transition-transform" />
              <h3 class="text-lg font-semibold text-white">Configuración</h3>
            </div>
            <p class="text-gray-400 text-sm">Ajustes del sistema</p>
          </router-link>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAdminStore } from '@/stores/admin'
import { useAuthStore } from '@/stores/auth'
import AdminLayout from '@/components/admin/AdminLayout.vue'
import axios from 'axios'
import {
  WrenchScrewdriverIcon,
  BriefcaseIcon,
  ChatBubbleLeftRightIcon,
  InboxIcon,
  PhotoIcon,
  PlusIcon,
  BuildingOfficeIcon
} from '@heroicons/vue/24/outline'

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

const adminStore = useAdminStore()
const authStore = useAuthStore()
const router = useRouter()

// Navigation state
const activeTab = ref('solicitudes') // Empezar en la bandeja de entrada

// Contacts state
const contacts = ref<Contact[]>([])
const loadingContacts = ref(false)
const contactsError = ref('')

// Filter and search state
const selectedType = ref('')
const searchTerm = ref('')

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

const API_BASE_URL = 'http://localhost:8000'

// Load contacts directly
const loadContacts = async () => {
  loadingContacts.value = true
  contactsError.value = ''
  
  console.log('🚀 INICIANDO CARGA DE CONTACTOS...')
  
  try {
    // Verificar autenticación primero
    if (!authStore.isAuthenticated) {
      console.error('❌ Usuario no autenticado')
      contactsError.value = 'Usuario no autenticado'
      return
    }

    const token = authStore.token
    console.log('🔐 Token disponible:', !!token)
    console.log('🔑 Token (primeros 20 chars):', token?.substring(0, 20) + '...')
    
    if (!token) {
      console.error('❌ No hay token disponible')
      contactsError.value = 'No hay token de autenticación'
      return
    }

    const headers = { 
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
    
    console.log('📡 Haciendo request a:', `${API_BASE_URL}/api/admin/contacts`)
    console.log('🔗 Headers:', { Authorization: `Bearer ${token.substring(0, 20)}...` })
    
    const response = await axios.get(`${API_BASE_URL}/api/admin/contacts`, { headers })
    
    console.log('✅ RESPUESTA DEL SERVIDOR:', {
      status: response.status,
      statusText: response.statusText,
      data: response.data,
      dataType: typeof response.data,
      isArray: Array.isArray(response.data)
    })
    
    // El backend devuelve un objeto con propiedad contacts: {contacts: [...]}
    if (response.data && response.data.contacts && Array.isArray(response.data.contacts)) {
      contacts.value = response.data.contacts
      
      console.log(`🎯 ÉXITO TOTAL: Se cargaron ${contacts.value.length} contactos`)
      console.log('📋 Tipos disponibles:', contactTypes.value)
      
      // Debug del primer contacto
      if (contacts.value.length > 0) {
        console.log('📝 Primer contacto completo:', contacts.value[0])
      }
    } else if (Array.isArray(response.data)) {
      // Fallback: si la respuesta es directamente un array
      contacts.value = response.data
      console.log(`🎯 ÉXITO (fallback): Se cargaron ${contacts.value.length} contactos`)
    } else {
      console.error('❌ Respuesta no tiene formato válido:', response.data)
      contactsError.value = 'Formato de respuesta inválido del servidor'
      contacts.value = []
    }
    
  } catch (err: any) {
    console.error('❌ ERROR COMPLETO AL CARGAR CONTACTOS:', {
      message: err.message,
      status: err.response?.status,
      statusText: err.response?.statusText,
      data: err.response?.data,
      headers: err.response?.headers
    })
    
    if (err.response?.status === 401) {
      contactsError.value = '🔒 Sesión expirada. Redirigiendo...'
      authStore.logout()
      router.push('/login/admin')
    } else if (err.response?.status === 403) {
      contactsError.value = '🚫 Sin permisos para ver contactos'
    } else if (err.response?.status === 404) {
      contactsError.value = '🔍 Endpoint de contactos no encontrado'
    } else {
      contactsError.value = err.response?.data?.detail || err.message || 'Error desconocido'
    }
    
    contacts.value = []
  } finally {
    loadingContacts.value = false
    console.log('🏁 Carga finalizada. Total contactos:', contacts.value.length)
  }
}

// Contact actions
const replyToContact = (contact: Contact) => {
  const subject = `Re: ${contact.type} - ${contact.name}`
  const body = `Hola ${contact.name},\n\nGracias por contactarnos respecto a ${contact.type}.\n\nSaludos,\nCloud Fort Technologies`
  const mailtoLink = `mailto:${contact.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
  window.open(mailtoLink, '_blank')
}

const markAsProcessed = (contact: Contact) => {
  // Aquí puedes agregar lógica para marcar como procesado
  alert(`Contacto de ${contact.name} marcado como procesado`)
  // TODO: Implementar API call para marcar como procesado
}

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
    loadContacts() // Load contacts directly instead of using adminStore
  ])
})
</script>
