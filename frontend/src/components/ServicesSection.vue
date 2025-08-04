<template>
  <section id="servicios" class="bg-gradient-to-b from-stealth-black via-arsenal-grey to-stealth-black min-h-screen py-20 relative overflow-hidden">
    <div class="absolute top-20 right-20 w-32 h-32 rounded-full opacity-5 bg-gradient-to-r from-tech-green to-alert-orange"></div>
    <div class="absolute bottom-32 left-16 w-24 h-24 rounded-full opacity-5 bg-gradient-to-r from-radar-green to-tactical-blue"></div>
    
    <div class="absolute inset-0 opacity-5">
      <div class="w-full h-full bg-grid-pattern"></div>
    </div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center mb-16">
        <div class="text-sm mb-4 font-mono text-tech-green">
          [ TACTICAL SOLUTIONS DEPLOYMENT ]
        </div>
        
        <h2 class="text-4xl md:text-5xl lg:text-6xl mb-6 font-mono">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-tech-green to-alert-orange">ARSENAL</span> 
          <span class="text-white">Digital</span>
        </h2>
        
        <p class="text-lg md:text-xl max-w-3xl mx-auto text-gray-300 font-mono">
          > Implementamos soluciones tecnológicas de élite con precisión militar.<br/>
          > Cada misión ejecutada con excelencia operacional._
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="(service, index) in tacticalServices" 
             :key="index" 
             class="bg-gradient-to-br from-arsenal-grey/20 to-tactical-blue/20 border border-tech-green/30 rounded-xl p-6 group cursor-pointer transition-all duration-500 hover:scale-105 hover:border-tech-green/60 backdrop-blur-sm">
          
          <div class="text-center mb-6">
            <div class="inline-flex items-center justify-center w-16 h-16 rounded-full mb-4 group-hover:scale-110 transition-transform duration-300 border-2 border-tech-green/50"
                 :style="{ background: service.gradient }">
              <i :class="service.icon" class="text-2xl text-white"></i>
            </div>
          </div>
          
          <div class="text-center">
            <h3 class="text-xl font-bold mb-4 font-mono group-hover:text-tech-green transition-all duration-300 text-white">
              {{ service.title }}
            </h3>
            
            <p class="text-gray-400 text-sm leading-relaxed mb-6 font-mono">
              > {{ service.description }}
            </p>
            
            <ul class="text-left space-y-2 mb-6">
              <li v-for="feature in service.features" 
                  :key="feature"
                  class="flex items-center text-sm text-gray-400 font-mono">
                <span class="text-tech-green mr-2">></span>
                {{ feature }}
              </li>
            </ul>
            
            <button class="w-full py-3 px-6 rounded-lg font-mono font-medium transition-all duration-300 
                           bg-gradient-to-r from-tech-green/20 to-alert-orange/20 
                           border border-tech-green/50 text-tech-green
                           hover:from-tech-green/30 hover:to-alert-orange/30 
                           hover:border-tech-green hover:shadow-lg hover:shadow-tech-green/25">
              [ DEPLOY ]
            </button>
          </div>
        </div>
      </div>

      <div class="text-center mt-16">
        <div class="bg-gradient-to-br from-arsenal-grey/30 to-tactical-blue/30 border border-tech-green/40 rounded-xl p-8 max-w-4xl mx-auto backdrop-blur-sm">
          <h3 class="text-2xl md:text-3xl mb-4 font-mono text-white">
            Ready to <span class="text-transparent bg-clip-text bg-gradient-to-r from-tech-green to-alert-orange font-bold">DEPLOY</span> your mission?
          </h3>
          
          <p class="text-gray-400 mb-6 max-w-2xl mx-auto font-mono">
            > Our tactical development unit stands ready to execute your vision.<br/>
            > Contact command center to initiate deployment protocols._
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button class="px-8 py-3 rounded-lg font-mono font-medium transition-all duration-300 
                           bg-gradient-to-r from-tech-green to-radar-green text-stealth-black
                           hover:scale-105 hover:shadow-lg hover:shadow-tech-green/50">
              [ INITIATE CONTACT ]
            </button>
            <button class="px-8 py-3 rounded-lg font-mono font-medium transition-all duration-300 
                           bg-transparent border-2 border-tech-green/50 text-tech-green
                           hover:border-tech-green hover:bg-tech-green/10 hover:scale-105">
              [ VIEW INTEL ]
            </button>
          </div>
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
.bg-grid-pattern {
  background-image: 
    linear-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 65, 0.1) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: grid-pulse 4s ease-in-out infinite;
}

@keyframes grid-pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.1; }
}

.group:hover {
  box-shadow: 
    0 0 20px rgba(0, 255, 65, 0.3),
    inset 0 0 20px rgba(0, 255, 65, 0.1);
}

.font-mono {
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  letter-spacing: 0.025em;
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .lg\:grid-cols-3 {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
