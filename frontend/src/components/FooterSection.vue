<template>
  <footer class="py-8 bg-slate-900 relative overflow-hidden">
    <!-- Decorative elements con paleta moderna -->
    <div class="absolute top-5 right-5 w-12 h-12 rounded-full opacity-10 bg-gradient-to-br from-indigo-600 to-purple-600"></div>
    <div class="absolute bottom-5 left-5 w-8 h-8 rounded-full opacity-10 bg-gradient-to-br from-purple-600 to-amber-500"></div>
    <div class="absolute top-1/2 left-5 w-6 h-6 rounded-full opacity-5 bg-gradient-to-br from-amber-500 to-indigo-600"></div>
    <!-- Contenido Principal -->
    <div class="relative z-10 max-w-7xl mx-auto px-6 py-4">
      
      <!-- Grid de Footer con Logo -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
        
        <!-- Logo y Marca VARNOX -->
        <div class="group">
          <div class="flex items-center gap-3 mb-2">
            <div class="w-8 h-8 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl flex items-center justify-center p-1.5 shadow-lg">
              <!-- Logo PNG -->
              <img src="@/assets/logo.png" alt="VARNOX Logo" class="w-full h-full object-contain filter brightness-125" />
            </div>
            <h3 class="text-sm font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent font-orbitron">
              VARNOX
            </h3>
          </div>
          <p class="text-gray-400 text-xs leading-relaxed font-source-sans">
            Transformamos ideas en soluciones tecnológicas innovadoras.
          </p>
        </div>
        
        <!-- Servicios -->
        <div class="group">
          <h4 class="text-xs font-bold mb-2 text-white relative font-orbitron">
            <span class="bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">Servicios</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-400 to-purple-400 group-hover:w-full transition-all duration-500"></div>
          </h4>
          <ul class="space-y-1 font-source-sans">
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              Desarrollo Web
            </a></li>
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              Aplicaciones Móviles
            </a></li>
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              Cloud Solutions
            </a></li>
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              DevOps & CI/CD
            </a></li>
          </ul>
        </div>
        
        <!-- Tecnologías -->
        <div class="group">
          <h4 class="text-xs font-orbitron font-bold mb-2 text-white relative">
            <span class="bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">Tecnologías</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-400 to-purple-400 group-hover:w-full transition-all duration-500"></div>
          </h4>
          <ul class="space-y-1 font-poppins">
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              Vue.js & React
            </a></li>
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              Node.js & Python
            </a></li>
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              Docker & AWS
            </a></li>
            <li><a href="#" class="text-gray-400 hover:text-indigo-300 transition-colors duration-300 flex items-center gap-2 text-xs">
              <div class="w-1 h-1 bg-indigo-400 rounded-full"></div>
              MongoDB & PostgreSQL
            </a></li>
          </ul>
        </div>
        
        <!-- Contacto -->
        <div class="group">
          <h4 class="text-xs font-orbitron font-bold mb-2 text-white relative">
            <span class="bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">Contacto</span>
            <div class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-400 to-purple-400 group-hover:w-full transition-all duration-500"></div>
          </h4>
          
          <!-- Información de Contacto -->
          <div class="space-y-2 font-poppins">
            <div class="flex items-center gap-2">
              <div class="w-4 h-4 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg flex items-center justify-center">
                <svg class="w-2 h-2 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
              </div>
              <span class="text-gray-400 text-xs">info@varnox.tech</span>
            </div>
            
            <div class="flex items-center gap-2">
              <div class="w-4 h-4 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-lg flex items-center justify-center">
                <svg class="w-2 h-2 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
              </div>
              <span class="text-gray-400 text-xs">+52 (55) 1234-5678</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Copyright Centrado -->
      <div class="border-t border-slate-700 pt-3">
        <div class="text-center">
          <p class="text-gray-400 text-xs font-poppins">
            © 2024 <span class="text-indigo-400 font-semibold">VARNOX</span>. Todos los derechos reservados.
          </p>
        </div>
      </div>
    </div>
    
    <!-- Línea de Acento Final -->
    <div class="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-indigo-600 via-purple-600 to-amber-500"></div>
  </footer>
</template>

<script setup lang="ts">
// Footer simplificado - sin funciones adicionales requeridas
</script>

<style scoped>
/* Tipografías Modernas */
/* Modern animations */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.animate-on-scroll.animate {
  opacity: 1;
  transform: translateY(0);
}

/* Font classes */
.font-orbitron {
  font-family: 'Orbitron', monospace;
}

.font-poppins {
  font-family: 'Poppins', sans-serif;
}

.font-source-sans {
  font-family: 'Source Sans Pro', sans-serif;
}

/* Animaciones Elegantes */
.transition-all {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Efectos de Hover Suaves */
a:hover {
  text-decoration: none;
}

/* Animaciones de Entrada */
.group:hover .group-hover\:w-full {
  width: 100%;
}

/* Responsive Design */
@media (max-width: 768px) {
  .font-orbitron {
    font-size: 0.9rem;
  }
  
  .grid {
    gap: 1.5rem;
  }
  
  h4 {
    font-size: 0.8rem;
  }
  
  p, span, a {
    font-size: 0.75rem;
  }
}
</style>
