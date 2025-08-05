<template>
  <section id="contacto" class="bg-gradient-to-br from-gray-50 via-white to-indigo-50/30 py-20 lg:py-32 relative overflow-hidden hexagonal-grid-pattern">
    <!-- Decorative elements con paleta moderna -->
    <div class="absolute top-10 right-10 w-32 h-32 rounded-full opacity-20 bg-gradient-to-br from-indigo-600 to-purple-600"></div>
    <div class="absolute bottom-10 left-10 w-24 h-24 rounded-full opacity-15 bg-gradient-to-br from-purple-600 to-amber-500"></div>
    <div class="absolute top-1/2 right-1/4 w-16 h-16 rounded-full opacity-10 bg-gradient-to-br from-amber-500 to-indigo-600"></div>
    
    <div class="max-w-6xl mx-auto px-6 lg:px-8 relative z-10">
      <!-- Modern Section Header -->
      <div class="text-center mb-16">
        <!-- Modern Accent Title -->
        <div class="text-indigo-600 font-rajdhani text-sm mb-4 tracking-wider uppercase font-semibold">
          Contacto
        </div>
        
        <h2 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-8 text-gray-900 font-orbitron">
          <span class="bg-gradient-to-r from-indigo-600 via-purple-600 to-amber-500 bg-clip-text text-transparent">Hablemos</span> de tu proyecto
        </h2>
        
        <div class="bg-white p-8 relative overflow-hidden rounded-2xl border border-gray-200 shadow-xl max-w-4xl mx-auto">
          <p class="text-gray-700 text-lg leading-relaxed font-source-sans mb-4">
            ¿Tienes una gran idea? Cuéntanos y la haremos realidad con la mejor tecnología.
          </p>
          <p class="text-gray-600 text-base font-source-sans">
            Nuestro equipo analizará tu propuesta y te responderá en menos de 24 horas.
          </p>
          
          <!-- Decorative Elements -->
          <div class="absolute top-4 right-4 w-3 h-3 rounded-full bg-indigo-600 opacity-30"></div>
          <div class="absolute bottom-4 left-4 w-2 h-2 rounded-full bg-amber-500 opacity-40"></div>
        </div>
      </div>

      <!-- Modern Contact Form -->
      <form @submit.prevent="handleSubmit" class="bg-white rounded-2xl border border-gray-200 shadow-xl p-8 max-w-4xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          
          <!-- Nombre completo -->
          <div class="space-y-2">
            <label for="name" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Nombre completo *
            </label>
            <input 
              type="text" 
              id="name" 
              v-model="form.name" 
              class="modern-input"
              :class="{ 'border-red-500': errors.name }"
              @blur="validateField('name')"
              @input="clearFieldError('name')"
              required
              placeholder="Ingresa tu nombre completo"
            />
            <span v-if="errors.name" class="text-red-500 text-xs">{{ errors.name }}</span>
          </div>

          <!-- Correo electrónico -->
          <div class="space-y-2">
            <label for="email" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Correo electrónico *
            </label>
            <input 
              type="email" 
              id="email" 
              v-model="form.email" 
              class="modern-input"
              :class="{ 'border-red-500': errors.email }"
              @blur="validateField('email')"
              @input="clearFieldError('email')"
              required
              placeholder="tu-correo@ejemplo.com"
            />
            <span v-if="errors.email" class="text-red-500 text-xs">{{ errors.email }}</span>
          </div>

          <!-- Teléfono -->
          <div class="space-y-2">
            <label for="phone" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Teléfono *
            </label>
            <input 
              type="tel" 
              id="phone" 
              v-model="form.phone" 
              class="modern-input"
              :class="{ 'border-red-500': errors.phone }"
              @blur="validateField('phone')"
              @input="clearFieldError('phone')"
              required
              placeholder="+57 (300) 123-4567"
            />
            <span v-if="errors.phone" class="text-red-500 text-xs">{{ errors.phone }}</span>
          </div>

          <!-- Empresa -->
          <div class="space-y-2">
            <label for="company" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Empresa o proyecto *
            </label>
            <input 
              type="text" 
              id="company" 
              v-model="form.company" 
              class="modern-input"
              :class="{ 'border-red-500': errors.company }"
              @blur="validateField('company')"
              @input="clearFieldError('company')"
              required
              placeholder="Nombre de tu empresa o proyecto"
            />
            <span v-if="errors.company" class="text-red-500 text-xs">{{ errors.company }}</span>
          </div>

          <!-- Tipo de proyecto -->
          <div class="space-y-2">
            <label for="type" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Tipo de proyecto *
            </label>
            <select 
              id="type" 
              v-model="form.type" 
              class="modern-input"
              :class="{ 'border-red-500': errors.type }"
              @blur="validateField('type')"
              @change="clearFieldError('type')"
              required
            >
              <option value="">Selecciona el tipo de proyecto</option>
              <option value="Desarrollo Web">Desarrollo Web</option>
              <option value="Aplicación Móvil">Aplicación Móvil</option>
              <option value="Inteligencia Artificial">Inteligencia Artificial</option>
              <option value="Infraestructura en la Nube">Infraestructura en la Nube</option>
              <option value="Solución Personalizada">Solución Personalizada</option>
            </select>
            <span v-if="errors.type" class="text-red-500 text-xs">{{ errors.type }}</span>
          </div>

          <!-- Presupuesto -->
          <div class="space-y-2">
            <label for="budget" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Presupuesto estimado *
            </label>
            <select 
              id="budget" 
              v-model="form.budget" 
              class="modern-input"
              :class="{ 'border-red-500': errors.budget }"
              @blur="validateField('budget')"
              @change="clearFieldError('budget')"
              required
            >
              <option value="">Selecciona tu rango de presupuesto</option>
              <option value="< 500 USD">Menos de $500 USD</option>
              <option value="500-1000">$500 - $1,000 USD</option>
              <option value="1000-3000">$1,000 - $3,000 USD</option>
              <option value="3000-5000">$3,000 - $5,000 USD</option>
              <option value="> 5000">Más de $5,000 USD</option>
            </select>
            <span v-if="errors.budget" class="text-red-500 text-xs">{{ errors.budget }}</span>
          </div>

          <!-- Referencia -->
          <div class="space-y-2 md:col-span-2">
            <label for="referral" class="text-gray-700 font-semibold text-sm block font-source-sans">
              ¿Cómo nos conociste? *
            </label>
            <select 
              id="referral" 
              v-model="form.referral" 
              class="modern-input"
              :class="{ 'border-red-500': errors.referral }"
              @blur="validateField('referral')"
              @change="clearFieldError('referral')"
              required
            >
              <option value="">Selecciona una opción</option>
              <option value="Búsqueda Google">Búsqueda en Google</option>
              <option value="Redes Sociales">Redes Sociales</option>
              <option value="Recomendación">Recomendación</option>
              <option value="Contacto Directo">Contacto Directo</option>
              <option value="Otro">Otro</option>
            </select>
            <span v-if="errors.referral" class="text-red-500 text-xs">{{ errors.referral }}</span>
          </div>

          <!-- Mensaje -->
          <div class="space-y-2 md:col-span-2">
            <label for="message" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Descripción del proyecto *
            </label>
            <textarea 
              id="message" 
              v-model="form.message" 
              class="modern-textarea"
              :class="{ 'border-red-500': errors.message }"
              @blur="validateField('message')"
              @input="clearFieldError('message')"
              required
              placeholder="Describe tu proyecto con el mayor detalle posible..."
            ></textarea>
            <span v-if="errors.message" class="text-red-500 text-xs">{{ errors.message }}</span>
          </div>

          <!-- Archivo -->
          <div class="space-y-2 md:col-span-2">
            <label for="file" class="text-gray-700 font-semibold text-sm block font-source-sans">
              Archivo adjunto (opcional)
            </label>
            <div class="relative">
              <input 
                type="file" 
                id="file" 
                @change="handleFileChange"
                accept=".pdf, .png, .jpg, .jpeg, .docx"
                class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
              />
              <div class="modern-file-upload border-2 border-dashed border-gray-300 text-center cursor-pointer hover:border-indigo-500 transition-colors rounded-lg p-6">
                <svg class="w-6 h-6 mx-auto mb-2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                </svg>
                <div class="text-gray-700 text-sm font-medium">
                  {{ form.file ? form.file.name : 'Arrastra un archivo aquí o haz clic para seleccionar' }}
                </div>
                <div class="text-gray-500 text-xs mt-1">
                  PDF, PNG, JPG, DOCX - Máximo 5MB
                </div>
              </div>
            </div>
            <span v-if="errors.file" class="text-red-500 text-xs">{{ errors.file }}</span>
          </div>
        </div>

        <!-- Modern Submit Button -->
        <div class="text-center mt-8">
          <button 
            type="submit" 
            :disabled="isSubmitting" 
            class="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white font-semibold py-4 px-12 rounded-xl text-lg transform transition-all duration-300 hover:scale-105 shadow-xl hover:shadow-2xl font-poppins"
            :class="{ 'opacity-50 cursor-not-allowed': isSubmitting }"
          >
            <span v-if="!isSubmitting" class="flex items-center justify-center">
              Enviar proyecto
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
          
          <p class="text-gray-600 text-sm mt-4 font-source-sans">
            Nos pondremos en contacto contigo en menos de 24 horas
          </p>
        </div>

        <!-- Modern Success/Error Messages -->
        <div v-if="showSuccessMessage" class="bg-green-50 border border-green-200 rounded-xl p-6 mt-8">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="text-green-800 font-semibold text-lg mb-1">¡Mensaje enviado con éxito!</h4>
              <p class="text-green-700 text-sm">Gracias por tu interés. Te responderemos en menos de 24 horas.</p>
            </div>
          </div>
        </div>
        
        <div v-if="showErrorMessage" class="bg-red-50 border border-red-200 rounded-xl p-6 mt-8">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="text-red-800 font-semibold text-lg mb-1">Error al enviar el mensaje</h4>
              <p class="text-red-700 text-sm">{{ errorMessage }}</p>
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
/* Hexagonal Grid Pattern - Malla 3D Tecnológica */
.hexagonal-grid-pattern {
  background-image: 
    /* Rejilla hexagonal principal con colores purple e indigo más brillantes */
    radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.45) 2px, transparent 2px),
    radial-gradient(circle at 25% 25%, rgba(99, 102, 241, 0.42) 1.5px, transparent 1.5px),
    radial-gradient(circle at 75% 75%, rgba(255, 255, 255, 0.38) 1px, transparent 1px),
    /* Líneas de conexión hexagonal con purple/indigo más nítidas */
    linear-gradient(30deg, rgba(139, 92, 246, 0.35) 1px, transparent 1px),
    linear-gradient(-30deg, rgba(99, 102, 241, 0.35) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.32) 1px, transparent 1px),
    /* Efecto 3D con sombras purple/indigo más intensas */
    linear-gradient(120deg, rgba(139, 92, 246, 0.28) 2px, transparent 2px),
    linear-gradient(-120deg, rgba(99, 102, 241, 0.28) 2px, transparent 2px),
    /* Puntos de intersección tecnológicos con white/purple más brillantes */
    radial-gradient(circle at 100% 100%, rgba(255, 255, 255, 0.4) 1px, transparent 1px),
    radial-gradient(circle at 0% 0%, rgba(139, 92, 246, 0.32) 1px, transparent 1px);
  background-size: 
    45px 45px,
    30px 30px, 
    60px 60px,
    80px 46px,
    80px 46px,
    120px 120px,
    100px 58px,
    100px 58px,
    90px 90px,
    75px 75px;
  background-position: 
    0 0,
    15px 15px,
    30px 30px,
    0 0,
    40px 23px,
    0 0,
    20px 12px,
    60px 35px,
    45px 45px,
    -15px -15px;
  animation: hexagonal-tech-drift 30s linear infinite;
}

