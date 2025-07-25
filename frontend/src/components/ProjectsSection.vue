<template>
  <section id="proyectos" class="bg-space-grey section">
    <div class="max-w-7xl mx-auto">
      <!-- Section Header -->
      <div class="text-center mb-16 lg:mb-20">
        <h2 class="section-title text-pure-white animate-on-scroll">
          Algunos mundos que ya ayudamos a construir
        </h2>
      </div>
      
      <!-- Projects Carousel/Grid -->
      <div class="relative">
        <!-- Projects Container -->
        <div class="flex space-x-8 overflow-x-auto pb-6 scrollbar-hide snap-x snap-mandatory">
          <div 
            v-for="(project, index) in projects" 
            :key="project.id"
            class="flex-none w-80 lg:w-96 snap-start animate-on-scroll"
            :style="{ animationDelay: `${index * 0.2}s` }"
          >
            <!-- Project Card -->
            <div class="bg-graphite rounded-3xl overflow-hidden group hover:scale-105 transition-all duration-500 hover:shadow-2xl hover:shadow-electric-blue/10">
              <!-- Project Image/Visual -->
              <div class="h-48 bg-gradient-to-br from-electric-blue/20 to-space-grey relative overflow-hidden">
                <!-- Abstract pattern background -->
                <div class="absolute inset-0 opacity-30">
                  <svg viewBox="0 0 200 200" class="w-full h-full">
                    <defs>
                      <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
                        <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#0A84FF" stroke-width="0.5" opacity="0.3"/>
                      </pattern>
                    </defs>
                    <rect width="200" height="200" fill="url(#grid)" />
                  </svg>
                </div>
                
                <!-- Project Type Badge -->
                <div class="absolute top-4 left-4">
                  <span class="bg-electric-blue/20 text-electric-blue px-3 py-1 rounded-full text-sm font-medium">
                    {{ project.type }}
                  </span>
                </div>
                
                <!-- Project Icon -->
                <div class="absolute bottom-4 right-4 w-12 h-12 bg-pure-black/30 backdrop-blur-sm rounded-full flex items-center justify-center">
                  <component :is="project.icon" class="w-6 h-6 text-electric-blue" />
                </div>
              </div>
              
              <!-- Project Content -->
              <div class="p-8">
                <h3 class="font-urbanist font-bold text-xl text-pure-white mb-3 group-hover:text-electric-blue transition-colors">
                  {{ project.name }}
                </h3>
                <p class="text-silver font-inter mb-4 leading-relaxed">
                  {{ project.description }}
                </p>
                
                <!-- Client Info -->
                <div class="flex items-center justify-between">
                  <div>
                    <p class="font-space-grotesk font-medium text-pure-white text-sm">
                      {{ project.client }}
                    </p>
                    <p class="text-silver text-xs">
                      {{ project.result }}
                    </p>
                  </div>
                  
                  <!-- Arrow Icon -->
                  <div class="w-8 h-8 bg-electric-blue/10 rounded-full flex items-center justify-center group-hover:bg-electric-blue/20 transition-colors">
                    <svg class="w-4 h-4 text-electric-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 17L17 7M17 7H7M17 7v10" />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Scroll Navigation Hint -->
        <div class="flex justify-center mt-8">
          <div class="flex space-x-2">
            <div 
              v-for="(_, index) in projects.slice(0, 3)" 
              :key="index"
              class="w-2 h-2 rounded-full bg-silver/30"
              :class="{ 'bg-electric-blue': index === 0 }"
            ></div>
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

// Sample projects data
const projects = [
  {
    id: 1,
    name: 'TechCorp Solutions',
    type: 'Sitio Web',
    description: 'Plataforma corporativa moderna con sistema de gestión integrado y panel administrativo.',
    client: 'Empresa Tecnológica',
    result: '+150% conversiones',
    icon: WebIcon
  },
  {
    id: 2,
    name: 'SmartBot Assistant',
    type: 'Automatización',
    description: 'Bot inteligente para atención al cliente con IA que redujo tiempos de respuesta significativamente.',
    client: 'E-commerce',
    result: '70% menos consultas manuales',
    icon: BotIcon
  },
  {
    id: 3,
    name: 'MobileFirst App',
    type: 'App Móvil',
    description: 'Aplicación móvil nativa con sincronización en tiempo real y experiencia de usuario premium.',
    client: 'Startup Financiera',
    result: '4.9★ en tiendas',
    icon: MobileIcon
  },
  {
    id: 4,
    name: 'CloudScale Infrastructure',
    type: 'Cloud',
    description: 'Migración completa a la nube con arquitectura escalable y monitoreo automatizado.',
    client: 'Empresa Manufacturera',
    result: '60% reducción costos',
    icon: CloudIcon
  },
  {
    id: 5,
    name: 'AI Analytics Platform',
    type: 'Inteligencia Artificial',
    description: 'Sistema de análisis predictivo con machine learning para optimización de inventarios.',
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
