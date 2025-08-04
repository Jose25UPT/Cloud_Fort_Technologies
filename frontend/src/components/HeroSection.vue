<template>
  <section id="hero" class="relative min-h-screen flex flex-col justify-center items-center overflow-hidden bg-stealth-black">
    <!-- Matrix Background Grid -->
    <div class="absolute inset-0 opacity-20">
      <div class="matrix-grid"></div>
    </div>
    
    <!-- Digital Rain Effect -->
    <div class="absolute inset-0 opacity-10">
      <div class="digital-rain"></div>
    </div>
    
    <!-- Radar Pulse Effect -->
    <div class="absolute inset-0 flex items-center justify-center">
      <div class="radar-pulse"></div>
    </div>
    
    <!-- Floating Tech Elements -->
    <div class="absolute top-20 right-20 w-32 h-32 rounded-full opacity-20 tech-floating bg-gradient-to-r from-tech-green to-alert-orange"></div>
    <div class="absolute bottom-32 left-16 w-24 h-24 rounded-full opacity-20 tech-floating bg-gradient-to-r from-radar-green to-tactical-blue" style="animation-delay: 2s;"></div>
    <div class="absolute top-1/2 right-1/4 w-16 h-16 rounded-full opacity-20 tech-floating bg-gradient-to-r from-alert-orange to-tech-green" style="animation-delay: 1s;"></div>
    
    <!-- Status Panel Mejorado -->
    <div class="absolute top-20 left-6 bg-arsenal-grey/50 backdrop-blur-md border-2 border-tech-green/40 rounded p-4 font-mono text-sm shadow-xl">
      <div class="text-tech-green mb-2 font-bold">[ SYSTEM STATUS ]</div>
      <div class="flex items-center gap-2 mb-1">
        <div class="w-3 h-3 bg-tech-green rounded-full animate-pulse"></div>
        <span class="text-white font-bold">🟢 STATUS: ONLINE</span>
      </div>
      <div class="flex items-center gap-2 mb-1">
        <div class="w-3 h-3 bg-alert-orange rounded-full animate-pulse"></div>
        <span class="text-white font-bold">🟠 MISSION: ACTIVE</span>
      </div>
      <div class="flex items-center gap-2">
        <div class="w-3 h-3 bg-tech-green rounded-full animate-pulse"></div>
        <span class="text-white font-bold">🟢 THREAT_LEVEL: LOW</span>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="relative z-10 text-center px-6 lg:px-8 max-w-6xl mx-auto">
      <!-- Military Code Header -->
      <div class="mb-4 animate-fade-in font-mono text-tech-green text-sm">
        [ INITIALIZING TACTICAL PROTOCOLS ]
      </div>
      
      <!-- Main Title Mejorado -->
      <div class="mb-8 lg:mb-12 animate-fade-in bg-stealth-black/60 backdrop-blur-md border-2 border-tech-green/40 rounded-lg p-6 shadow-2xl">
        <h1 class="text-6xl md:text-8xl lg:text-9xl tracking-wider font-mono font-bold drop-shadow-lg">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-tech-green via-alert-orange to-radar-green">
            VARNOX
          </span>
        </h1>
        <div class="text-tech-green/90 text-lg md:text-xl font-mono mt-2 font-bold drop-shadow-md">
          [ TACTICAL DEVELOPMENT UNIT ]
        </div>
      </div>
      
      <!-- Military Headline Mejorado -->
      <h2 class="text-4xl md:text-6xl lg:text-7xl mb-6 lg:mb-8 animate-fade-in-up font-mono font-bold text-white drop-shadow-2xl" style="animation-delay: 0.3s;">
        DEPLOYING DIGITAL
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-tech-green to-alert-orange drop-shadow-xl">
          WARFARE
        </span>
      </h2>
      
      <!-- Terminal Style Subtitle Mejorado -->
      <div class="bg-stealth-black/60 backdrop-blur-md border border-tech-green/40 rounded-lg p-4 font-mono text-lg md:text-xl mb-12 lg:mb-16 max-w-4xl mx-auto animate-fade-in-up text-tech-green/90 shadow-xl" style="animation-delay: 0.6s;">
        <span class="text-tech-green">></span> Soluciones tecnológicas de élite<br/>
        <span class="text-tech-green">></span> Operaciones de desarrollo avanzado<br/>
        <span class="text-tech-green">></span> Misiones críticas ejecutadas con precisión militar_
      </div>
      
      <!-- Command Prompt Style -->
      <div class="font-mono text-sm md:text-base mb-8 animate-fade-in-up text-white/70" style="animation-delay: 0.7s;">
        <span class="text-tech-green">varnox@tactical:~$</span> ./deploy --mission=success --target=innovation
      </div>
      
      <!-- Military CTA Buttons Mejorados -->
      <div class="animate-fade-in-up flex flex-col sm:flex-row gap-6 justify-center" style="animation-delay: 0.9s;">
        <button 
          @click="scrollToContact"
          class="group relative overflow-hidden bg-stealth-black/60 border-2 border-tech-green text-tech-green px-8 py-4 rounded-lg font-mono font-bold text-lg transition-all duration-300 hover:bg-tech-green hover:text-stealth-black backdrop-blur-md shadow-2xl transform hover:scale-105 hover:shadow-[0_20px_25px_-5px_rgba(0,255,65,0.3)]"
        >
          <span class="relative z-10 drop-shadow-lg">[ INITIATE CONTACT ]</span>
          <div class="absolute inset-0 h-full w-full scale-0 bg-tech-green transition-all duration-300 group-hover:scale-100"></div>
        </button>
        <button 
          @click="scrollToServices"
          class="group relative overflow-hidden bg-stealth-black/60 border-2 border-alert-orange text-alert-orange px-8 py-4 rounded-lg font-mono font-bold text-lg transition-all duration-300 hover:bg-alert-orange hover:text-stealth-black backdrop-blur-md shadow-2xl transform hover:scale-105 hover:shadow-[0_20px_25px_-5px_rgba(255,107,53,0.3)]"
        >
          <span class="relative z-10 drop-shadow-lg">[ VIEW INTEL ]</span>
          <div class="absolute inset-0 h-full w-full scale-0 bg-alert-orange transition-all duration-300 group-hover:scale-100"></div>
        </button>
      </div>
      
      <!-- Terminal Output -->
      <div class="font-mono text-xs mt-8 animate-fade-in-up text-tech-green/60" style="animation-delay: 1.2s;">
        <div class="typing-animation">
          > VARNOX.init() // Systems operational<br/>
          > Deploying tactical solutions...<br/>
          > Ready for mission deployment_
        </div>
      </div>
    </div>
    
    <!-- Enhanced Military Scroll Indicator Mejorado -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 text-center animate-bounce">
      <div class="mb-3 text-tech-green font-mono text-sm font-bold drop-shadow-lg">SCROLL TO EXPLORE</div>
      <div class="flex flex-col items-center">
        <div class="w-6 h-10 border-2 border-tech-green rounded-full p-1 bg-stealth-black/40 backdrop-blur-sm shadow-lg">
          <div class="w-2 h-2 bg-tech-green rounded-full animate-ping"></div>
        </div>
        <div class="text-tech-green mt-2 animate-pulse text-lg">▼</div>
      </div>
    </div>
    
    <!-- Military Tech Elements -->
    <div class="absolute top-20 right-10 w-3 h-3 rounded-full opacity-70 animate-pulse bg-tech-green"></div>
    <div class="absolute bottom-40 left-10 w-2 h-2 rounded-full opacity-50 bg-alert-orange animate-ping"></div>
    <div class="absolute top-1/3 right-20 w-2 h-2 rounded-full opacity-60 animate-ping bg-radar-green"></div>
    <div class="absolute top-1/4 left-1/4 w-1 h-1 rounded-full opacity-40 bg-tech-green"></div>
  </section>
