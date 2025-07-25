<template>
  <section id="contacto" class="bg-space-grey section">
    <div class="max-w-5xl mx-auto">
      <h2 class="section-title text-pure-white text-center mb-12 animate-on-scroll">
        ¿Lista la siguiente gran idea?
      </h2>
      
      <!-- Contact Form -->
      <form @submit.prevent="handleSubmit" class="space-y-8">
        <!-- Name Field -->
        <div class="flex flex-col">
          <label for="name" class="text-silver font-medium mb-2">Nombre</label>
          <input 
            type="text" 
            id="name" 
            v-model="form.name" 
            class="form-input"
            required
          />
        </div>

        <!-- Email Field -->
        <div class="flex flex-col">
          <label for="email" class="text-silver font-medium mb-2">Correo electrónico</label>
          <input 
            type="email" 
            id="email" 
            v-model="form.email" 
            class="form-input"
            required
          />
        </div>

        <!-- Company Field -->
        <div class="flex flex-col">
          <label for="company" class="text-silver font-medium mb-2">Empresa</label>
          <input 
            type="text" 
            id="company" 
            v-model="form.company" 
            class="form-input"
            required
          />
        </div>

        <!-- Message Field -->
        <div class="flex flex-col">
          <label for="message" class="text-silver font-medium mb-2">Mensaje</label>
          <textarea 
            id="message" 
            v-model="form.message" 
            class="form-input h-32"
            required
          />
        </div>

        <!-- Submit Button -->
        <div class="text-center">
          <button type="submit" class="btn btn-primary font-space-grotesk">Enviar mensaje</button>
        </div>
      </form>

      <!-- Success Notification -->
      <div v-if="success" class="mt-8 bg-electric-blue/10 p-4 rounded-md text-center text-electric-blue animate-fade-in-up">
        🎉 ¡Gracias por contactarnos! Te responderemos pronto.
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface Form {
  name: string;
  email: string;
  company: string;
  message: string;
}

const form = ref<Form>({
  name: '',
  email: '',
  company: '',
  message: ''
});

const success = ref(false);

const handleSubmit = () => {
  if (form.value.name && form.value.email && form.value.company && form.value.message) {
    // Simulate form submission
    setTimeout(() => {
      success.value = true;
      form.value = { name: '', email: '', company: '', message: '' };
      setTimeout(() => success.value = false, 3000);
    }, 1000);
  }
};
</script>

<style scoped>
form input:focus, form textarea:focus {
  outline: none;
}
</style>
