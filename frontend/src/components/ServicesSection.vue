<template>
  <section id="servicios" class="py-20 lg:py-32 bg-gradient-to-br from-gray-50 via-white to-indigo-50/30 relative overflow-hidden">
    <!-- Hexagonal Grid Background -->
    <div class="absolute inset-0 hexagonal-grid-pattern opacity-30"></div>
    
    <!-- Decorative elements con paleta moderna -->
    <div class="absolute top-10 right-10 w-20 h-20 rounded-full opacity-10 bg-gradient-to-br from-indigo-600 to-purple-600"></div>
    <div class="absolute bottom-20 left-20 w-16 h-16 rounded-full opacity-10 bg-gradient-to-br from-purple-600 to-amber-500"></div>
    <div class="absolute top-1/2 left-10 w-12 h-12 rounded-full opacity-5 bg-gradient-to-br from-amber-500 to-indigo-600"></div>
    
    <div class="max-w-7xl mx-auto px-6 lg:px-8 relative z-10">
      <div class="text-center mb-16">
        <div class="text-indigo-600 font-semibold font-poppins text-sm mb-4 tracking-wider uppercase">
          [ NUESTROS SERVICIOS ]
        </div>
        
        <h2 class="text-4xl md:text-5xl lg:text-6xl mb-8 font-orbitron font-bold text-gray-900">
          Nuestro <span class="bg-gradient-to-r from-indigo-600 via-purple-600 to-amber-500 bg-clip-text text-transparent">Arsenal</span> Digital
        </h2>
        
        <p class="text-lg md:text-xl max-w-3xl mx-auto text-gray-700 font-source-sans">
          Implementamos soluciones tecnológicas de élite con precisión profesional. 
          Cada proyecto ejecutado con excelencia operacional.
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="(service, index) in tacticalServices" 
             :key="index" 
             class="bg-white p-8 relative overflow-hidden rounded-2xl border border-gray-200 shadow-xl group cursor-pointer transition-all duration-500 hover:scale-105 hover:border-indigo-200 hover:shadow-2xl">
          
          <div class="text-center mb-6">
            <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300 bg-gradient-to-br from-indigo-600 to-purple-600">
              <i :class="service.icon" class="text-2xl text-white"></i>
            </div>
          </div>
          
          <div class="text-center">
            <h3 class="text-xl font-bold mb-4 font-orbitron group-hover:text-indigo-600 transition-all duration-300 text-gray-900">
              {{ service.title }}
            </h3>
            
            <p class="text-gray-600 leading-relaxed mb-6 font-source-sans">
              {{ service.description }}
            </p>
            
            <ul class="text-left space-y-2 mb-6">
              <li v-for="feature in service.features" 
                  :key="feature"
                  class="flex items-center text-sm text-gray-700 font-source-sans">
                <svg class="w-4 h-4 mr-2 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                {{ feature }}
              </li>
            </ul>
            
            <button class="w-full py-3 px-6 rounded-xl font-poppins font-medium transition-all duration-300 
                           bg-gradient-to-r from-indigo-600 to-purple-600 text-white
                           hover:from-indigo-700 hover:to-purple-700 hover:shadow-lg hover:shadow-indigo-500/25">
              Conocer más
            </button>
          </div>
          
          <!-- Decorative elements -->
          <div class="absolute top-4 right-4 w-3 h-3 rounded-full bg-indigo-600 opacity-30"></div>
          <div class="absolute bottom-4 left-4 w-2 h-2 rounded-full bg-amber-500 opacity-40"></div>
        </div>
      </div>

      <div class="text-center mt-16">
        <div class="bg-white p-8 relative overflow-hidden rounded-2xl border border-gray-200 shadow-xl max-w-4xl mx-auto">
          <h3 class="text-2xl md:text-3xl mb-4 font-orbitron font-bold text-gray-900">
            ¿Listo para <span class="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">comenzar</span> tu proyecto?
          </h3>
          
          <p class="text-gray-600 mb-6 max-w-2xl mx-auto font-source-sans">
            Nuestro equipo está preparado para transformar tus ideas en soluciones tecnológicas exitosas.
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button class="px-8 py-3 rounded-xl font-poppins font-medium transition-all duration-300 
                           bg-gradient-to-r from-indigo-600 to-purple-600 text-white
                           hover:scale-105 hover:shadow-lg hover:shadow-indigo-500/25">
              Iniciar Proyecto
            </button>
            <button class="px-8 py-3 rounded-xl font-poppins font-medium transition-all duration-300 
                           bg-transparent border-2 border-indigo-600 text-indigo-600
                           hover:bg-indigo-50 hover:scale-105">
              Ver Portafolio
            </button>
          </div>
          
          <!-- Decorative elements -->
          <div class="absolute top-4 right-4 w-3 h-3 rounded-full bg-indigo-600 opacity-30"></div>
          <div class="absolute bottom-4 left-4 w-2 h-2 rounded-full bg-amber-500 opacity-40"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const tacticalServices = ref([
  {
    icon: 'fas fa-code',
    title: 'Web Warfare',
    description: 'Aplicaciones web de élite con arquitectura militar.',
    gradient: 'linear-gradient(135deg, #00FF41 0%, #0A4D68 100%)',
    features: [
      'Frontend tactical',
      'Backend fortified',
      'APIs secured',
      'SEO stealth mode'
    ]
  },
  {
    icon: 'fas fa-mobile-alt',
    title: 'Mobile Arsenal',
    description: 'Desarrollo móvil para misiones iOS y Android.',
    gradient: 'linear-gradient(135deg, #FF6B35 0%, #39FF14 100%)',
    features: [
      'iOS & Android ops',
      'React Native deploy',
      'Flutter tactical',
      'UI/UX combat ready'
    ]
  },
  {
    icon: 'fas fa-cloud',
    title: 'Cloud Command',
    description: 'Infraestructura en la nube con seguridad militar.',
    gradient: 'linear-gradient(135deg, #0A4D68 0%, #00FF41 100%)',
    features: [
      'AWS & Azure ops',
      'Docker containers',
      'Microservices grid',
      'DevOps automation'
    ]
  },
  {
    icon: 'fas fa-database',
    title: 'Intel Analytics',
    description: 'Análisis de datos e inteligencia operacional.',
    gradient: 'linear-gradient(135deg, #39FF14 0%, #556B2F 100%)',
    features: [
      'Business Intelligence',
      'Machine Learning ops',
      'Data visualization',
      'Predictive analytics'
    ]
  },
  {
    icon: 'fas fa-shield-alt',
    title: 'Cyber Defense',
    description: 'Protección perimetral de sistemas críticos.',
    gradient: 'linear-gradient(135deg, #FF6B35 0%, #2D3748 100%)',
    features: [
      'Security audits',
      'Penetration testing',
      'Compliance ops',
      'Incident response'
    ]
  },
  {
    icon: 'fas fa-cogs',
    title: 'DevOps Command',
    description: 'Automatización de operaciones de despliegue.',
    gradient: 'linear-gradient(135deg, #2D3748 0%, #FF6B35 100%)',
    features: [
      'Pipeline automation',
      'Infrastructure as Code',
      'Monitoring systems',
      'Container orchestration'
    ]
  }
])
</script>

