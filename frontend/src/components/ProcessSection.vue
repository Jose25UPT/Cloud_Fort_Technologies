<template>
  <section id="proceso" class="bg-pure-black section">
    <div class="max-w-7xl mx-auto">
      <!-- Section Header -->
      <div class="text-center mb-16 lg:mb-20">
        <h2 class="section-title text-pure-white animate-on-scroll">
          Así trabajamos contigo
        </h2>
      </div>
      
      <!-- Process Steps -->
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-6">
        <div 
          v-for="(step, index) in processSteps" 
          :key="step.id"
          class="process-card animate-on-scroll group"
          :style="{ animationDelay: `${index * 0.2}s` }"
        >
          <!-- Step Number -->
          <div class="flex items-center mb-6">
            <div class="w-12 h-12 bg-electric-blue/10 rounded-full flex items-center justify-center border-2 border-electric-blue/20 group-hover:border-electric-blue/50 transition-colors">
              <span class="font-urbanist font-bold text-electric-blue text-lg">
                {{ step.number }}
              </span>
            </div>
            
            <!-- Connection Line (except for last step) -->
            <div 
              v-if="index < processSteps.length - 1"
              class="hidden lg:block flex-1 h-px bg-graphite/50 ml-6"
            ></div>
          </div>
          
          <!-- Step Icon -->
          <div class="w-16 h-16 bg-space-grey rounded-2xl flex items-center justify-center mb-6 group-hover:bg-graphite/50 transition-colors">
            <component :is="step.icon" class="w-8 h-8 text-electric-blue" />
          </div>
          
          <!-- Step Content -->
          <h3 class="font-urbanist font-bold text-xl text-pure-white mb-4 group-hover:text-electric-blue transition-colors">
            {{ step.title }}
          </h3>
          <p class="text-silver font-inter leading-relaxed mb-6">
            {{ step.description }}
          </p>
          
          <!-- Step Details -->
          <ul class="space-y-2">
            <li 
              v-for="detail in step.details" 
              :key="detail"
              class="flex items-center text-sm text-silver/80"
            >
              <div class="w-1.5 h-1.5 bg-electric-blue rounded-full mr-3"></div>
              {{ detail }}
            </li>
          </ul>
          
          <!-- Hover Effect -->
          <div class="absolute inset-0 bg-electric-blue/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300 -z-10"></div>
        </div>
      </div>
      
      <!-- Process Timeline (Mobile) -->
      <div class="block lg:hidden mt-12">
        <div class="flex justify-center">
          <div class="flex space-x-4">
            <div 
              v-for="(_, index) in processSteps" 
              :key="index"
              class="w-8 h-2 rounded-full"
              :class="index === 0 ? 'bg-electric-blue' : 'bg-graphite'"
            ></div>
          </div>
        </div>
      </div>
      
      <!-- Call to Action -->
      <div class="text-center mt-16 lg:mt-20 animate-on-scroll" style="animation-delay: 0.8s;">
        <p class="text-silver font-inter text-lg mb-8">
          ¿Listo para comenzar tu proyecto tecnológico?
        </p>
        <button 
          @click="scrollToContact"
          class="btn btn-primary font-space-grotesk"
        >
          Iniciemos juntos
        </button>
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
