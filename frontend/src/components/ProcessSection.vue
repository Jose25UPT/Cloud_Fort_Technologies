<template>
  <section id="proceso" class="varnox-bg-section varnox-section relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-20 left-10 w-36 h-36 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-hero);"></div>
    <div class="absolute bottom-32 right-20 w-28 h-28 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-section); animation-delay: 4s;"></div>
    
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Section Header with new typography -->
      <div class="text-center mb-16 lg:mb-20">
        <!-- Accent title -->
        <div class="varnox-accent-title text-sm mb-4">
          [ NUESTRO PROCESO ]
        </div>
        
        <h2 class="varnox-section-title text-4xl md:text-5xl lg:text-6xl mb-6 animate-on-scroll">
          <span class="varnox-display-title">DEPLOY</span> Process
        </h2>
        
        <div class="varnox-card max-w-3xl mx-auto p-6">
          <p class="varnox-body-text text-lg leading-relaxed">
            <span class="varnox-code-text">&gt;</span> Así trabajamos contigo para hacer realidad tus ideas
            <span class="text-varnox-primary animate-pulse">_</span>
          </p>
        </div>
      </div>
      
      <!-- Process Steps with enhanced VARNOX design -->
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-6">
        <div 
          v-for="(step, index) in processSteps" 
          :key="step.id"
          class="group varnox-card transition-all duration-300 animate-on-scroll relative overflow-hidden"
          :style="{ animationDelay: `${index * 0.2}s` }"
        >
          <!-- Enhanced Step Number -->
          <div class="flex items-center mb-6">
            <div class="w-12 h-12 rounded-full flex items-center justify-center border-2 transition-all duration-300 group-hover:scale-110"
                 style="background: var(--varnox-gradient-button); border-color: var(--varnox-primary);">
              <span class="varnox-code-text text-white font-bold text-lg">
                {{ step.number.toString().padStart(2, '0') }}
              </span>
            </div>
            
            <!-- Enhanced Connection Line -->
            <div 
              v-if="index < processSteps.length - 1"
              class="hidden lg:block flex-1 h-0.5 ml-6 relative overflow-hidden"
              style="background: linear-gradient(90deg, var(--varnox-primary) 0%, transparent 100%);"
            >
              <div class="absolute inset-0 bg-gradient-to-r from-varnox-primary to-transparent animate-pulse"></div>
            </div>
          </div>
          
          <!-- Enhanced Step Icon -->
          <div class="w-16 h-16 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-105 transition-transform duration-300"
               style="background: var(--varnox-gradient-card);">
            <component :is="step.icon" class="w-8 h-8 text-varnox-primary" />
          </div>
          
          <!-- Step Content with new typography -->
          <h3 class="varnox-section-title text-xl mb-4 group-hover:text-varnox-primary transition-colors">
            {{ step.title }}
          </h3>
          <p class="varnox-body-text text-sm leading-relaxed mb-6">
            {{ step.description }}
          </p>
          
          <!-- Enhanced Step Details -->
          <div class="mb-4">
            <div class="varnox-accent-title text-xs mb-3">DELIVERABLES:</div>
            <ul class="space-y-2">
              <li 
                v-for="detail in step.details" 
                :key="detail"
                class="flex items-center varnox-body-text text-xs"
              >
                <span class="text-varnox-primary mr-2 text-sm">&gt;</span>
                {{ detail }}
              </li>
            </ul>
          </div>
          
          <!-- Status Badge -->
          <div class="absolute top-4 right-4">
            <div class="varnox-code-text text-xs px-2 py-1 rounded" 
                 style="background: var(--varnox-primary); color: white;">
              STEP_{{ step.number }}
            </div>
          </div>
          
          <!-- Animated border on hover -->
          <div class="absolute inset-0 border border-transparent group-hover:border-varnox-primary/20 rounded-lg transition-all duration-300 pointer-events-none"></div>
        </div>
      </div>
      
      <!-- Enhanced Process Timeline -->
      <div class="block lg:hidden mt-12">
        <div class="varnox-card p-4">
          <div class="flex justify-center items-center space-x-3">
            <span class="varnox-code-text text-xs">PROGRESS:</span>
            <div class="flex space-x-2">
              <div 
                v-for="(_, index) in processSteps" 
                :key="index"
                class="w-8 h-2 rounded-full transition-all duration-300"
                :class="index === 0 ? 'bg-varnox-primary animate-pulse' : 'bg-white/20'"
              ></div>
            </div>
            <span class="varnox-code-text text-xs">25%</span>
          </div>
        </div>
      </div>
      
      <!-- Enhanced Call to Action -->
      <div class="text-center mt-16 lg:mt-20 animate-on-scroll" style="animation-delay: 0.8s;">
        <div class="varnox-card p-12 relative overflow-hidden">
          <!-- Background decoration -->
          <div class="absolute inset-0 opacity-5">
            <div class="w-full h-full" style="background: var(--varnox-gradient-hero);"></div>
          </div>
          
          <div class="relative z-10">
            <div class="varnox-accent-title text-sm mb-4">
              [ LISTO PARA COMENZAR ]
            </div>
            <h3 class="varnox-display-title text-3xl md:text-4xl mb-6">
              ¿Listo para comenzar tu proyecto?
            </h3>
            <p class="varnox-body-text text-lg mb-8 max-w-2xl mx-auto">
              Transformemos tus ideas en soluciones tecnológicas que impulsen tu negocio al siguiente nivel.
            </p>
            <div class="space-x-4">
              <button 
                @click="scrollToContact"
                class="varnox-btn varnox-btn-primary"
              >
                [ DEPLOY_PROJECT ]
              </button>
              <button class="varnox-btn varnox-btn-secondary">
                Ver Metodología
              </button>
            </div>
            
            <!-- Code element -->
            <div class="varnox-code-text text-xs mt-6">
              &gt; VARNOX.initProject(yourIdea) // Let's build something amazing
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, defineComponent, h } from 'vue';

