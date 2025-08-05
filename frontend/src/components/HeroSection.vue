<template>
  <section id="hero" class="relative min-h-screen flex flex-col justify-center items-center overflow-hidden">
    <!-- Fondo Degradado Tipo Escama -->
    <div class="absolute inset-0 scale-pattern-bg"></div>
    
    <!-- Overlay de Gradiente Elegante -->
    <div class="absolute inset-0 bg-gradient-to-br from-slate-900 via-indigo-900 to-purple-900"></div>
    
    <!-- Efectos de Luz Dinámicos -->
    <div class="absolute inset-0">
      <div class="floating-orb orb-1"></div>
      <div class="floating-orb orb-2"></div>
      <div class="floating-orb orb-3"></div>
    </div>
    
    <!-- Patrón de Partículas -->
    <div class="absolute inset-0 particles-container">
      <div class="particle p-1"></div>
      <div class="particle p-2"></div>
      <div class="particle p-3"></div>
      <div class="particle p-4"></div>
      <div class="particle p-5"></div>
    </div>
    
    <!-- Status Panel Militar Tecnológico -->
    <div class="absolute top-20 left-6 bg-slate-900 backdrop-blur-lg border border-green-500 rounded p-4 font-mono text-sm shadow-2xl">
      <div class="text-green-400 mb-3 font-bold text-xs tracking-wider">[ TACTICAL STATUS ]</div>
      <div class="flex items-center gap-3 mb-2">
        <div class="w-2 h-2 bg-green-400 rounded-full shadow-green-400 shadow-lg"></div>
        <span class="text-green-300 font-medium">SISTEMAS OPERATIVOS</span>
      </div>
      <div class="flex items-center gap-3 mb-2">
        <div class="w-2 h-2 bg-amber-400 rounded-full shadow-amber-400 shadow-lg"></div>
        <span class="text-amber-300 font-medium">MISIONES ACTIVAS</span>
      </div>
      <div class="flex items-center gap-3">
        <div class="w-2 h-2 bg-red-400 rounded-full shadow-red-400 shadow-lg"></div>
        <span class="text-red-300 font-medium">DEFCON 2 - READY</span>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="relative z-10 text-center px-6 lg:px-8 max-w-6xl mx-auto">
      <!-- Header Militar -->
      <div class="mb-6 animate-fade-in font-mono text-green-400 text-sm tracking-wider">
        [ TACTICAL OPERATIONS COMMAND - VARNOX ]
      </div>
      
      <!-- Main Title Militar -->
      <div class="mb-8 lg:mb-12 animate-fade-in">
        <h1 class="text-6xl md:text-8xl lg:text-9xl tracking-wider font-mono font-bold">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-green-400 via-red-400 to-amber-400 drop-shadow-2xl">
            VARNOX
          </span>
        </h1>
        <div class="text-green-300 text-lg md:text-xl font-mono mt-4 font-medium tracking-widest">
          ADVANCED WARFARE TECHNOLOGIES
        </div>
      </div>
      
      <!-- Headline Militar -->
      <h2 class="text-4xl md:text-6xl lg:text-7xl mb-8 animate-fade-in-up font-mono font-bold text-white drop-shadow-2xl" style="animation-delay: 0.3s;">
        DEPLOY DIGITAL
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-amber-400">
          SUPREMACY
        </span>
      </h2>
      
      <!-- Subtitle Militar -->
      <div class="bg-slate-900/80 backdrop-blur-lg border border-green-500/30 rounded p-6 font-mono text-lg md:text-xl mb-12 lg:mb-16 max-w-4xl mx-auto animate-fade-in-up shadow-2xl" style="animation-delay: 0.6s;">
        <div class="text-slate-200 leading-relaxed">
          <span class="text-green-400 font-semibold">▶</span> TACTICAL WEB & MOBILE SYSTEMS<br/>
          <span class="text-red-400 font-semibold">▶</span> FORTIFIED CLOUD INFRASTRUCTURE<br/>
          <span class="text-amber-400 font-semibold">▶</span> NEXT-GEN MISSION CRITICAL SOLUTIONS
        </div>
      </div>
      
      <!-- Code Display Militar -->
      <div class="font-mono text-sm md:text-base mb-8 animate-fade-in-up text-slate-400" style="animation-delay: 0.7s;">
        <span class="text-green-400">varnox@tactical:~$</span> ./deploy --mode=classified --target=domination
      </div>
      
      <!-- CTA Buttons Militares -->
      <div class="animate-fade-in-up flex flex-col sm:flex-row gap-6 justify-center" style="animation-delay: 0.9s;">
        <button 
          @click="scrollToContact"
          class="group relative overflow-hidden bg-gradient-to-r from-green-600 via-red-600 to-amber-500 text-white px-8 py-4 rounded font-mono font-bold text-lg transition-all duration-300 shadow-2xl hover:shadow-red-500/30 transform hover:scale-105 border border-green-500/50"
        >
          <span class="relative z-10">[ INITIATE MISSION ]</span>
          <div class="absolute inset-0 bg-gradient-to-r from-red-600 via-green-600 to-amber-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </button>
        <button 
          @click="scrollToServices"
          class="group relative overflow-hidden bg-slate-900/80 border-2 border-green-500 text-green-300 px-8 py-4 rounded font-mono font-bold text-lg transition-all duration-300 backdrop-blur-lg shadow-2xl hover:bg-green-500 hover:text-black transform hover:scale-105"
        >
          <span class="relative z-10">[ INTEL BRIEFING ]</span>
        </button>
      </div>
      
      <!-- Output Terminal Militar -->
      <div class="font-mono text-xs mt-8 animate-fade-in-up text-green-400" style="animation-delay: 1.2s;">
        <div class="typing-animation">
          > VARNOX_TACTICAL.initialize() // Sistema de combate activado<br/>
          > Cargando arsenales tecnológicos...<br/>
          > Comando listo para operaciones de élite_
        </div>
      </div>
    </div>
    
    <!-- Scroll Indicator Militar -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 text-center animate-bounce">
      <div class="mb-3 text-green-400 font-mono text-sm font-medium tracking-wide">CONTINUE_MISSION</div>
      <div class="flex flex-col items-center">
        <div class="w-6 h-10 border-2 border-green-400 rounded-sm p-1 bg-slate-900 backdrop-blur-sm shadow-lg">
          <div class="w-2 h-2 bg-green-400 rounded-sm animate-ping"></div>
        </div>
        <svg class="w-6 h-6 text-green-400 mt-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
        </svg>
      </div>
    </div>
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
/* Tipografías VARNOX */
.font-orbitron {
  font-family: 'Orbitron', monospace;
  letter-spacing: 0.05em;
}

