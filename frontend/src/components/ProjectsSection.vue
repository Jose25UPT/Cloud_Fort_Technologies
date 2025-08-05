<template>
  <section id="proyectos" class="bg-gradient-to-br from-gray-50 via-white to-indigo-50/30 py-20 lg:py-32 relative overflow-hidden hexagonal-grid-pattern">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <div class="text-indigo-600 text-sm mb-4 tracking-wider uppercase font-semibold">
          Proyectos Desplegados
        </div>
        
        <h2 class="text-4xl md:text-5xl font-bold mb-8 text-gray-900">
          <span class="bg-gradient-to-r from-indigo-600 via-purple-600 to-amber-500 bg-clip-text text-transparent">Nuestros</span> Proyectos
        </h2>
        
        <div class="bg-white p-8 rounded-2xl border border-gray-200 shadow-xl max-w-4xl mx-auto">
          <p class="text-gray-700 text-lg leading-relaxed mb-4">
            <span class="text-indigo-600 font-bold">></span> Operaciones completadas con éxito absoluto
            <span class="text-indigo-600 animate-pulse">_</span>
          </p>
          <p class="text-gray-600 text-base">
            Cada proyecto representa una misión cumplida y un cliente satisfecho con resultados excepcionales.
          </p>
        </div>
      </div>
      
      <!-- Projects Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div 
          v-for="project in projects" 
          :key="project.id"
          class="bg-white rounded-2xl border border-gray-200 shadow-xl transition-all duration-500 overflow-hidden hover:shadow-2xl hover:scale-105"
        >
          <!-- Project Header -->
          <div class="p-6 border-b border-gray-100">
            <div class="flex items-center justify-between mb-4">
              <span class="text-2xl">{{ project.icon }}</span>
              <span class="px-3 py-1 text-xs font-semibold rounded-full bg-green-100 text-green-800">
                {{ project.status }}
              </span>
            </div>
            
            <h3 class="text-xl font-bold text-gray-900 mb-2">{{ project.title }}</h3>
            <p class="text-indigo-600 text-sm font-medium mb-4">{{ project.category }}</p>
            <p class="text-gray-600 text-sm leading-relaxed">{{ project.description }}</p>
          </div>
          
          <!-- Tech Stack -->
          <div class="p-6 border-b border-gray-100">
            <h4 class="text-sm font-semibold text-gray-700 mb-3">Tecnologías:</h4>
            <div class="flex flex-wrap gap-2">
              <span 
                v-for="tech in project.tech" 
                :key="tech"
                class="px-2 py-1 text-xs font-medium bg-indigo-100 text-indigo-700 rounded"
              >
                {{ tech }}
              </span>
            </div>
          </div>
          
          <!-- Metrics -->
          <div class="p-6 space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-sm font-semibold text-gray-700">Rendimiento:</span>
              <span class="text-indigo-700 font-bold">{{ project.metrics.performance }}</span>
            </div>
            
            <div class="flex items-center justify-between">
              <span class="text-sm font-semibold text-gray-700">Satisfacción:</span>
              <span class="text-purple-700 font-bold">{{ project.metrics.satisfaction }}</span>
            </div>
            
            <div class="flex items-center justify-between">
              <span class="text-sm font-semibold text-gray-700">Mejora:</span>
              <span class="text-amber-700 font-bold">{{ project.metrics.improvement }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const projects = ref([
  {
    id: 1,
    title: "VARNOX Corporativo",
    category: "Desarrollo Empresarial",
    description: "Plataforma integral de gestión empresarial con módulos avanzados de analítica y automatización de procesos críticos.",
    tech: ["Vue.js", "TypeScript", "Node.js", "PostgreSQL"],
    metrics: {
      performance: "98%",
      satisfaction: "96%",
      improvement: "45%"
    },
    status: "Activo",
    icon: "🏢"
  },
  {
    id: 2,
    title: "VARNOX Asistente",
    category: "Inteligencia Artificial",
    description: "Sistema de asistencia inteligente con capacidades de procesamiento de lenguaje natural y aprendizaje automático.",
    tech: ["Python", "TensorFlow", "FastAPI", "Docker"],
    metrics: {
      performance: "94%",
      satisfaction: "92%",
      improvement: "67%"
    },
    status: "Activo",
    icon: "🤖"
  },
  {
    id: 3,
    title: "VARNOX Mobile",
    category: "Aplicación Móvil",
    description: "Aplicación móvil multiplataforma con funcionalidades avanzadas de sincronización y experiencia de usuario optimizada.",
    tech: ["React Native", "TypeScript", "GraphQL", "MongoDB"],
    metrics: {
      performance: "91%",
      satisfaction: "89%",
      improvement: "38%"
    },
    status: "Desarrollo",
    icon: "📱"
  }
])
</script>

<style scoped>
.hexagonal-grid-pattern {
  background-image: 
    radial-gradient(circle at 1px 1px, rgba(139, 92, 246, 0.45) 1px, transparent 0),
    radial-gradient(circle at 8px 8px, rgba(99, 102, 241, 0.42) 1px, transparent 0),
    radial-gradient(circle at 15px 15px, rgba(255, 255, 255, 0.38) 1px, transparent 0);
  background-size: 16px 16px, 24px 24px, 32px 32px;
  background-position: 0 0, 8px 8px, 16px 16px;
}
</style>
