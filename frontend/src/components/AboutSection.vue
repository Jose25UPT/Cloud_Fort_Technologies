<template>
  <section id="nosotros" class="varnox-bg-section varnox-section">
    <!-- Decorative elements -->
    <div class="absolute top-10 right-10 w-20 h-20 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-section);"></div>
    <div class="absolute bottom-20 left-20 w-16 h-16 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-accent); animation-delay: 2s;"></div>
    
    <div class="max-w-7xl mx-auto relative z-10">
      <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
        <!-- Text Content -->
        <div class="animate-on-scroll">
          <!-- Section accent title -->
          <div class="varnox-accent-title text-sm mb-4">
            [ QUIÉNES SOMOS ]
          </div>
          
          <h2 class="varnox-section-title text-4xl md:text-5xl lg:text-6xl mb-8">
            Somos <span class="varnox-display-title">VARNOX</span>
          </h2>
          
          <div class="space-y-6">
            <p class="varnox-body-text text-lg md:text-xl leading-relaxed">
              Startup tecnológica fundada en <span class="text-varnox-accent font-semibold">Tacna</span>, 
              enfocada en impulsar a negocios, empresas y marcas con tecnología de vanguardia.
            </p>
            <p class="varnox-body-text text-lg md:text-xl leading-relaxed">
              Creamos <span class="text-varnox-primary font-semibold">páginas web</span>, 
              <span class="text-varnox-primary font-semibold">apps móviles</span>, 
              <span class="text-varnox-primary font-semibold">bots inteligentes</span>, 
              <span class="text-varnox-primary font-semibold">infraestructura cloud</span> y 
              soluciones basadas en <span class="text-varnox-secondary font-semibold">IA</span>.
            </p>
            
            <!-- Stats or features -->
            <div class="grid grid-cols-2 gap-6 pt-8">
              <div class="text-center p-4 rounded-xl" style="background: var(--varnox-gradient-card);">
                <div class="varnox-display-title text-2xl md:text-3xl font-bold">2024</div>
                <div class="varnox-body-text text-sm">Fundación</div>
              </div>
              <div class="text-center p-4 rounded-xl" style="background: var(--varnox-gradient-card);">
                <div class="varnox-display-title text-2xl md:text-3xl font-bold">100%</div>
                <div class="varnox-body-text text-sm">Digital</div>
              </div>
            </div>
            
            <div class="pt-6">
              <div class="flex items-center space-x-4 p-6 rounded-xl varnox-card">
                <div class="w-12 h-12 rounded-full flex items-center justify-center"
                     style="background: var(--varnox-gradient-section);">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <div>
                  <p class="varnox-section-title text-lg font-semibold">Fundada en Tacna, Perú</p>
                  <p class="varnox-body-text text-sm">Impulsando el futuro digital</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Enhanced Visual Element -->
        <div class="animate-on-scroll" style="animation-delay: 0.3s;">
          <div class="relative">
            <!-- Main visual container with new design -->
            <div class="varnox-card p-8 lg:p-12 relative overflow-hidden">
              <!-- Abstract geometric pattern with VARNOX colors -->
              <div class="absolute inset-0 opacity-10">
                <svg viewBox="0 0 400 400" class="w-full h-full">
                  <defs>
                    <linearGradient id="varnoxGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" style="stop-color:#6366F1;stop-opacity:0.3" />
                      <stop offset="50%" style="stop-color:#8B5CF6;stop-opacity:0.2" />
                      <stop offset="100%" style="stop-color:#F59E0B;stop-opacity:0.1" />
                    </linearGradient>
                  </defs>
                  <!-- Geometric shapes with VARNOX gradients -->
                  <polygon points="0,0 100,50 80,150 20,120" fill="url(#varnoxGrad1)" />
                  <polygon points="120,20 200,0 220,80 140,100" fill="url(#varnoxGrad1)" />
                  <polygon points="200,120 300,100 320,200 240,220" fill="url(#varnoxGrad1)" />
                  <polygon points="50,250 150,230 170,330 70,350" fill="url(#varnoxGrad1)" />
                  <polygon points="250,250 350,270 330,370 230,350" fill="url(#varnoxGrad1)" />
                </svg>
              </div>
              
              <!-- Content with new typography -->
              <div class="relative z-10 text-center">
                <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6"
                     style="background: var(--varnox-gradient-section);">
                  <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                          d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                  </svg>
                </div>
                <h3 class="varnox-display-title text-2xl mb-4">
                  Innovación Constante
                </h3>
                <p class="varnox-body-text">
                  Transformamos ideas en soluciones tecnológicas que impulsan el crecimiento empresarial
                </p>
                
                <!-- Code element -->
                <div class="varnox-code-text text-xs mt-4">
                  &lt;innovation&gt;true&lt;/innovation&gt;
                </div>
              </div>
              
              <!-- Enhanced decorative dots with VARNOX colors -->
              <div class="absolute top-4 right-4 w-3 h-3 rounded-full opacity-60"
                   style="background: var(--varnox-primary);"></div>
              <div class="absolute bottom-4 left-4 w-2 h-2 rounded-full opacity-40"
                   style="background: var(--varnox-accent);"></div>
              <div class="absolute top-1/2 right-8 w-1 h-1 rounded-full opacity-50"
                   style="background: var(--varnox-secondary);"></div>
            </div>
            
            <!-- Floating elements -->
            <div class="absolute -top-4 -right-4 w-8 h-8 bg-electric-blue/20 rounded-full animate-pulse"></div>
            <div class="absolute -bottom-2 -left-2 w-4 h-4 bg-silver/30 rounded-full"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

onMounted(() => {
  // Intersection Observer for scroll animations
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
