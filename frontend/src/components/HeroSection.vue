<template>
  <section id="hero" class="relative min-h-screen flex flex-col justify-center items-center overflow-hidden bg-slate-900">
    <!-- Tactical Grid Background -->
    <div class="absolute inset-0 tactical-grid-bg"></div>
    
    <!-- Military Overlay -->
    <div class="absolute inset-0 bg-gradient-to-br from-slate-900 via-gray-900 to-black opacity-95"></div>
    
    <!-- HUD Elements -->
    <div class="absolute inset-0">
      <div class="tactical-scanner scanner-1"></div>
      <div class="tactical-scanner scanner-2"></div>
      <div class="tactical-scanner scanner-3"></div>
    </div>
    
    <!-- Circuit Pattern Overlay -->
    <div class="absolute inset-0 circuit-pattern">
      <div class="circuit c-1"></div>
      <div class="circuit c-2"></div>
      <div class="circuit c-3"></div>
      <div class="circuit c-4"></div>
    </div>
    
    <!-- Military Command Panel -->
    <div class="absolute top-20 left-6 bg-black/80 backdrop-blur-lg border border-green-400 rounded-none p-4 font-mono text-sm shadow-2xl">
      <div class="text-green-400 mb-3 font-bold text-xs tracking-wider">[ VARNOX COMMAND CENTER ]</div>
      <div class="flex items-center gap-3 mb-2">
        <div class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
        <span class="text-green-300 font-medium">SYSTEMS: OPERATIONAL</span>
      </div>
      <div class="flex items-center gap-3 mb-2">
        <div class="w-2 h-2 bg-orange-400 rounded-full animate-pulse"></div>
        <span class="text-orange-300 font-medium">SECURITY: ENHANCED</span>
      </div>
      <div class="flex items-center gap-3">
        <div class="w-2 h-2 bg-red-400 rounded-full animate-pulse"></div>
        <span class="text-red-300 font-medium">THREAT LEVEL: MINIMAL</span>
      </div>
    </div>
    
    <!-- Mission Timer -->
    <div class="absolute top-20 right-6 bg-black/80 backdrop-blur-lg border border-blue-400 rounded-none p-4 font-mono text-sm shadow-2xl">
      <div class="text-blue-400 mb-3 font-bold text-xs tracking-wider">[ MISSION TIMER ]</div>
      <div class="text-blue-300 text-lg font-bold" id="mission-timer">00:00:00</div>
      <div class="text-blue-300/60 text-xs mt-1">UPTIME SINCE DEPLOYMENT</div>
    </div>
    
    <!-- Main Content -->
    <div class="relative z-10 text-center px-6 lg:px-8 max-w-6xl mx-auto">
      <!-- Tactical Header -->
      <div class="mb-6 animate-fade-in font-mono text-green-400 text-sm tracking-wider">
        <span class="text-green-400">[</span> 
        <span class="text-green-300">VARNOX TACTICAL SYSTEMS</span>
        <span class="text-green-400">]</span>
        <span class="text-green-400 animate-pulse ml-2">█</span>
      </div>
      
      <!-- Main Military Title -->
      <div class="mb-8 lg:mb-12 animate-fade-in">
        <h1 class="text-6xl md:text-8xl lg:text-9xl tracking-wider font-mono font-bold">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-green-400 via-orange-400 to-blue-400 drop-shadow-2xl">
            VARNOX
          </span>
        </h1>
        <div class="text-green-300 text-lg md:text-xl font-mono mt-4 font-medium tracking-widest">
          TACTICAL CYBER OPERATIONS
        </div>
      </div>
      
      <!-- Military Headline -->
      <h2 class="text-4xl md:text-6xl lg:text-7xl mb-8 animate-fade-in-up font-mono font-bold text-white drop-shadow-2xl" style="animation-delay: 0.3s;">
        CYBER
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-red-400">
          WARFARE
        </span>
        DIVISION
      </h2>
      
      <!-- Military Subtitle -->
      <div class="bg-black/80 backdrop-blur-lg border border-green-500/30 rounded-none p-6 font-mono text-lg md:text-xl mb-12 lg:mb-16 max-w-4xl mx-auto animate-fade-in-up shadow-2xl" style="animation-delay: 0.6s;">
        <div class="text-slate-200 leading-relaxed">
          <span class="text-green-400 font-semibold">></span> ADVANCED CYBERSECURITY SYSTEMS<br/>
          <span class="text-orange-400 font-semibold">></span> MILITARY-GRADE INFRASTRUCTURE<br/>
          <span class="text-blue-400 font-semibold">></span> CLASSIFIED MISSION SOLUTIONS
        </div>
      </div>
      
      <!-- Terminal Command Display -->
      <div class="font-mono text-sm md:text-base mb-8 animate-fade-in-up text-slate-400" style="animation-delay: 0.7s;">
        <span class="text-green-400">root@varnox:~$</span> 
        <span class="text-white">./initiate</span> 
        <span class="text-orange-400">--classified</span> 
        <span class="text-blue-400">--security=maximum</span>
        <span class="text-green-400 animate-pulse">█</span>
      </div>
      
      <!-- Military CTA Buttons -->
      <div class="animate-fade-in-up flex flex-col sm:flex-row gap-6 justify-center" style="animation-delay: 0.9s;">
        <button 
          @click="scrollToContact"
          class="group relative overflow-hidden bg-gradient-to-r from-green-600 via-orange-600 to-red-600 text-white px-8 py-4 rounded-none font-mono font-bold text-lg transition-all duration-300 shadow-2xl hover:shadow-green-500/30 transform hover:scale-105 border border-green-500/50"
        >
          <span class="relative z-10">[ ENGAGE OPERATIONS ]</span>
          <div class="absolute inset-0 bg-gradient-to-r from-orange-600 via-red-600 to-green-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
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
import { onMounted, onUnmounted } from 'vue'