@keyframes hexagonal-tech-drift {
  0% { 
    transform: translateX(0) translateY(0) rotate(0deg) scale(1); 
    opacity: 0.85;
  }
  25% { 
    transform: translateX(-8px) translateY(-4px) rotate(0.3deg) scale(1.02); 
    opacity: 0.75;
  }
  50% { 
    transform: translateX(4px) translateY(-8px) rotate(0deg) scale(1); 
    opacity: 0.85;
  }
  75% { 
    transform: translateX(-4px) translateY(4px) rotate(-0.3deg) scale(0.98); 
    opacity: 0.8;
  }
  100% { 
    transform: translateX(0) translateY(0) rotate(0deg) scale(1); 
    opacity: 0.85;
  }
}

/* Font classes */
.font-orbitron {
  font-family: 'Orbitron', monospace;
}

.font-poppins {
  font-family: 'Poppins', sans-serif;
}

.font-source-sans {
  font-family: 'Source Sans Pro', sans-serif;
}

.font-rajdhani {
  font-family: 'Rajdhani', sans-serif;
}

/* Modern Input Styles */
.modern-input,
.modern-textarea {
  width: 100%;
  padding: 12px 16px;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  color: #374151;
  font-family: 'Source Sans Pro', sans-serif;
  transition: all 0.3s ease;
  font-size: 14px;
}

.modern-input:focus,
.modern-textarea:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.modern-input::placeholder,
.modern-textarea::placeholder {
  color: #9ca3af;
}

.modern-textarea {
  min-height: 120px;
  resize: vertical;
}

.modern-file-upload {
  background: #f9fafb;
  transition: all 0.3s ease;
}

.modern-file-upload:hover {
  background: #f3f4f6;
}

/* Animations */
@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .modern-input,
  .modern-textarea {
    padding: 10px 12px;
    font-size: 13px;
  }
}
</style>


