<template>
  <nav role="navigation" class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-lg border-b border-gray-200/50 shadow-xl">
    <!-- Status Panel Moderno -->
    <div class="absolute top-2 left-4 text-xs font-mono text-indigo-600">
      <div class="flex items-center gap-2">
        <div class="w-2 h-2 bg-indigo-600 rounded-full animate-pulse"></div>
        <span class="font-medium">ONLINE</span>
      </div>
    </div>
    
    <!-- Gradiente Decorativo -->
    <div class="absolute inset-0 overflow-hidden opacity-10">
      <div class="gradient-bg"></div>
    </div>
    
    <div class="px-6 md:px-12 py-4 relative z-10">
      <div class="flex items-center justify-between">
        <!-- Logo Original VARNOX -->
        <div class="flex items-center gap-x-3">
          <img src="/src/assets/logo.png" alt="VARNOX Logo" class="w-14 h-14" />
          <div class="text-gray-800 font-bold text-sm md:text-base leading-tight font-orbitron">
            <div class="tracking-wider bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">VARNOX</div>
          </div>
        </div>

        <!-- Menu Desktop Moderno -->
        <div class="hidden md:flex items-center space-x-8">
          <a
            href="#hero"
            class="nav-link text-gray-700 hover:text-indigo-600 transition-all duration-300 font-poppins text-base font-medium tracking-wide"
          >
            Inicio
          </a>
          <a
            href="#servicios"
            class="nav-link text-gray-700 hover:text-indigo-600 transition-all duration-300 font-poppins text-base font-medium tracking-wide"
          >
            Servicios
          </a>
          <a
            href="#nosotros"
            class="nav-link text-gray-700 hover:text-indigo-600 transition-all duration-300 font-poppins text-base font-medium tracking-wide"
          >
            Nosotros
          </a>
          <a
            href="#proyectos"
            class="nav-link text-gray-700 hover:text-indigo-600 transition-all duration-300 font-poppins text-base font-medium tracking-wide"
          >
            Proyectos
          </a>
          <a
            href="#proceso"
            class="nav-link text-gray-700 hover:text-indigo-600 transition-all duration-300 font-poppins text-base font-medium tracking-wide"
          >
            Proceso
          </a>
          <a
            href="#contacto"
            class="nav-link text-gray-700 hover:text-indigo-600 transition-all duration-300 font-poppins text-base font-medium tracking-wide"
          >
            Contacto
          </a>
          
          <!-- Botón CTA Moderno -->
          <button
            @click="scrollToContact"
            class="cta-btn bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-6 py-2 rounded-lg hover:shadow-lg hover:shadow-indigo-500/25 transition-all duration-300 font-poppins font-semibold tracking-wide"
          >
            Comenzar Proyecto
          </button>
        </div>

        <!-- Botón Hamburguesa Moderno -->
        <button
          @click="toggleMobileMenu"
          class="md:hidden text-indigo-600 focus:outline-none hover:text-purple-600 transition-colors duration-300"
          aria-label="Toggle menu"
        >
          <div class="flex flex-col gap-1">
            <div class="w-6 h-0.5 bg-current transition-all duration-300" :class="{ 'rotate-45 translate-y-2': isOpen }"></div>
            <div class="w-6 h-0.5 bg-current transition-all duration-300" :class="{ 'opacity-0': isOpen }"></div>
            <div class="w-6 h-0.5 bg-current transition-all duration-300" :class="{ '-rotate-45 -translate-y-2': isOpen }"></div>
          </div>
        </button>
      </div>

      <!-- Menu Mobile Moderno -->
      <Transition
        enter-active-class="transition ease-out duration-300 transform"
        enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition ease-in duration-200 transform"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-4"
      >
        <div
          v-show="isOpen"
          class="md:hidden mt-4 bg-white/95 backdrop-blur-md rounded-lg border border-gray-200/50 p-4 shadow-xl"
        >
          <div class="flex flex-col space-y-3">
            <a
              href="#hero"
              @click="closeMobileMenu"
              class="text-gray-700 hover:text-indigo-600 transition-colors duration-300 py-2 border-b border-gray-200/50 font-poppins text-base font-medium"
            >
              Inicio
            </a>
            <a
              href="#servicios"
              @click="closeMobileMenu"
              class="text-gray-700 hover:text-indigo-600 transition-colors duration-300 py-2 border-b border-gray-200/50 font-poppins text-base font-medium"
            >
              Servicios
            </a>
            <a
              href="#nosotros"
              @click="closeMobileMenu"
              class="text-gray-700 hover:text-indigo-600 transition-colors duration-300 py-2 border-b border-gray-200/50 font-poppins text-base font-medium"
            >
              Nosotros
            </a>
            <a
              href="#proyectos"
              @click="closeMobileMenu"
              class="text-gray-700 hover:text-indigo-600 transition-colors duration-300 py-2 border-b border-gray-200/50 font-poppins text-base font-medium"
            >
              Proyectos
            </a>
            <a
              href="#proceso"
              @click="closeMobileMenu"
              class="text-gray-700 hover:text-indigo-600 transition-colors duration-300 py-2 border-b border-gray-200/50 font-poppins text-base font-medium"
            >
              Proceso
            </a>
            <a
              href="#contacto"
              @click="closeMobileMenu"
              class="text-gray-700 hover:text-indigo-600 transition-colors duration-300 py-2 border-b border-gray-200/50 font-poppins text-base font-medium"
            >
              Contacto
            </a>
            
            <!-- Botón CTA Mobile -->
            <button
              @click="scrollToContact"
              class="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-4 py-3 rounded-lg hover:shadow-lg transition-all duration-300 text-center mt-4 font-poppins font-semibold tracking-wide"
            >
              Comenzar Proyecto
            </button>
          </div>
        </div>
      </Transition>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

