<template>
  <section id="contact" class="bg-space-grey section">
    <div class="max-w-5xl mx-auto">
      <h2 class="section-title text-pure-white text-center mb-4 animate-on-scroll font-urbanist">
        ¿Tienes una gran idea? Cuéntanos y la hacemos realidad
      </h2>
      <p class="section-subtitle text-center mb-12 animate-on-scroll text-silver">
        Nuestro equipo analizará tu propuesta y te responderá en menos de 24 horas.
      </p>

      <!-- Contact Form -->
      <form @submit.prevent="handleSubmit" class="space-y-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <!-- Nombre completo -->
          <div class="form-field">
            <label for="name" class="form-label">Nombre Completo *</label>
            <input 
              type="text" 
              id="name" 
              v-model="form.name" 
              :class="['contact-input', { 'input-error': errors.name }]"
              @blur="validateField('name')"
              @input="clearFieldError('name')"
              required
              placeholder="Ingresa tu nombre completo"
            />
            <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
          </div>

          <!-- Email -->
          <div class="form-field">
            <label for="email" class="form-label">Correo Electrónico *</label>
            <input 
              type="email" 
              id="email" 
              v-model="form.email" 
              :class="['contact-input', { 'input-error': errors.email }]"
              @blur="validateField('email')"
              @input="clearFieldError('email')"
              required
              placeholder="ejemplo@correo.com"
            />
            <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
          </div>

          <!-- Teléfono -->
          <div class="form-field">
            <label for="phone" class="form-label">Teléfono *</label>
            <input 
              type="tel" 
              id="phone" 
              v-model="form.phone" 
              :class="['contact-input', { 'input-error': errors.phone }]"
              @blur="validateField('phone')"
              @input="clearFieldError('phone')"
              required
              placeholder="+1 (555) 123-4567"
            />
            <span v-if="errors.phone" class="error-message">{{ errors.phone }}</span>
          </div>

          <!-- Empresa -->
          <div class="form-field">
            <label for="company" class="form-label">Empresa / Marca *</label>
            <input 
              type="text" 
              id="company" 
              v-model="form.company" 
              :class="['contact-input', { 'input-error': errors.company }]"
              @blur="validateField('company')"
              @input="clearFieldError('company')"
              required
              placeholder="Nombre de tu empresa o marca"
            />
            <span v-if="errors.company" class="error-message">{{ errors.company }}</span>
          </div>

          <!-- Tipo de solución -->
          <div class="form-field">
            <label for="type" class="form-label">¿Qué tipo de solución busca? *</label>
            <select 
              id="type" 
              v-model="form.type" 
              :class="['contact-input', { 'input-error': errors.type }]"
              @blur="validateField('type')"
              @change="clearFieldError('type')"
              required
            >
              <option value="">Selecciona una opción</option>
              <option value="Sitio Web">Sitio Web</option>
              <option value="App Móvil">App Móvil</option>
              <option value="Bots o IA">Bots o IA</option>
              <option value="Automatización">Automatización</option>
              <option value="Otro">Otro</option>
            </select>
            <span v-if="errors.type" class="error-message">{{ errors.type }}</span>
          </div>

          <!-- Presupuesto -->
          <div class="form-field">
            <label for="budget" class="form-label">Presupuesto Estimado *</label>
            <select 
              id="budget" 
              v-model="form.budget" 
              :class="['contact-input', { 'input-error': errors.budget }]"
              @blur="validateField('budget')"
              @change="clearFieldError('budget')"
              required
            >
              <option value="">Selecciona un rango</option>
              <option value="< 500 USD">< 500 USD</option>
              <option value="500-1000">500-1000 USD</option>
              <option value="1000-3000">1000-3000 USD</option>
              <option value="> 3000">> 3000 USD</option>
            </select>
            <span v-if="errors.budget" class="error-message">{{ errors.budget }}</span>
          </div>

          <!-- Referencia -->
          <div class="form-field">
            <label for="referral" class="form-label">¿Cómo nos encontraste? *</label>
            <select 
              id="referral" 
              v-model="form.referral" 
              :class="['contact-input', { 'input-error': errors.referral }]"
              @blur="validateField('referral')"
              @change="clearFieldError('referral')"
              required
            >
              <option value="">Selecciona una opción</option>
              <option value="Google">Google</option>
              <option value="Instagram">Instagram</option>
              <option value="Referido">Referido</option>
              <option value="Otro">Otro</option>
            </select>
            <span v-if="errors.referral" class="error-message">{{ errors.referral }}</span>
          </div>

          <!-- Mensaje -->
          <div class="form-field md:col-span-2">
            <label for="message" class="form-label">Mensaje Detallado *</label>
            <textarea 
              id="message" 
              v-model="form.message" 
              :class="['contact-input', 'h-32', { 'input-error': errors.message }]"
              @blur="validateField('message')"
              @input="clearFieldError('message')"
              required
              placeholder="Describe tu proyecto con el mayor detalle posible..."
            ></textarea>
            <span v-if="errors.message" class="error-message">{{ errors.message }}</span>
          </div>

          <!-- Archivo -->
          <div class="form-field md:col-span-2">
            <label for="file" class="form-label">Adjuntar archivo (opcional)</label>
            <div class="file-input-wrapper">
              <input 
                type="file" 
                id="file" 
                @change="handleFileChange"
                accept=".pdf, .png, .jpg, .jpeg, .docx"
                class="file-input"
              />
              <label for="file" class="file-input-label">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                </svg>
                {{ form.file ? form.file.name : 'Seleccionar archivo (PDF, PNG, JPG, DOCX - Max. 5MB)' }}
              </label>
            </div>
            <span v-if="errors.file" class="error-message">{{ errors.file }}</span>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="text-center">
          <button 
            type="submit" 
            :disabled="isSubmitting" 
            :class="['submit-button', { 'submitting': isSubmitting }]"
          >
            <span v-if="!isSubmitting" class="flex items-center justify-center">
              Enviar mensaje
              <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
              </svg>
            </span>
            <span v-else class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Enviando...
            </span>
          </button>
        </div>

        <!-- Success/Error Messages -->
        <div v-if="showSuccessMessage" class="success-message animate-fade-in-up">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="font-medium">¡Mensaje enviado con éxito!</h4>
              <p class="text-sm opacity-90">Gracias por tu interés. Te responderemos en menos de 24 horas.</p>
            </div>
          </div>
        </div>
        
        <div v-if="showErrorMessage" class="error-message-box animate-fade-in-up">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="font-medium">Error al enviar el mensaje</h4>
              <p class="text-sm opacity-90">{{ errorMessage }}</p>
            </div>
          </div>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { contactService, ContactFormData } from '../services/contact';