</template>

<script setup lang="ts">
const scrollToContact = () => {
  const contactSection = document.getElementById('contacto');
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' });
  }
};

const scrollToServices = () => {
  const servicesSection = document.getElementById('servicios');
  if (servicesSection) {
    servicesSection.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>

<style scoped>
.font-mono {
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  letter-spacing: 0.025em;
}

/* Matrix Grid Background */
.matrix-grid {
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 65, 0.1) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: grid-pulse 4s ease-in-out infinite;
}

@keyframes grid-pulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.1; }
}

/* Digital Rain Effect */
.digital-rain {
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    transparent 0px,
    rgba(0, 255, 65, 0.03) 1px,
    rgba(0, 255, 65, 0.03) 3px,
    transparent 4px
  );
  animation: digital-fall 6s linear infinite;
}

@keyframes digital-fall {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100%); }
}

/* Radar Pulse Effect */
.radar-pulse {
  width: 200px;
  height: 200px;
  border: 2px solid rgba(0, 255, 65, 0.3);
  border-radius: 50%;
  animation: radar-sweep 3s ease-in-out infinite;
}

@keyframes radar-sweep {
  0% {
    transform: scale(0.5);
    opacity: 1;
  }
  100% {
    transform: scale(2);
    opacity: 0;
  }
}

/* Tech Floating Elements */
.tech-floating {
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
  }
}

/* Tactical Button Effects */
.tactical-btn {
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.tactical-btn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.tactical-btn:hover::before {
  width: 300px;
  height: 300px;
}

.tactical-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 0 30px rgba(0, 255, 65, 0.4);
}

/* Typing Animation */
.typing-animation {
  overflow: hidden;
  border-right: 2px solid #00FF41;
  white-space: nowrap;
  animation: typing 3s steps(40) 1s forwards, blink 1s infinite;
  width: 0;
}

@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  0%, 50% { border-color: #00FF41; }
  51%, 100% { border-color: transparent; }
}

/* Fade In Animations */
.animate-fade-in {
  opacity: 0;
  animation: fadeIn 1s ease-out forwards;
}

.animate-fade-in-up {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 1s ease-out forwards;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .matrix-grid {
    background-size: 30px 30px;
  }
  
  .radar-pulse {
    width: 150px;
    height: 150px;
  }
  
  .typing-animation {
    font-size: 10px;
  }
}

@media (max-width: 640px) {
  .tech-floating {
    display: none;
  }
}

/* Enhanced visibility styles */
.glow-tech-green {
  text-shadow: 0 0 10px rgba(0, 255, 65, 0.5),
               0 0 20px rgba(0, 255, 65, 0.3),
               0 0 30px rgba(0, 255, 65, 0.2);
}

.enhanced-backdrop {
  backdrop-filter: blur(8px) brightness(1.1);
  background: rgba(13, 17, 23, 0.8);
  border: 2px solid rgba(0, 255, 65, 0.4);
  box-shadow: 0 8px 32px rgba(0, 255, 65, 0.15),
              inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.ultra-visible {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8),
               0 0 8px rgba(0, 255, 65, 0.6);
  font-weight: 900;
  letter-spacing: 0.05em;
}
</style>
