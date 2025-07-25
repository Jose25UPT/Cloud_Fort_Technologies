<template>
  <div class="min-h-screen bg-black text-white flex items-center justify-center">
    <div class="text-center">
      <h1 class="text-6xl font-bold mb-4">404</h1>
      <p class="text-xl mb-8">Página no encontrada</p>
      <router-link 
        to="/" 
        class="bg-blue-600 px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors"
      >
        Volver al inicio
      </router-link>
    </div>
  </div>
</template>

<script setup>
console.log('404 page loaded')
</script>