<style scoped>
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

/* Enhanced hover effects */
.group:hover {
  transform: translateY(-8px);
}

/* Smooth transitions */
.transition-all {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Hexagonal Grid Pattern - Malla 3D Tecnológica */
.hexagonal-grid-pattern {
  background-image: 
    /* Rejilla hexagonal principal con colores purple e indigo */
    radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.25) 2px, transparent 2px),
    radial-gradient(circle at 25% 25%, rgba(99, 102, 241, 0.22) 1.5px, transparent 1.5px),
    radial-gradient(circle at 75% 75%, rgba(255, 255, 255, 0.18) 1px, transparent 1px),
    /* Líneas de conexión hexagonal con purple/indigo */
    linear-gradient(30deg, rgba(139, 92, 246, 0.15) 1px, transparent 1px),
    linear-gradient(-30deg, rgba(99, 102, 241, 0.15) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.12) 1px, transparent 1px),
    /* Efecto 3D con sombras purple/indigo */
    linear-gradient(120deg, rgba(139, 92, 246, 0.08) 2px, transparent 2px),
    linear-gradient(-120deg, rgba(99, 102, 241, 0.08) 2px, transparent 2px),
    /* Puntos de intersección tecnológicos con white/purple */
    radial-gradient(circle at 100% 100%, rgba(255, 255, 255, 0.2) 1px, transparent 1px),
    radial-gradient(circle at 0% 0%, rgba(139, 92, 246, 0.12) 1px, transparent 1px);
  background-size: 
    45px 45px,
    30px 30px, 
    60px 60px,
    80px 46px,
    80px 46px,
    120px 120px,
    100px 58px,
    100px 58px,
    90px 90px,
    75px 75px;
  background-position: 
    0 0,
    15px 15px,
    30px 30px,
    0 0,
    40px 23px,
    0 0,
    20px 12px,
    60px 35px,
    45px 45px,
    -15px -15px;
  animation: hexagonal-tech-drift 30s linear infinite;
}

@keyframes hexagonal-tech-drift {
  0% { 
    transform: translateX(0) translateY(0) rotate(0deg) scale(1); 
    opacity: 0.6;
  }
  25% { 
    transform: translateX(-8px) translateY(-4px) rotate(0.3deg) scale(1.02); 
    opacity: 0.5;
  }
  50% { 
    transform: translateX(4px) translateY(-8px) rotate(0deg) scale(1); 
    opacity: 0.6;
  }
  75% { 
    transform: translateX(-4px) translateY(4px) rotate(-0.3deg) scale(0.98); 
    opacity: 0.55;
  }
  100% { 
    transform: translateX(0) translateY(0) rotate(0deg) scale(1); 
    opacity: 0.6;
  }
}
</style>
