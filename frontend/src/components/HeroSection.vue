<template>
  <section id="hero" class="bg-pure-black min-h-screen flex flex-col justify-center items-center relative overflow-hidden">
    <!-- Background subtle pattern/gradient -->
    <div class="absolute inset-0 bg-gradient-to-br from-pure-black via-pure-black to-space-grey opacity-50"></div>
    
    <!-- Main content -->
    <div class="relative z-10 text-center px-6 lg:px-8 max-w-6xl mx-auto">
      <!-- Logo -->
      <div class="mb-8 lg:mb-12 animate-fade-in">
        <h1 class="font-urbanist font-bold text-2xl md:text-3xl text-pure-white tracking-wider">
          CLOUDFORT TECHNOLOGIES
        </h1>
      </div>
      
      <!-- Main headline -->
      <h2 class="hero-title text-pure-white mb-6 lg:mb-8 animate-fade-in-up" style="animation-delay: 0.3s;">
        Hacemos realidad tu mundo tecnológico
      </h2>
      
      <!-- Subtitle -->
      <p class="section-subtitle text-silver mb-12 lg:mb-16 max-w-4xl mx-auto animate-fade-in-up" style="animation-delay: 0.6s;">
        Creamos soluciones inteligentes para empresas del presente y del futuro
      </p>
      
      <!-- CTA Button -->
      <div class="animate-fade-in-up" style="animation-delay: 0.9s;">
        <button 
          @click="scrollToContact"
          class="btn btn-primary font-space-grotesk text-lg"
        >
          Contáctanos
        </button>
      </div>
    </div>
    
    <!-- Scroll indicator -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
      <div class="w-6 h-10 border-2 border-silver rounded-full flex justify-center">
        <div class="w-1 h-3 bg-silver rounded-full mt-2 animate-pulse"></div>
      </div>
    </div>
    
    <!-- Decorative elements -->
    <div class="absolute top-20 right-10 w-2 h-2 bg-electric-blue rounded-full opacity-70 animate-pulse"></div>
    <div class="absolute bottom-40 left-10 w-1 h-1 bg-silver rounded-full opacity-50"></div>
    <div class="absolute top-1/3 right-20 w-1 h-1 bg-electric-blue rounded-full opacity-60 animate-ping"></div>
  </section>
</template>

<script setup lang="ts">
const scrollToContact = () => {
  const contactSection = document.getElementById('contacto');
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>
