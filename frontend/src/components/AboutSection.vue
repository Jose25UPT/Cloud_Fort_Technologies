<template>
  <section id="nosotros" class="bg-space-grey section">
    <div class="max-w-7xl mx-auto">
      <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
        <!-- Text Content -->
        <div class="animate-on-scroll">
          <h2 class="section-title text-pure-white">
            Somos CLOUDFORT TECHNOLOGIES
          </h2>
          <div class="space-y-6">
            <p class="text-silver text-lg md:text-xl leading-relaxed font-inter">
              Startup tecnológica fundada en <span class="text-pure-white font-medium">Tacna</span>, 
              enfocada en impulsar a negocios, empresas y marcas con tecnología de vanguardia.
            </p>
            <p class="text-silver text-lg md:text-xl leading-relaxed font-inter">
              Creamos <span class="text-electric-blue font-medium">páginas web</span>, 
              <span class="text-electric-blue font-medium">apps móviles</span>, 
              <span class="text-electric-blue font-medium">bots inteligentes</span>, 
              <span class="text-electric-blue font-medium">infraestructura cloud</span> y 
              soluciones basadas en <span class="text-electric-blue font-medium">IA</span>.
            </p>
            <div class="pt-6">
              <div class="flex items-center space-x-4">
                <div class="w-12 h-12 bg-electric-blue/10 rounded-full flex items-center justify-center">
                  <svg class="w-6 h-6 text-electric-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <div>
                  <p class="font-space-grotesk font-medium text-pure-white">Fundada en Tacna, Perú</p>
                  <p class="text-silver text-sm">Impulsando el futuro digital</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Visual Element -->
        <div class="animate-on-scroll" style="animation-delay: 0.3s;">
          <div class="relative">
            <!-- Main visual container -->
            <div class="bg-graphite rounded-3xl p-8 lg:p-12 relative overflow-hidden">
              <!-- Abstract geometric pattern -->
              <div class="absolute inset-0 opacity-10">
                <svg viewBox="0 0 400 400" class="w-full h-full">
                  <defs>
                    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" style="stop-color:#0A84FF;stop-opacity:0.3" />
                      <stop offset="100%" style="stop-color:#0A84FF;stop-opacity:0.1" />
                    </linearGradient>
                  </defs>
                  <polygon points="0,0 100,50 80,150 20,120" fill="url(#grad1)" />
                  <polygon points="120,20 200,0 220,80 140,100" fill="url(#grad1)" />
                  <polygon points="200,120 300,100 320,200 240,220" fill="url(#grad1)" />
                  <polygon points="50,250 150,230 170,330 70,350" fill="url(#grad1)" />
                  <polygon points="250,250 350,270 330,370 230,350" fill="url(#grad1)" />
                </svg>
              </div>
              
              <!-- Content -->
              <div class="relative z-10 text-center">
                <div class="w-20 h-20 bg-electric-blue/20 rounded-full flex items-center justify-center mx-auto mb-6">
                  <svg class="w-10 h-10 text-electric-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                          d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                  </svg>
                </div>
                <h3 class="font-urbanist font-bold text-2xl text-pure-white mb-4">
                  Innovación Constante
                </h3>
                <p class="text-silver font-inter">
                  Transformamos ideas en soluciones tecnológicas que impulsan el crecimiento empresarial
                </p>
              </div>
              
              <!-- Decorative dots -->
              <div class="absolute top-4 right-4 w-2 h-2 bg-electric-blue rounded-full opacity-60"></div>
              <div class="absolute bottom-4 left-4 w-1 h-1 bg-silver rounded-full opacity-40"></div>
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