// Process step icons
const ListenIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z'
      })
    ]);
  }
});

const DesignIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM7 3H5a2 2 0 00-2 2v12a4 4 0 004 4h2a2 2 0 002-2V5a2 2 0 00-2-2zM9 9h6m-6 4h6m2 5l4-4m-4-4v8'
      })
    ]);
  }
});

const DevelopIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4'
      })
    ]);
  }
});

const DeliverIcon = defineComponent({
  setup() {
    return () => h('svg', {
      fill: 'none',
      stroke: 'currentColor',
      viewBox: '0 0 24 24',
      class: 'w-8 h-8'
    }, [
      h('path', {
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': '2',
        d: 'M5 13l4 4L19 7'
      })
    ]);
  }
});

const processSteps = [
  {
    id: 1,
    number: '01',
    icon: ListenIcon,
    title: 'Escuchamos tu necesidad',
    description: 'Analizamos profundamente tu desafío empresarial para entender exactamente qué necesitas.',
    details: [
      'Reunión de descubrimiento',
      'Análisis de requerimientos',
      'Definición de objetivos'
    ]
  },
  {
    id: 2,
    number: '02',
    icon: DesignIcon,
    title: 'Diseñamos la solución',
    description: 'Creamos la arquitectura y diseño perfecto que resuelva tu problema de manera elegante.',
    details: [
      'Prototipado y mockups',
      'Arquitectura técnica',
      'Validación de propuesta'
    ]
  },
  {
    id: 3,
    number: '03',
    icon: DevelopIcon,
    title: 'Desarrollamos e integramos',
    description: 'Construimos la solución con las mejores prácticas y tecnologías más avanzadas.',
    details: [
      'Desarrollo ágil',
      'Testing continuo',
      'Integración de sistemas'
    ]
  },
  {
    id: 4,
    number: '04',
    icon: DeliverIcon,
    title: 'Entregamos y acompañamos',
    description: 'Desplegamos la solución y brindamos soporte continuo para garantizar tu éxito.',
    details: [
      'Despliegue en producción',
      'Capacitación del equipo',
      'Soporte técnico continuo'
    ]
  }
];

const scrollToContact = () => {
  const contactSection = document.getElementById('contacto');
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' });
  }
};

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