interface Form extends Omit<ContactFormData, 'file'> {
  file: any;
}

const form = ref<Form>({
  name: '',
  email: '',
  phone: '',
  company: '',
  type: '',
  budget: '',
  referral: '',
  message: '',
  file: null
});

const errors = reactive<Partial<Record<keyof Form, string>>>({
  name: '',
  email: '',
  phone: '',
  company: '',
  type: '',
  budget: '',
  referral: '',
  message: '',
  file: ''
});

const isSubmitting = ref(false);
const showSuccessMessage = ref(false);
const showErrorMessage = ref(false);
const errorMessage = ref('');

// Validation functions
const validateField = (fieldName: keyof Form) => {
  const value = form.value[fieldName];
  
  switch (fieldName) {
    case 'name':
      if (!value || (typeof value === 'string' && value.trim().length < 2)) {
        errors.name = 'El nombre debe tener al menos 2 caracteres';
      } else {
        errors.name = '';
      }
      break;
    
    case 'email':
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!value || !emailRegex.test(value as string)) {
        errors.email = 'Ingresa un correo electrónico válido';
      } else {
        errors.email = '';
      }
      break;
    
    case 'phone':
      const phoneRegex = /^[\+]?[(]?[\d\s\-\(\)]+$/;
      if (!value || !phoneRegex.test(value as string) || (value as string).length < 8) {
        errors.phone = 'Ingresa un número de teléfono válido';
      } else {
        errors.phone = '';
      }
      break;
    
    case 'company':
      if (!value || (typeof value === 'string' && value.trim().length < 2)) {
        errors.company = 'El nombre de la empresa es requerido';
      } else {
        errors.company = '';
      }
      break;
    
    case 'type':
    case 'budget':
    case 'referral':
      if (!value) {
        errors[fieldName] = 'Este campo es requerido';
      } else {
        errors[fieldName] = '';
      }
      break;
    
    case 'message':
      if (!value || (typeof value === 'string' && value.trim().length < 10)) {
        errors.message = 'El mensaje debe tener al menos 10 caracteres';
      } else {
        errors.message = '';
      }
      break;
  }
};

const clearFieldError = (fieldName: keyof Form) => {
  errors[fieldName] = '';
};

const validateForm = (): boolean => {
  let isValid = true;
  
  Object.keys(form.value).forEach(key => {
    if (key !== 'file') {
      validateField(key as keyof Form);
      if (errors[key as keyof Form]) {
        isValid = false;
      }
    }
  });
  
  return isValid;
};