.font-poppins {
  font-family: 'Poppins', sans-serif;
  letter-spacing: 0.025em;
}

.font-jetbrains {
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.05em;
}

/* Fondo Degradado Tipo Escama */
.scale-pattern-bg {
  background: 
    radial-gradient(circle at 25% 25%, #1e1b4b 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, #312e81 0%, transparent 50%),
    radial-gradient(circle at 25% 75%, #581c87 0%, transparent 50%),
    radial-gradient(circle at 75% 25%, #7c2d12 0%, transparent 50%),
    linear-gradient(45deg, 
      rgba(30, 27, 75, 0.8) 0%, 
      rgba(49, 46, 129, 0.6) 25%, 
      rgba(88, 28, 135, 0.7) 50%, 
      rgba(124, 45, 18, 0.5) 75%, 
      rgba(30, 27, 75, 0.8) 100%
    );
  background-size: 100px 100px, 150px 150px, 120px 120px, 80px 80px, 100% 100%;
  background-position: 0 0, 50px 50px, 25px 75px, 75px 25px, 0 0;
  animation: scale-flow 12s ease-in-out infinite;
}

@keyframes scale-flow {
  0%, 100% {
    background-position: 0 0, 50px 50px, 25px 75px, 75px 25px, 0 0;
  }
  25% {
    background-position: 20px 20px, 70px 30px, 45px 95px, 95px 5px, 0 0;
  }
  50% {
    background-position: -20px 20px, 30px 70px, 5px 55px, 55px 45px, 0 0;
  }
  75% {
    background-position: 10px -10px, 60px 60px, 35px 85px, 85px 15px, 0 0;
  }
}

/* Efectos de Luz Dinámicos */
.floating-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(1px);
  animation: float-orb 8s ease-in-out infinite;
}

.orb-1 {
  top: 20%;
  left: 20%;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(99, 102, 241, 1) 0%, transparent 70%);
  animation-delay: 0s;
}

.orb-2 {
  top: 60%;
  right: 20%;
  width: 150px;
  height: 150px;
  background: radial-gradient(circle, rgba(139, 92, 246, 1) 0%, transparent 70%);
  animation-delay: 2s;
}

.orb-3 {
  bottom: 20%;
  left: 60%;
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, rgba(245, 158, 11, 1) 0%, transparent 70%);
  animation-delay: 4s;
}

