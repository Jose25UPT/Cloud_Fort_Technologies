<template>
  <footer class="varnox-bg-section py-16 px-6 lg:px-8 relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-10 right-20 w-64 h-64 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-hero); animation-duration: 8s;"></div>
    <div class="absolute bottom-10 left-10 w-48 h-48 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-section); animation-delay: 4s; animation-duration: 6s;"></div>
    
    <div class="max-w-7xl mx-auto relative z-10">
      <!-- Main Footer Content -->
      <div class="grid lg:grid-cols-3 gap-12 lg:gap-8 mb-12">
        
        <!-- Enhanced Brand Column -->
        <div class="lg:col-span-1">
          <!-- Logo with enhanced styling -->
          <div class="flex items-center space-x-2 mb-6">
            <div class="w-10 h-10 rounded-lg flex items-center justify-center"
                 style="background: var(--varnox-gradient-button);">
              <span class="varnox-code-text text-white font-bold">V</span>
            </div>
            <h3 class="varnox-hero-title text-2xl">
              VARNOX
            </h3>
          </div>
          
          <!-- Enhanced Brand Statement -->
          <div class="varnox-card p-4 mb-8">
            <p class="varnox-body-text leading-relaxed">
              <span class="varnox-code-text">&gt;</span> Impulsando el futuro digital desde Tacna, Perú
              <span class="text-varnox-primary animate-pulse">_</span>
            </p>
            <div class="varnox-code-text text-xs mt-2 opacity-70">
              // Building tomorrow's technology today
            </div>
          </div>
          
          <!-- Enhanced Location Badge -->
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-full flex items-center justify-center"
                 style="background: var(--varnox-gradient-card);">
              <svg class="w-5 h-5 text-varnox-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <div>
              <p class="varnox-section-title text-sm">TACNA, PERÚ</p>
              <p class="varnox-code-text text-xs opacity-70">LOCATION: { lat: -18.0, lng: -70.2 }</p>
            </div>
          </div>
        </div>
        
        <!-- Enhanced Quick Links -->
        <div class="lg:col-span-1">
          <div class="varnox-accent-title text-xs mb-6">
            [ NAVIGATION_MENU ]
          </div>
          <ul class="space-y-3">
            <li>
              <a 
                href="#home" 
                class="varnox-body-text hover:text-varnox-primary transition-colors flex items-center group"
                @click="scrollTo('home')"
              >
                <span class="mr-2 text-varnox-primary opacity-0 group-hover:opacity-100 transition-opacity">&gt;</span>
                HOME
              </a>
            </li>
            <li>
              <a 
                href="#servicios" 
                class="varnox-body-text hover:text-varnox-primary transition-colors flex items-center group"
                @click="scrollTo('servicios')"
              >
                <span class="mr-2 text-varnox-primary opacity-0 group-hover:opacity-100 transition-opacity">&gt;</span>
                SERVICES
              </a>
            </li>
            <li>
              <a 
                href="#sobre-nosotros" 
                class="varnox-body-text hover:text-varnox-primary transition-colors flex items-center group"
                @click="scrollTo('sobre-nosotros')"
              >
                <span class="mr-2 text-varnox-primary opacity-0 group-hover:opacity-100 transition-opacity">&gt;</span>
                ABOUT
              </a>
            </li>
            <li>
              <a 
                href="#proyectos" 
                class="varnox-body-text hover:text-varnox-primary transition-colors flex items-center group"
                @click="scrollTo('proyectos')"
              >
                <span class="mr-2 text-varnox-primary opacity-0 group-hover:opacity-100 transition-opacity">&gt;</span>
                PROJECTS
              </a>
            </li>
            <li>
              <a 
                href="#contact" 
                class="varnox-body-text hover:text-varnox-primary transition-colors flex items-center group"
                @click="scrollTo('contact')"
              >
                <span class="mr-2 text-varnox-primary opacity-0 group-hover:opacity-100 transition-opacity">&gt;</span>
                CONTACT
              </a>
            </li>
          </ul>
        </div>
        
        <!-- Enhanced Social & Contact -->
        <div class="lg:col-span-1">
          <div class="varnox-accent-title text-xs mb-6">
            [ CONNECT_WITH_US ]
          </div>
          
          <!-- Social Links -->
          <div class="flex space-x-4 mb-6">
            <!-- GitHub -->
            <a 
              href="https://github.com/varnox-technologies" 
              target="_blank" 
              rel="noopener noreferrer"
              class="w-12 h-12 bg-graphite rounded-full flex items-center justify-center hover:bg-electric-blue/20 hover:scale-110 transition-all duration-300 group"
            >
              <svg class="w-5 h-5 text-silver group-hover:text-electric-blue transition-colors" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
            
            <!-- LinkedIn -->
            <a 
              href="https://linkedin.com/company/varnox-technologies" 
              target="_blank" 
              rel="noopener noreferrer"
              class="w-12 h-12 bg-graphite rounded-full flex items-center justify-center hover:bg-electric-blue/20 hover:scale-110 transition-all duration-300 group"
            >
              <svg class="w-5 h-5 text-silver group-hover:text-electric-blue transition-colors" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
            </a>
          </div>
          
          <!-- Contact Info -->
          <div class="space-y-3">
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-electric-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span class="text-silver text-sm">hello@varnox.tech</span>
            </div>
            <div class="flex items-center space-x-3">
              <svg class="w-4 h-4 text-electric-blue" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <span class="text-silver text-sm">+51 999 123 456</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Terminal Command Section -->
      <div class="pt-8 border-t border-tech-green/30">
        <div class="text-center">
          <!-- Terminal prompt -->
          <div class="font-mono text-sm text-tech-green mb-2">
            varnox@tacna:~$
          </div>
          
          <!-- Copyright centered -->
          <p class="text-silver text-sm font-mono mb-2">
            © {{ new Date().getFullYear() }} VARNOX. All rights reserved.
          </p>
          
          <!-- Command line smaller and centered -->
          <div class="font-mono text-xs text-gray-400">
            echo "Ready to deploy your next mission."
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
const scrollTo = (elementId: string) => {
  const element = document.getElementById(elementId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>