// Estado reactivo para el menú móvil
const isOpen = ref<boolean>(false)

// Funciones para manejar el menú móvil
const toggleMobileMenu = (): void => {
  isOpen.value = !isOpen.value
}

const closeMobileMenu = (): void => {
  isOpen.value = false
}

// Función para scroll a contacto
const scrollToContact = (): void => {
  const contactSection = document.getElementById('contacto')
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' })
  }
  closeMobileMenu()
}

// Función para cerrar el menú al hacer clic fuera
const handleClickOutside = (event: Event): void => {
  const target = event.target as HTMLElement
  const navbar = document.querySelector('nav')
  
  if (navbar && !navbar.contains(target)) {
    isOpen.value = false
  }
}

// Lifecycle hooks
onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
/* Sistema de Tipografía Diferenciado */
.font-orbitron {
  font-family: 'Orbitron', monospace;
  letter-spacing: 0.05em;
}

.font-poppins {
  font-family: 'Poppins', sans-serif;
  letter-spacing: 0.025em;
}

/* Gradiente Decorativo */
.gradient-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, 
    rgba(99, 102, 241, 0.1) 0%, 
    rgba(139, 92, 246, 0.1) 50%, 
    rgba(245, 158, 11, 0.1) 100%);
  background-size: 400% 400%;
  animation: gradient-shift 8s ease infinite;
}

@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Efectos de Enlaces de Navegación */
.nav-link {
  position: relative;
  overflow: hidden;
}

.nav-link::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #6366F1, #8B5CF6, transparent);
  transition: left 0.3s ease;
}

.nav-link:hover::before {
  left: 100%;
}

/* Efectos del Botón CTA */
.cta-btn {
  position: relative;
  overflow: hidden;
  transform: translateY(0);
}

.cta-btn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.cta-btn:hover::before {
  width: 300px;
  height: 300px;
}

.cta-btn:hover {
  transform: translateY(-1px);
}

/* Animaciones del Menú Mobile */
.md\:hidden div {
  transition: transform 0.3s ease;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .gradient-bg {
    background-size: 200% 200%;
  }
}
</style>