let missionTimer: NodeJS.Timeout | null = null

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

const updateMissionTimer = () => {
  const startTime = new Date('2024-01-01T00:00:00Z').getTime()
  const now = new Date().getTime()
  const elapsed = now - startTime
  
  const hours = Math.floor(elapsed / (1000 * 60 * 60))
  const minutes = Math.floor((elapsed % (1000 * 60 * 60)) / (1000 * 60))
  const seconds = Math.floor((elapsed % (1000 * 60)) / 1000)
  
  const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
  
  const timerElement = document.getElementById('mission-timer')
  if (timerElement) {
    timerElement.textContent = formattedTime
  }
}

onMounted(() => {
  updateMissionTimer()
  missionTimer = setInterval(updateMissionTimer, 1000)
})

onUnmounted(() => {
  if (missionTimer) {
    clearInterval(missionTimer)
  }
})
</script>

<style scoped>
/* VARNOX Tactical Typography */
.font-orbitron {
  font-family: 'Orbitron', monospace;
  letter-spacing: 0.1em;
}

.font-jetbrains {
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.05em;
}

/* Tactical Grid Background */
.tactical-grid-bg {
  background-image: 
    linear-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 65, 0.1) 1px, transparent 1px),
    linear-gradient(rgba(255, 107, 53, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 107, 53, 0.05) 1px, transparent 1px);
  background-size: 50px 50px, 50px 50px, 10px 10px, 10px 10px;
  background-position: 0 0, 0 0, 0 0, 0 0;
  animation: grid-scan 8s linear infinite;
}

@keyframes grid-scan {
  0% { background-position: 0 0, 0 0, 0 0, 0 0; }
  100% { background-position: 50px 50px, 50px 50px, 10px 10px, 10px 10px; }
}

/* Tactical Scanners */
.tactical-scanner {
  position: absolute;
  border: 2px solid rgba(0, 255, 65, 0.3);
  border-radius: 50%;
  animation: scanner-pulse 3s ease-in-out infinite;
}

.scanner-1 {
  top: 20%;
  left: 10%;
  width: 200px;
  height: 200px;
  animation-delay: 0s;
}

.scanner-2 {
  top: 60%;
  right: 15%;
  width: 150px;
  height: 150px;
  animation-delay: 1s;
}

.scanner-3 {
  bottom: 20%;
  left: 20%;
  width: 100px;
  height: 100px;
  animation-delay: 2s;
}

@keyframes scanner-pulse {
  0%, 100% { 
    transform: scale(1);
    border-color: rgba(0, 255, 65, 0.3);
  }
  50% { 
    transform: scale(1.2);
    border-color: rgba(0, 255, 65, 0.8);
  }
}

/* Circuit Pattern */
.circuit-pattern {
  opacity: 0.3;
}

.circuit {
  position: absolute;
  background: linear-gradient(90deg, transparent 40%, rgba(0, 255, 65, 0.5) 50%, transparent 60%);
  animation: circuit-flow 4s linear infinite;
}

.c-1 {
  top: 25%;
  left: 0;
  width: 100%;
  height: 2px;
  animation-delay: 0s;
}

.c-2 {
  top: 0;
  left: 30%;
  width: 2px;
  height: 100%;
  background: linear-gradient(0deg, transparent 40%, rgba(255, 107, 53, 0.5) 50%, transparent 60%);
  animation-delay: 1s;
}

.c-3 {
  top: 75%;
  left: 0;
  width: 100%;
  height: 2px;
  animation-delay: 2s;
}

.c-4 {
  top: 0;
  right: 20%;
  width: 2px;
  height: 100%;
  background: linear-gradient(0deg, transparent 40%, rgba(10, 132, 255, 0.5) 50%, transparent 60%);
  animation-delay: 3s;
}

@keyframes circuit-flow {
  0% { opacity: 0.2; }
  50% { opacity: 1; }
  100% { opacity: 0.2; }
}

/* Tactical Animations */
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
  to { opacity: 1; }
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Terminal Cursor */
.terminal-cursor {
  animation: cursor-blink 1s infinite;
}

@keyframes cursor-blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* HUD Elements */
.hud-element {
  border: 1px solid rgba(0, 255, 65, 0.3);
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
}

/* Mission Timer Effect */
#mission-timer {
  text-shadow: 0 0 10px rgba(10, 132, 255, 0.8);
}

/* Tactical Button Effects */
button {
  position: relative;
  overflow: hidden;
}

button:before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

button:hover:before {
  left: 100%;
}

/* Responsive Design */
@media (max-width: 768px) {
  .tactical-grid-bg {
    background-size: 30px 30px, 30px 30px, 5px 5px, 5px 5px;
  }
  
  .tactical-scanner {
    display: none;
  }
  
  .circuit {
    display: none;
  }
}
</style>
