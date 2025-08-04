<template>
  <section id="contact" class="varnox-bg-section varnox-section relative overflow-hidden">
    <!-- Decorative background elements -->
    <div class="absolute top-32 right-20 w-48 h-48 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-hero);"></div>
    <div class="absolute bottom-20 left-16 w-36 h-36 rounded-full opacity-5 varnox-floating"
         style="background: var(--varnox-gradient-section); animation-delay: 2s;"></div>
    
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <!-- Section Header with new typography -->
      <div class="text-center mb-12">
        <!-- Accent title -->
        <div class="varnox-accent-title text-sm mb-4">
          [ INICIAR PROYECTO ]
        </div>
        
        <h2 class="varnox-section-title text-4xl md:text-5xl lg:text-6xl mb-6 animate-on-scroll">
          <span class="varnox-display-title">DEPLOY</span> Your Idea
        </h2>
        
        <div class="varnox-card max-w-3xl mx-auto p-6">
          <p class="varnox-body-text text-lg leading-relaxed">
            <span class="varnox-code-text">&gt;</span> ¿Tienes una gran idea? Cuéntanos y la hacemos realidad
            <span class="text-varnox-primary animate-pulse">_</span>
          </p>
          <p class="varnox-body-text text-sm mt-3 opacity-80">
            Nuestro equipo analizará tu propuesta y te responderá en menos de 24 horas.
          </p>
        </div>
      </div>

      <!-- Enhanced Contact Form -->
      <form @submit.prevent="handleSubmit" class="space-y-8">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          <!-- Nombre completo -->
          <div class="form-field">
            <label for="name" class="varnox-accent-title text-xs mb-2 block">
              NOMBRE_COMPLETO *
            </label>
            <input 
              type="text" 
              id="name" 
              v-model="form.name" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.name }"
              @blur="validateField('name')"
              @input="clearFieldError('name')"
              required
              placeholder="Ingresa tu nombre completo"
            />
            <span v-if="errors.name" class="text-red-400 text-xs mt-1 block">{{ errors.name }}</span>
          </div>

          <!-- Email -->
          <div class="form-field">
            <label for="email" class="varnox-accent-title text-xs mb-2 block">
              EMAIL_ADDRESS *
            </label>
            <input 
              type="email" 
              id="email" 
              v-model="form.email" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.email }"
              @blur="validateField('email')"
              @input="clearFieldError('email')"
              required
              placeholder="ejemplo@correo.com"
            />
            <span v-if="errors.email" class="text-red-400 text-xs mt-1 block">{{ errors.email }}</span>
          </div>

          <!-- Teléfono -->
          <div class="form-field">
            <label for="phone" class="varnox-accent-title text-xs mb-2 block">
              PHONE_NUMBER *
            </label>
            <input 
              type="tel" 
              id="phone" 
              v-model="form.phone" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.phone }"
              @blur="validateField('phone')"
              @input="clearFieldError('phone')"
              required
              placeholder="+1 (555) 123-4567"
            />
            <span v-if="errors.phone" class="text-red-400 text-xs mt-1 block">{{ errors.phone }}</span>
          </div>

          <!-- Empresa -->
          <div class="form-field">
            <label for="company" class="varnox-accent-title text-xs mb-2 block">
              COMPANY_NAME *
            </label>
            <input 
              type="text" 
              id="company" 
              v-model="form.company" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.company }"
              @blur="validateField('company')"
              @input="clearFieldError('company')"
              required
              placeholder="Nombre de tu empresa o marca"
            />
            <span v-if="errors.company" class="text-red-400 text-xs mt-1 block">{{ errors.company }}</span>
          </div>

          <!-- Tipo de solución -->
          <div class="form-field">
            <label for="type" class="varnox-accent-title text-xs mb-2 block">
              PROJECT_TYPE *
            </label>
            <select 
              id="type" 
              v-model="form.type" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.type }"
              @blur="validateField('type')"
              @change="clearFieldError('type')"
              required
            >
              <option value="">[ SELECT_PROJECT_TYPE ]</option>
              <option value="Web Platform">Web Platform</option>
              <option value="Mobile App">Mobile App</option>
              <option value="AI/Automation">AI/Automation</option>
              <option value="Cloud Infrastructure">Cloud Infrastructure</option>
              <option value="Custom Solution">Custom Solution</option>
            </select>
            <span v-if="errors.type" class="text-red-400 text-xs mt-1 block">{{ errors.type }}</span>
          </div>

          <!-- Presupuesto -->
          <div class="form-field">
            <label for="budget" class="varnox-accent-title text-xs mb-2 block">
              BUDGET_RANGE *
            </label>
            <select 
              id="budget" 
              v-model="form.budget" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.budget }"
              @blur="validateField('budget')"
              @change="clearFieldError('budget')"
              required
            >
              <option value="">[ SELECT_BUDGET_RANGE ]</option>
              <option value="< 500 USD">< 500 USD</option>
              <option value="500-1000">500-1000 USD</option>
              <option value="1000-3000">1000-3000 USD</option>
              <option value="3000-5000">3000-5000 USD</option>
              <option value="> 5000">> 5000 USD</option>
            </select>
            <span v-if="errors.budget" class="text-red-400 text-xs mt-1 block">{{ errors.budget }}</span>
          </div>

          <!-- Referencia -->
          <div class="form-field">
            <label for="referral" class="varnox-accent-title text-xs mb-2 block">
              HOW_DID_YOU_FIND_US *
            </label>
            <select 
              id="referral" 
              v-model="form.referral" 
              class="varnox-input"
              :class="{ 'border-red-500': errors.referral }"
              @blur="validateField('referral')"
              @change="clearFieldError('referral')"
              required
            >
              <option value="">[ SELECT_SOURCE ]</option>
              <option value="Google Search">Google Search</option>
              <option value="Social Media">Social Media</option>
              <option value="Referral">Referral</option>
              <option value="Direct Contact">Direct Contact</option>
              <option value="Other">Other</option>
            </select>
            <span v-if="errors.referral" class="text-red-400 text-xs mt-1 block">{{ errors.referral }}</span>
          </div>

          <!-- Mensaje -->
          <div class="form-field md:col-span-2">
            <label for="message" class="varnox-accent-title text-xs mb-2 block">
              PROJECT_DESCRIPTION *
            </label>
            <textarea 
              id="message" 
              v-model="form.message" 
              class="varnox-textarea"
              :class="{ 'border-red-500': errors.message }"
              @blur="validateField('message')"
              @input="clearFieldError('message')"
              required
              placeholder="Describe tu proyecto con el mayor detalle posible..."
            ></textarea>
            <span v-if="errors.message" class="text-red-400 text-xs mt-1 block">{{ errors.message }}</span>
          </div>

          <!-- Archivo -->
          <div class="form-field md:col-span-2">
            <label for="file" class="varnox-accent-title text-xs mb-2 block">
              ATTACH_FILE (opcional)
            </label>
            <div class="relative">
              <input 
                type="file" 
                id="file" 
                @change="handleFileChange"
                accept=".pdf, .png, .jpg, .jpeg, .docx"
                class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
              />
              <div class="varnox-card p-4 border-2 border-dashed border-white/20 text-center cursor-pointer hover:border-varnox-primary transition-colors">
                <svg class="w-6 h-6 mx-auto mb-2 text-varnox-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                </svg>
                <div class="varnox-body-text text-sm">
                  {{ form.file ? form.file.name : 'Upload file (PDF, PNG, JPG, DOCX - Max. 5MB)' }}
                </div>
                <div class="varnox-code-text text-xs mt-1 opacity-70">
                  &gt; click_to_browse_files()
                </div>
              </div>
            </div>
            <span v-if="errors.file" class="text-red-400 text-xs mt-1 block">{{ errors.file }}</span>
          </div>
        </div>

        <!-- Enhanced Submit Button -->
        <div class="text-center">
          <button 
            type="submit" 
            :disabled="isSubmitting" 
            class="varnox-btn varnox-btn-primary text-lg px-12 py-4"
            :class="{ 'opacity-50 cursor-not-allowed': isSubmitting }"
          >
            <span v-if="!isSubmitting" class="flex items-center justify-center">
              [ DEPLOY_MESSAGE ]
              <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
              </svg>
            </span>
            <span v-else class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              PROCESSING...
            </span>
          </button>
          
          <!-- Command line indicator -->
          <div class="varnox-code-text text-xs mt-4">
            &gt; VARNOX.sendMessage(formData) // Transmitting your request
          </div>
        </div>

        <!-- Enhanced Success/Error Messages -->
        <div v-if="showSuccessMessage" class="varnox-card p-6 border border-green-500/30" style="background: rgba(34, 197, 94, 0.1);">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="varnox-section-title text-green-400 text-lg mb-1">[ MESSAGE_SENT ]</h4>
              <p class="varnox-body-text text-sm opacity-90">Gracias por tu interés. Te responderemos en menos de 24 horas.</p>
              <div class="varnox-code-text text-xs mt-2 text-green-400">
                &gt; success: message_transmitted_successfully()
              </div>
            </div>
          </div>
        </div>
        
        <div v-if="showErrorMessage" class="varnox-card p-6 border border-red-500/30" style="background: rgba(239, 68, 68, 0.1);">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="varnox-section-title text-red-400 text-lg mb-1">[ TRANSMISSION_ERROR ]</h4>
              <p class="varnox-body-text text-sm opacity-90">{{ errorMessage }}</p>
              <div class="varnox-code-text text-xs mt-2 text-red-400">
                &gt; error: failed_to_transmit_message()
              </div>
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
/* Form Animations */
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

/* Select Arrow */
select.varnox-input {
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%236366F1' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6,9 12,15 18,9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
  padding-right: 40px;
}

/* Enhanced focus states */
.varnox-input:focus,
.varnox-textarea:focus {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2);
}

/* Error states */
.border-red-500 {
  border-color: #ef4444 !important;
}

.border-red-500:focus {
  border-color: #ef4444 !important;
  box-shadow: 0 0 0 1px #ef4444 !important;
}
</style>

