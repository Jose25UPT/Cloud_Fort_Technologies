<template>
  <section id="servicios" class="bg-pure-black section">
    <div class="max-w-7xl mx-auto">
      <!-- Section Header -->
      <div class="text-center mb-16 lg:mb-20">
        <h2 class="section-title text-pure-white animate-on-scroll">
          ¿Qué podemos crear contigo?
        </h2>
      </div>
      
      <!-- Services Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="(service, index) in services" 
          :key="service.id"
          class="service-card animate-on-scroll"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <!-- Icon -->
          <div class="w-16 h-16 bg-electric-blue/10 rounded-2xl flex items-center justify-center mb-6">
            <component :is="service.icon" class="w-8 h-8 text-electric-blue" />
          </div>
          
          <!-- Content -->
          <h3 class="font-urbanist font-bold text-xl text-pure-white mb-4">
            {{ service.title }}
          </h3>
          <p class="text-silver font-inter leading-relaxed">
            {{ service.description }}
          </p>
          
          <!-- Hover indicator -->
          <div class="mt-6 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
            <div class="w-6 h-6 border-2 border-electric-blue rounded-full flex items-center justify-center">
              <svg class="w-3 h-3 text-electric-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted, defineComponent, h } from 'vue';

// Service icons as inline SVG components
const WebIcon = defineComponent({
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
        d: 'M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9'
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
      class: 'w-8 h-8'
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

const MobileIcon = defineComponent({
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
        d: 'M12 18h.01M8 21h8a1 1 0 001-1V4a1 1 0 00-1-1H8a1 1 0 00-1 1v16a1 1 0 001 1z'
      })
    ]);
  }
});

const SecurityIcon = defineComponent({
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
        d: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z'
      })
    ]);
  }
});

const AIIcon = defineComponent({
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
        d: 'M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z'
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
      class: 'w-8 h-8'
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

const ConsultingIcon = defineComponent({
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
        d: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z'
      })
    ]);
  }
});

const services = [
  {
    id: 1,
    icon: WebIcon,
    title: 'Desarrollo Web',
    description: 'Creamos sitios web modernos, responsivos y optimizados para convertir visitantes en clientes.'
  },
  {
    id: 2,
    icon: BotIcon,
    title: 'Automatización y Bots',
    description: 'Desarrollamos bots inteligentes para automatizar procesos y mejorar la eficiencia operacional.'
  },
  {
    id: 3,
    icon: MobileIcon,
    title: 'Apps móviles / web',
    description: 'Diseñamos aplicaciones móviles y web progresivas con experiencias de usuario excepcionales.'
  },
  {
    id: 4,
    icon: SecurityIcon,
    title: 'Seguridad informática',
    description: 'Implementamos soluciones de ciberseguridad para proteger tu información y sistemas críticos.'
  },
  {
    id: 5,
    icon: AIIcon,
    title: 'Proyectos con IA',
    description: 'Integramos inteligencia artificial para automatizar decisiones y optimizar procesos empresariales.'
  },
  {
    id: 6,
    icon: CloudIcon,
    title: 'Infraestructura Cloud',
    description: 'Migramos y optimizamos tu infraestructura tecnológica en la nube para mayor escalabilidad.'
  },
  {
    id: 7,
    icon: ConsultingIcon,
    title: 'Consultoría Técnica',
    description: 'Brindamos asesoría especializada para tomar las mejores decisiones tecnológicas en tu empresa.'
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
