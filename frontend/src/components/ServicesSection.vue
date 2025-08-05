<template>
  <section id="servicios" class="py-20 lg:py-32 bg-slate-900 relative overflow-hidden">
    <!-- Circuit Grid Background -->
    <div class="absolute inset-0 circuit-grid-pattern opacity-20"></div>
    
    <!-- Military decorative elements -->
    <div class="absolute top-10 right-10 w-20 h-20 opacity-10 bg-gradient-to-br from-green-400 to-orange-400"></div>
    <div class="absolute bottom-20 left-20 w-16 h-16 opacity-10 bg-gradient-to-br from-orange-400 to-red-400"></div>
    <div class="absolute top-1/2 left-10 w-12 h-12 opacity-5 bg-gradient-to-br from-blue-400 to-green-400"></div>
    
    <div class="max-w-7xl mx-auto px-6 lg:px-8 relative z-10">
      <div class="text-center mb-16">
        <div class="text-green-400 font-semibold font-mono text-sm mb-4 tracking-wider uppercase">
          [ TACTICAL OPERATIONS DIVISION ]
        </div>
        
        <h2 class="text-4xl md:text-5xl lg:text-6xl mb-8 font-mono font-bold text-white">
          Operaciones <span class="bg-gradient-to-r from-green-400 via-orange-400 to-red-400 bg-clip-text text-transparent">Especializadas</span>
        </h2>
        
        <p class="text-lg md:text-xl max-w-3xl mx-auto text-gray-300 font-mono">
          Despliegue de sistemas de seguridad avanzados y soluciones de ciberseguridad militar. 
          Cada misión ejecutada con precisión táctica.
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div v-for="(service, index) in tacticalServices" 
             :key="index" 
             class="bg-black/80 p-8 relative overflow-hidden border border-green-500/30 shadow-xl group cursor-pointer transition-all duration-500 hover:scale-105 hover:border-green-400 hover:shadow-2xl backdrop-blur-lg">
          
          <div class="text-center mb-6">
            <div class="w-16 h-16 border-2 border-green-400/50 flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform duration-300 bg-gradient-to-br from-green-600/20 to-orange-600/20">
              <i :class="service.icon" class="text-2xl text-green-400"></i>
            </div>
          </div>
          
          <div class="text-center">
            <h3 class="text-xl font-bold mb-4 font-mono group-hover:text-green-400 transition-all duration-300 text-white">
              {{ service.title }}
            </h3>
            
            <p class="text-gray-300 leading-relaxed mb-6 font-mono text-sm">
              {{ service.description }}
            </p>
            
            <ul class="text-left space-y-2 mb-6">
              <li v-for="feature in service.features" 
                  :key="feature"
                  class="flex items-center text-sm text-gray-400 font-mono">
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
            <button class="px-8 py-3 font-mono font-medium transition-all duration-300 
                           bg-gradient-to-r from-green-600 to-orange-600 text-black border border-green-400
                           hover:scale-105 hover:shadow-lg hover:shadow-green-500/25">
              [ DEPLOY ]
            </button>
            <button class="px-8 py-3 font-mono font-medium transition-all duration-300 
                           bg-transparent border-2 border-orange-400 text-orange-400
                           hover:bg-orange-400/10 hover:scale-105">
              [ INTEL ]
            </button>
          </div>
          
          <!-- Military decorative elements -->
          <div class="absolute top-4 right-4 w-3 h-3 bg-green-400 opacity-30"></div>
          <div class="absolute bottom-4 left-4 w-2 h-2 bg-orange-500 opacity-40"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const tacticalServices = ref([
  {
    icon: 'fas fa-shield-alt',
    title: 'CYBERSECURITY OPERATIONS',
    description: 'Sistemas de defensa avanzados contra amenazas digitales.',
    gradient: 'linear-gradient(135deg, #00FF41 0%, #FF6B35 100%)',
    features: [
      'Penetration Testing',
      'Vulnerability Assessment', 
      'Security Auditing',
      'Incident Response'
    ]
  },
  {
    icon: 'fas fa-satellite-dish',
    title: 'TACTICAL COMMUNICATIONS',
    description: 'Sistemas de comunicación segura y redes privadas.',
    gradient: 'linear-gradient(135deg, #FF6B35 0%, #0A84FF 100%)',
    features: [
      'Encrypted Networks',
      'Secure VPN Tunnels',
      'Radio Communications',
      'Satellite Uplinks'
    ]
  },
  {
    icon: 'fas fa-server',
    title: 'FORTIFIED INFRASTRUCTURE',
    description: 'Infraestructura blindada para operaciones críticas.',
    gradient: 'linear-gradient(135deg, #0A84FF 0%, #00FF41 100%)',
    features: [
      'Hardened Servers',
      'Redundant Systems',
      'DDoS Protection',
      'Zero-Trust Architecture'
    ]
  },
  {
    icon: 'fas fa-search',
    title: 'DIGITAL FORENSICS',
    description: 'Investigación forense digital y análisis de amenazas.',
    gradient: 'linear-gradient(135deg, #00FF41 0%, #FF453A 100%)',
    features: [
      'Evidence Collection',
      'Malware Analysis',
      'Network Forensics',
      'Chain of Custody'
    ]
  },
  {
    icon: 'fas fa-eye',
    title: 'SURVEILLANCE SYSTEMS',
    description: 'Sistemas de monitoreo y vigilancia avanzada.',
    gradient: 'linear-gradient(135deg, #FF6B35 0%, #00FF41 100%)',
    features: [
      'Real-time Monitoring',
      'Threat Detection',
      'Behavioral Analysis',
      'Automated Alerts'
    ]
  },
  {
    icon: 'fas fa-lock',
    title: 'ENCRYPTION PROTOCOLS',
    description: 'Protocolos de cifrado militar y gestión de claves.',
    gradient: 'linear-gradient(135deg, #FF453A 0%, #0A84FF 100%)',
    features: [
      'AES-256 Encryption',
      'Key Management',
      'PKI Infrastructure',
      'Quantum Resistance'
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

.font-mono {
  font-family: 'JetBrains Mono', monospace;
}

.font-orbitron {
  font-family: 'Orbitron', monospace;
}

/* Enhanced tactical hover effects */
.group:hover {
  transform: translateY(-8px);
}

/* Smooth military transitions */
.transition-all {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Circuit Grid Pattern - Military Network */
.circuit-grid-pattern {
  background-image: 
    /* Main circuit lines - green */
    linear-gradient(0deg, rgba(0, 255, 65, 0.3) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 65, 0.3) 1px, transparent 1px),
    /* Secondary circuit lines - orange */
    linear-gradient(45deg, rgba(255, 107, 53, 0.2) 1px, transparent 1px),
    linear-gradient(-45deg, rgba(255, 107, 53, 0.2) 1px, transparent 1px),
    /* Circuit nodes - blue */
    radial-gradient(circle at 25% 25%, rgba(10, 132, 255, 0.4) 2px, transparent 2px),
    radial-gradient(circle at 75% 75%, rgba(10, 132, 255, 0.3) 1.5px, transparent 1.5px),
    /* Power lines - red */
    linear-gradient(30deg, rgba(255, 69, 58, 0.15) 1px, transparent 1px),
    linear-gradient(-30deg, rgba(255, 69, 58, 0.15) 1px, transparent 1px),
    /* Data flow indicators */
    radial-gradient(circle at 50% 50%, rgba(0, 255, 65, 0.2) 1px, transparent 1px);
  background-size: 
    50px 50px,
    50px 50px,
    25px 25px,
    25px 25px,
    75px 75px,
    100px 100px,
    80px 80px,
    80px 80px,
    40px 40px;
  background-position: 
    0 0,
    0 0,
    12px 12px,
    38px 38px,
    0 0,
    25px 25px,
    20px 20px,
    60px 60px,
    15px 15px;
  animation: circuit-flow 20s linear infinite;
}

@keyframes circuit-flow {
  0% { 
    transform: translateX(0) translateY(0); 
    opacity: 0.7;
  }
  25% { 
    transform: translateX(-5px) translateY(-5px); 
    opacity: 0.6;
  }
  50% { 
    transform: translateX(5px) translateY(-5px); 
    opacity: 0.8;
  }
  75% { 
    transform: translateX(-5px) translateY(5px); 
    opacity: 0.65;
  }
  100% { 
    transform: translateX(0) translateY(0); 
    opacity: 0.7;
  }
}
</style>