const handleSubmit = async () => {
  if (!validateForm()) {
    return;
  }
  
  isSubmitting.value = true;
  showSuccessMessage.value = false;
  showErrorMessage.value = false;
  
  try {
    const { success: isSent, message } = await contactService.submitContactForm(form.value);
    
    if (isSent) {
      showSuccessMessage.value = true;
      form.value = {
        name: '',
        email: '',
        phone: '',
        company: '',
        type: '',
        budget: '',
        referral: '',
        message: '',
        file: null
      };
      
      // Hide success message after 5 seconds
      setTimeout(() => {
        showSuccessMessage.value = false;
      }, 5000);
    } else {
      showErrorMessage.value = true;
      errorMessage.value = message;
      
      // Hide error message after 5 seconds
      setTimeout(() => {
        showErrorMessage.value = false;
      }, 5000);
    }
  } catch (error) {
    showErrorMessage.value = true;
    errorMessage.value = 'Error inesperado. Por favor intenta de nuevo.';
    
    setTimeout(() => {
      showErrorMessage.value = false;
    }, 5000);
  } finally {
    isSubmitting.value = false;
  }
};

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  
  if (target.files && target.files.length) {
    const file = target.files[0];
    const allowedTypes = ['application/pdf', 'image/png', 'image/jpeg', 'image/jpg', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
    
    if (!allowedTypes.includes(file.type)) {
      errors.file = 'Tipo de archivo no permitido. Solo PDF, PNG, JPG o DOCX.';
      target.value = '';
      return;
    }
    
    if (file.size > 5 * 1024 * 1024) { // 5MB limit
      errors.file = 'El archivo es demasiado grande. Tamaño máximo: 5MB.';
      target.value = '';
      return;
    }
    
    form.value.file = file;
    errors.file = '';
  }
};
</script>

<style scoped>
/* Form Styles */
.form-field {
  @apply flex flex-col space-y-2;
}

.form-label {
  @apply block text-silver font-medium font-inter;
}

.contact-input {
  @apply w-full bg-graphite border border-graphite/50 rounded-lg px-4 py-3 text-pure-white placeholder-silver/70 font-inter transition-all duration-300 focus:border-electric-blue focus:ring-1 focus:ring-electric-blue;
}

.contact-input:focus {
  outline: none;
  box-shadow: 0 0 0 1px #0A84FF;
}

.input-error {
  @apply border-red-500 focus:border-red-500 focus:ring-red-500;
}

.error-message {
  @apply text-red-400 text-sm font-inter;
}

/* File Input Styles */
.file-input-wrapper {
  @apply relative;
}

.file-input {
  @apply absolute inset-0 w-full h-full opacity-0 cursor-pointer;
}

.file-input-label {
  @apply flex items-center justify-center w-full p-4 border-2 border-dashed border-graphite rounded-lg cursor-pointer transition-all duration-300 hover:border-electric-blue bg-graphite/20 text-silver font-inter;
}

.file-input-label:hover {
  @apply border-electric-blue text-electric-blue bg-electric-blue/5;
}

/* Submit Button */
.submit-button {
  @apply bg-electric-blue hover:bg-electric-blue/90 text-pure-white font-medium py-4 px-8 rounded-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg hover:shadow-electric-blue/25 font-space-grotesk disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none disabled:shadow-none;
}

.submit-button.submitting {
  @apply bg-electric-blue/70 cursor-not-allowed;
}

/* Message Boxes */
.success-message {
  @apply mt-8 bg-green-500/10 border border-green-500/20 p-6 rounded-lg text-green-400;
}

.error-message-box {
  @apply mt-8 bg-red-500/10 border border-red-500/20 p-6 rounded-lg text-red-400;
}

/* Select Styling */
select.contact-input {
  @apply appearance-none bg-no-repeat;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23D1D1D6' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6,9 12,15 18,9'%3e%3c/polyline%3e%3c/svg%3e");
  background-position: right 12px center;
  background-size: 16px;
  padding-right: 40px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .form-field {
    @apply space-y-3;
  }
  
  .contact-input {
    @apply text-base;
  }
  
  .submit-button {
    @apply w-full py-4;
  }
}

/* Animation for form fields */
.form-field {
  animation: slideInUp 0.6s ease-out;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Stagger animation for form fields */
.form-field:nth-child(1) { animation-delay: 0.1s; }
.form-field:nth-child(2) { animation-delay: 0.2s; }
.form-field:nth-child(3) { animation-delay: 0.3s; }
.form-field:nth-child(4) { animation-delay: 0.4s; }
.form-field:nth-child(5) { animation-delay: 0.5s; }
.form-field:nth-child(6) { animation-delay: 0.6s; }
.form-field:nth-child(7) { animation-delay: 0.7s; }
.form-field:nth-child(8) { animation-delay: 0.8s; }
.form-field:nth-child(9) { animation-delay: 0.9s; }
</style>

