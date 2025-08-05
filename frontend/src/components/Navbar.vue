<template>
  <nav role="navigation" class="fixed top-0 left-0 right-0 z-50 bg-slate-900 border-b border-slate-700 shadow-2xl">
    <!-- Status Panel Elegante -->
    <div class="absolute top-3 left-6 text-xs font-jetbrains text-green-400">
      <div class="flex items-center gap-2">
        <div class="w-2 h-2 bg-green-400 rounded-full shadow-green-400 shadow-lg"></div>
        <span class="font-medium tracking-wider">VARNOX.ONLINE</span>
      </div>
    </div>
    
    <!-- Gradiente Sutil de Fondo -->
    <div class="absolute inset-0 bg-gradient-to-r from-slate-900/90 via-slate-800/80 to-slate-900/90"></div>
    
    <!-- Línea de Acento -->
    <div class="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-indigo-600 via-purple-600 to-amber-500"></div>
    
    <div class="px-6 md:px-12 py-5 relative z-10">
      <div class="flex items-center justify-between">
        <!-- Logo VARNOX Moderno -->
        <div class="flex items-center gap-x-4">
          <div class="relative">
            <img src="/src/assets/logo.png" alt="VARNOX Logo" class="w-12 h-12 rounded-lg shadow-lg" />
          </div>
          <div class="font-orbitron">
            <div class="text-xs text-green-400 tracking-widest font-mono mb-1 animate-pulse">
              .active
            </div>
            <div class="text-xl font-bold tracking-widest text-white">
              VARNOX
            </div>
          </div>
        </div>

        <!-- Menu Desktop Elegante -->
        <div class="hidden md:flex items-center space-x-10">
          <a
            href="#hero"
            class="nav-link text-gray-300 hover:text-indigo-400 transition-all duration-300 font-poppins text-sm font-medium tracking-wide relative group"
          >
            <span class="relative z-10">Inicio</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-400 to-purple-400 group-hover:w-full transition-all duration-300"></div>
          </a>
          <a
            href="#servicios"
            class="nav-link text-gray-300 hover:text-purple-400 transition-all duration-300 font-poppins text-sm font-medium tracking-wide relative group"
          >
            <span class="relative z-10">Servicios</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-purple-400 to-indigo-400 group-hover:w-full transition-all duration-300"></div>
          </a>
          <a
            href="#nosotros"
            class="nav-link text-gray-300 hover:text-amber-400 transition-all duration-300 font-poppins text-sm font-medium tracking-wide relative group"
          >
            <span class="relative z-10">Nosotros</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-amber-400 to-purple-400 group-hover:w-full transition-all duration-300"></div>
          </a>
          <a
            href="#proyectos"
            class="nav-link text-gray-300 hover:text-indigo-400 transition-all duration-300 font-poppins text-sm font-medium tracking-wide relative group"
          >
            <span class="relative z-10">Proyectos</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-400 to-amber-400 group-hover:w-full transition-all duration-300"></div>
          </a>
          <a
            href="#proceso"
            class="nav-link text-gray-300 hover:text-purple-400 transition-all duration-300 font-poppins text-sm font-medium tracking-wide relative group"
          >
            <span class="relative z-10">Proceso</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-purple-400 to-amber-400 group-hover:w-full transition-all duration-300"></div>
          </a>
          <a
            href="#contacto"
            class="nav-link text-gray-300 hover:text-amber-400 transition-all duration-300 font-poppins text-sm font-medium tracking-wide relative group"
          >
            <span class="relative z-10">Contacto</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-amber-400 to-indigo-400 group-hover:w-full transition-all duration-300"></div>
          </a>
          
          <!-- Botón CTA Elegante -->
          <button
            @click="scrollToContact"
            class="cta-btn relative overflow-hidden bg-gradient-to-r from-indigo-600 via-purple-600 to-amber-500 text-white px-7 py-3 rounded-xl font-poppins font-semibold text-sm tracking-wide shadow-xl hover:shadow-2xl hover:shadow-purple-500/25 transition-all duration-300 group"
          >
            <span class="relative z-10">Comenzar Proyecto</span>
            <div class="absolute inset-0 bg-gradient-to-r from-purple-600 via-indigo-600 to-amber-600 group-hover:opacity-100 transition-opacity duration-300"></div>
          </button>
        </div>

        <!-- Botón Hamburguesa Elegante -->
        <button
          @click="toggleMobileMenu"
          class="md:hidden text-gray-300 focus:outline-none hover:text-indigo-400 transition-colors duration-300"
          aria-label="Toggle menu"
        >
          <div class="flex flex-col gap-1.5">
            <div class="w-7 h-0.5 bg-current transition-all duration-300 rounded-full" :class="{ 'rotate-45 translate-y-2': isOpen }"></div>
            <div class="w-7 h-0.5 bg-current transition-all duration-300 rounded-full" :class="{ 'display-none': isOpen }"></div>
            <div class="w-7 h-0.5 bg-current transition-all duration-300 rounded-full" :class="{ '-rotate-45 -translate-y-2': isOpen }"></div>
          </div>
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isOpen = ref(false)

const toggleMobileMenu = () => {
  isOpen.value = !isOpen.value
}

const scrollToContact = () => {
  const contactSection = document.getElementById('contacto')
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;800;900&family=Poppins:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500;600&display=swap');

/* Variables CSS personalizadas */
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --accent-gradient: linear-gradient(45deg, #f093fb 0%, #f5576c 50%, #4facfe 100%);
}

/* Fuentes */
.font-orbitron {
  font-family: 'Orbitron', monospace;
}

.font-poppins {
  font-family: 'Poppins', sans-serif;
}

.font-jetbrains {
  font-family: 'JetBrains Mono', monospace;
}

/* Efectos de Hover */
.nav-link {
  position: relative;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.nav-link:hover {
  transform: translateY(-2px);
}

/* Botón CTA con efecto de hover */
.cta-btn:hover {
  transform: translateY(-3px) scale(1.02);
}

/* Animaciones suaves */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

nav {
  animation: fadeInDown 0.8s ease-out;
}

/* Efecto de desenfoque de respaldo */
.backdrop-blur-xl {
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
}
</style>