@keyframes float-orb {
  0%, 100% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
  33% {
    transform: translate(30px, -20px) scale(1.1);
    opacity: 1;
  }
  66% {
    transform: translate(-20px, 30px) scale(0.9);
    opacity: 1;
  }
}

/* Partículas Animadas */
.particles-container {
  overflow: hidden;
}

.particle {
  position: absolute;
  width: 2px;
  height: 2px;
  background: rgba(99, 102, 241, 0.8);
  border-radius: 50%;
  animation: particle-float 6s linear infinite;
}

.p-1 {
  top: 10%;
  left: 10%;
  animation-delay: 0s;
  background: rgba(139, 92, 246, 0.8);
}

.p-2 {
  top: 30%;
  left: 70%;
  animation-delay: 1.2s;
  background: rgba(245, 158, 11, 0.8);
}

.p-3 {
  top: 70%;
  left: 20%;
  animation-delay: 2.4s;
  background: rgba(99, 102, 241, 0.8);
}

.p-4 {
  top: 50%;
  left: 80%;
  animation-delay: 3.6s;
  background: rgba(139, 92, 246, 0.8);
}

.p-5 {
  top: 80%;
  left: 60%;
  animation-delay: 4.8s;
  background: rgba(245, 158, 11, 0.8);
}

@keyframes particle-float {
  0% {
    transform: translateY(0) translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  90% {
    opacity: 1;
  }
  100% {
    transform: translateY(-100vh) translateX(50px);
    opacity: 0;
  }
}

/* Animación de Escritura */
.typing-animation {
  overflow: hidden;
  border-right: 2px solid #6366f1;
  white-space: nowrap;
  animation: typing 3s steps(40) 1s forwards, blink 1s infinite;
  width: 0;
}

@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  0%, 50% { border-color: #6366f1; }
  51%, 100% { border-color: transparent; }
}

/* Animaciones de Entrada */
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

/* Efectos de Botones */
.group:hover .group-hover\:opacity-100 {
  opacity: 1;
}

/* Efectos de Sombra para Indicadores */
.shadow-green-400\/50 {
  box-shadow: 0 0 10px rgba(74, 222, 128, 0.5);
}

.shadow-amber-400\/50 {
  box-shadow: 0 0 10px rgba(251, 191, 36, 0.5);
}

.shadow-purple-400\/50 {
  box-shadow: 0 0 10px rgba(168, 85, 247, 0.5);
}

/* Responsive Design */
@media (max-width: 768px) {
  .scale-pattern-bg {
    background-size: 60px 60px, 90px 90px, 70px 70px, 50px 50px, 100% 100%;
  }
  
  .floating-orb {
    display: none;
  }
  
  .particle {
    display: none;
  }
  
  .typing-animation {
    font-size: 10px;
  }
}

@media (max-width: 640px) {
  .scale-pattern-bg {
    background-size: 40px 40px, 60px 60px, 50px 50px, 30px 30px, 100% 100%;
  }
}

/* Glass Morphism Mejorado */
.backdrop-blur-lg {
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
}

/* Mejoras de Contraste y Visibilidad */
.drop-shadow-2xl {
  filter: drop-shadow(0 25px 25px rgb(0 0 0 / 0.15));
}

/* Efectos de Gradiente Animado */
.bg-gradient-to-r {
  background-size: 200% 200%;
  animation: gradient-shift 4s ease infinite;
}

@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
