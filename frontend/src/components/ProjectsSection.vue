<template>
  <section id="proyectos" class="varnox-bg-section varnox-section relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-32 left-20 w-40 h-40 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-hero);"></div>
    <div class="absolute bottom-20 right-16 w-32 h-32 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-section); animation-delay: 3s;"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Section Header with new typography -->
      <div class="text-center mb-16 lg:mb-20">
        <!-- Accent title -->
        <div class="varnox-accent-title text-sm mb-4">
          [ NUESTROS PROYECTOS ]
        </div>
        
        <h2 class="varnox-section-title text-4xl md:text-5xl lg:text-6xl mb-6 animate-on-scroll">
          <span class="varnox-display-title">DEPLOY</span> Showcase
        </h2>
        
        <div class="varnox-card max-w-3xl mx-auto p-6">
          <p class="varnox-body-text text-lg leading-relaxed">
            <span class="varnox-code-text">&gt;</span> Algunos mundos que ya ayudamos a construir
            <span class="text-varnox-primary animate-pulse">_</span>
          </p>
        </div>
      </div>
      
      <!-- Projects Carousel/Grid with enhanced design -->
      <div class="relative">
        <!-- Projects Container -->
        <div class="flex space-x-8 overflow-x-auto pb-6 scrollbar-hide snap-x snap-mandatory">
          <div 
            v-for="(project, index) in projects" 
            :key="project.id"
            class="flex-none w-80 lg:w-96 snap-start animate-on-scroll"
            :style="{ animationDelay: `${index * 0.2}s` }"
          >
            <!-- Project Card with VARNOX design -->
            <div class="group varnox-card transition-all duration-300 overflow-hidden hover:shadow-2xl">
              <!-- Project Image/Visual with new styling -->
              <div class="h-48 relative overflow-hidden"
                   style="background: var(--varnox-gradient-card);">
                
                <!-- Decorative pattern background -->
                <div class="absolute inset-0 opacity-20">
                  <svg viewBox="0 0 200 200" class="w-full h-full">
                    <defs>
                      <pattern id="varnox-grid" width="20" height="20" patternUnits="userSpaceOnUse">
                        <path d="M 20 0 L 0 0 0 20" fill="none" stroke="var(--varnox-primary)" stroke-width="0.5" opacity="0.5"/>
                      </pattern>
                      <linearGradient id="varnox-overlay" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:var(--varnox-primary);stop-opacity:0.1" />
                        <stop offset="100%" style="stop-color:var(--varnox-secondary);stop-opacity:0.2" />
                      </linearGradient>
                    </defs>
                    <rect width="200" height="200" fill="url(#varnox-grid)" />
                    <rect width="200" height="200" fill="url(#varnox-overlay)" />
                  </svg>
                </div>
                
                <!-- Project Type Badge -->
                <div class="absolute top-4 left-4">
                  <span class="varnox-code-text text-xs px-3 py-1 rounded-full" 
                        style="background: var(--varnox-primary); color: white;">
                    [ {{ project.type.toUpperCase().replace(/\s+/g, '_') }} ]
                  </span>
                </div>
                
                <!-- Project Icon -->
                <div class="absolute bottom-4 right-4 w-12 h-12 varnox-card-dark rounded-full flex items-center justify-center group-hover:scale-110 transition-transform">
                  <component :is="project.icon" class="w-6 h-6 text-varnox-primary" />
                </div>
                
                <!-- Animated lines -->
                <div class="absolute top-0 left-0 w-full h-0.5 bg-gradient-to-r from-transparent via-varnox-primary to-transparent group-hover:animate-pulse"></div>
              </div>
              
              <!-- Project Content with VARNOX styling -->
              <div class="p-8">
                <h3 class="varnox-section-title text-xl mb-3 group-hover:text-varnox-primary transition-colors">
                  {{ project.name }}
                </h3>
                <p class="varnox-body-text text-sm leading-relaxed mb-4">
                  {{ project.description }}
                </p>
                
                <!-- Client Info with new design -->
                <div class="flex items-center justify-between">
                  <div>
                    <p class="varnox-accent-title text-xs mb-1">
                      CLIENT: {{ project.client.toUpperCase() }}
                    </p>
                    <p class="varnox-code-text text-xs text-varnox-accent">
                      &gt; {{ project.result }}
                    </p>
                  </div>
                  
                  <!-- Enhanced Arrow Icon -->
                  <div class="w-10 h-10 rounded-full flex items-center justify-center transition-all duration-300 group-hover:scale-110"
                       style="background: var(--varnox-gradient-button);">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 17L17 7M17 7H7M17 7v10" />
                    </svg>
                  </div>
                </div>
                
                <!-- Status indicator -->
                <div class="mt-4 pt-4 border-t border-white/10">
                  <div class="flex items-center space-x-2">
                    <div class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></div>
                    <span class="varnox-code-text text-xs">STATUS: DEPLOYED</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Enhanced Scroll Navigation -->
        <div class="flex justify-center mt-8">
          <div class="varnox-card p-4">
            <div class="flex items-center space-x-3">
              <span class="varnox-code-text text-xs">SCROLL:</span>
              <div class="flex space-x-2">
                <div 
                  v-for="(_, index) in projects.slice(0, 3)" 
                  :key="index"
                  class="w-2 h-2 rounded-full transition-all duration-300"
                  :class="index === 0 ? 'bg-varnox-primary animate-pulse' : 'bg-white/20'"
                ></div>
              </div>
              <span class="varnox-code-text text-xs">→</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, defineComponent, h } from 'vue';

