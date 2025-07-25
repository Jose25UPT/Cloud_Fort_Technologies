<template>
  <nav role="navigation" class="sticky top-0 z-50 bg-black/80 backdrop-blur-sm shadow-md">
    <div class="px-6 md:px-12 py-4">
      <div class="flex items-center justify-between">
        <!-- Logo -->
        <div class="flex items-center gap-x-3">
          <img src="/src/assets/logo.png" alt="Cloud Fort Logo" class="w-14 h-124" />
          <div class="text-white font-bold text-sm md:text-base leading-tight font-sans">
            <div class="tracking-wider">CLOUD FORT</div>
            <div class="text-center text-[10px] md:text-xs tracking-wide">TECHNOLOGIES</div>
          </div>
        </div>

        <!-- Menú Desktop -->
        <div class="hidden md:flex items-center space-x-6">
          <a
            href="#hero"
            class="text-white hover:text-blue-400 hover:underline transition-all duration-300"
          >
            Inicio
          </a>
          <a
            href="#nosotros"
            class="text-white hover:text-blue-400 hover:underline transition-all duration-300"
          >
            Nosotros
          </a>
          <a
            href="#servicios"
            class="text-white hover:text-blue-400 hover:underline transition-all duration-300"
          >
            Servicios
          </a>
          <a
            href="#proyectos"
            class="text-white hover:text-blue-400 hover:underline transition-all duration-300"
          >
            Proyectos
          </a>
          <a
            href="#proceso"
            class="text-white hover:text-blue-400 hover:underline transition-all duration-300"
          >
            Proceso
          </a>
          <a
            href="#contacto"
            class="text-white hover:text-blue-400 hover:underline transition-all duration-300"
          >
            Contacto
          </a>
          
          <!-- Botón Especial Contáctanos -->
          <a
            href="#contacto"
            class="bg-[#0A84FF] text-white px-4 py-2 rounded-lg hover:brightness-110 transition-all duration-300 font-medium"
          >
            Contáctanos
          </a>
        </div>

        <!-- Botón Hamburger (Móvil) -->
        <button
          @click="toggleMobileMenu"
          class="md:hidden text-white focus:outline-none focus:text-blue-400 transition-colors duration-300"
          aria-label="Toggle mobile menu"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              v-if="!isOpen"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
            <path
              v-else
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            ></path>
          </svg>
        </button>
      </div>

      <!-- Menú Móvil -->
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
          class="md:hidden mt-4 bg-black rounded-lg p-4 shadow-lg border border-gray-800"
        >
          <div class="flex flex-col space-y-4">
            <a
              href="#hero"
              @click="closeMobileMenu"
              class="text-white hover:text-blue-400 transition-colors duration-300 py-2 border-b border-gray-800"
            >
              Inicio
            </a>
            <a
              href="#nosotros"
              @click="closeMobileMenu"
              class="text-white hover:text-blue-400 transition-colors duration-300 py-2 border-b border-gray-800"
            >
              Nosotros
            </a>
            <a
              href="#servicios"
              @click="closeMobileMenu"
              class="text-white hover:text-blue-400 transition-colors duration-300 py-2 border-b border-gray-800"
            >
              Servicios
            </a>
            <a
              href="#proyectos"
              @click="closeMobileMenu"
              class="text-white hover:text-blue-400 transition-colors duration-300 py-2 border-b border-gray-800"
            >
              Proyectos
            </a>
            <a
              href="#proceso"
              @click="closeMobileMenu"
              class="text-white hover:text-blue-400 transition-colors duration-300 py-2 border-b border-gray-800"
            >
              Proceso
            </a>
            <a
              href="#contacto"
              @click="closeMobileMenu"
              class="text-white hover:text-blue-400 transition-colors duration-300 py-2"
            >
              Contacto
            </a>
            
            <!-- Botón Especial Contáctanos (Móvil) -->
            <a
              href="#contacto"
              @click="closeMobileMenu"
              class="bg-[#0A84FF] text-white px-4 py-3 rounded-lg hover:brightness-110 transition-all duration-300 text-center mt-4 font-medium"
            >
              Contáctanos
            </a>
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