// Project icons
const WebIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-6 h-6'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9'
      })
    ]);
  }
});

const MobileIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-6 h-6'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M12 18h.01M8 21h8a1 1 0 001-1V4a1 1 0 00-1-1H8a1 1 0 00-1 1v16a1 1 0 001 1z'
      })
    ]);
  }
});

const BotIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-6 h-6'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z'
      })
    ]);
  }
});

const CloudIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-6 h-6'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10'
      })
    ]);
  }
});

// Sample projects data with VARNOX branding
const projects = [
  {
    id: 1,
    name: 'VARNOX Corporate',
    type: 'Web Platform',
    description: 'Sistema empresarial completo con arquitectura moderna, panel administrativo avanzado y APIs escalables.',
    client: 'TechCorp Solutions',
    result: '+150% conversiones',
    icon: WebIcon
  },
  {
    id: 2,
    name: 'VARNOX Assistant',
    type: 'AI Automation',
    description: 'Bot inteligente con IA conversacional, integración WhatsApp y sistema de aprendizaje automático.',
    client: 'E-commerce Global',
    result: '70% menos consultas manuales',
    icon: BotIcon
  },
  {
    id: 3,
    name: 'VARNOX Mobile',
    type: 'Native App',
    description: 'Aplicación móvil multiplataforma con sincronización en tiempo real y diseño premium.',
    client: 'FinTech Startup',
    result: '4.9★ rating promedio',
    icon: MobileIcon
  },
  {
    id: 4,
    name: 'VARNOX Cloud',
    type: 'Infrastructure',
    description: 'Migración completa a AWS con arquitectura serverless, auto-scaling y monitoreo 24/7.',
    client: 'Manufacturing Inc',
    result: '60% reducción costos',
    icon: CloudIcon
  },
  {
    id: 5,
    name: 'VARNOX Analytics',
    type: 'Machine Learning',
    description: 'Plataforma de análisis predictivo con ML para optimización de inventarios y forecasting.',
    client: 'Retail Nacional',
    result: '40% mejor predicción',
    icon: BotIcon
  }
];

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.animate-on-scroll').forEach((el) => {
    observer.observe(el);
  });
});
</script>

<style scoped>
/* Hide scrollbar but keep functionality */
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
</style>
