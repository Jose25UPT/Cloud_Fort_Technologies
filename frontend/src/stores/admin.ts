import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

// Types
export interface Hero {
  id: string
  titulo: string
  subtitulo?: string
  cta_texto?: string
  cta_url?: string
  imagen_url?: string
  updated_at: string
}

export interface Service {
  id: string
  titulo: string
  descripcion: string
  icono?: string
}

export interface Project {
  id: string
  nombre: string
  descripcion: string
  imagen_url?: string
  tags?: string[]
  link?: string
  fecha?: string
}

export interface Testimonial {
  id: string
  nombre_cliente: string
  cargo?: string
  opinion: string
  imagen_url?: string
}

export interface Company {
  id: string
  telefono?: string
  email_contacto?: string
  redes_sociales?: Record<string, string>
}

export interface ContactRequest {
  id: string
  nombre: string
  correo: string
  empresa?: string
  mensaje: string
  timestamp: string
  pdf_path?: string
}

const API_BASE_URL = 'http://localhost:8000/api'

export const useAdminStore = defineStore('admin', () => {
  // State
  const hero = ref<Hero | null>(null)
  const services = ref<Service[]>([])
  const projects = ref<Project[]>([])
  const testimonials = ref<Testimonial[]>([])
  const company = ref<Company | null>(null)
  const contactRequests = ref<ContactRequest[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Helper function for API calls
  const handleApiCall = async <T>(apiCall: () => Promise<T>): Promise<T | null> => {
    try {
      loading.value = true
      error.value = null
      return await apiCall()
    } catch (err: any) {
      console.error('API Error:', err)
      error.value = err.response?.data?.detail || 'Error en la operación'
      return null
    } finally {
      loading.value = false
    }
  }

  // Hero Actions
  const fetchHero = async () => {
    const result = await handleApiCall(async () => {
      const response = await axios.get(`${API_BASE_URL}/admin/hero`)
      return response.data
    })
    if (result) {
      hero.value = result
    }
  }

  const updateHero = async (heroData: Partial<Hero>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.put(`${API_BASE_URL}/admin/hero`, heroData)
      return response.data
    })
    if (result) {
      hero.value = result
      return result
    }
    return null
  }

  // Services Actions
  const fetchServices = async () => {
    const result = await handleApiCall(async () => {
      const response = await axios.get(`${API_BASE_URL}/admin/services`)
      return response.data
    })
    if (result) {
      services.value = result
    }
  }

  const createService = async (serviceData: Omit<Service, 'id'>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.post(`${API_BASE_URL}/admin/services`, serviceData)
      return response.data
    })
    if (result) {
      services.value.push(result)
      return result
    }
    return null
  }

  const updateService = async (id: string, serviceData: Partial<Service>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.put(`${API_BASE_URL}/admin/services/${id}`, serviceData)
      return response.data
    })
    if (result) {
      const index = services.value.findIndex(s => s.id === id)
      if (index !== -1) {
        services.value[index] = result
      }
      return result
    }
    return null
  }

  const deleteService = async (id: string) => {
    const result = await handleApiCall(async () => {
      await axios.delete(`${API_BASE_URL}/admin/services/${id}`)
      return true
    })
    if (result) {
      services.value = services.value.filter(s => s.id !== id)
      return true
    }
    return false
  }

  // Projects Actions
  const fetchProjects = async () => {
    const result = await handleApiCall(async () => {
      const response = await axios.get(`${API_BASE_URL}/admin/projects`)
      return response.data
    })
    if (result) {
      projects.value = result
    }
  }

  const createProject = async (projectData: Omit<Project, 'id'>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.post(`${API_BASE_URL}/admin/projects`, projectData)
      return response.data
    })
    if (result) {
      projects.value.push(result)
      return result
    }
    return null
  }

  const updateProject = async (id: string, projectData: Partial<Project>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.put(`${API_BASE_URL}/admin/projects/${id}`, projectData)
      return response.data
    })
    if (result) {
      const index = projects.value.findIndex(p => p.id === id)
      if (index !== -1) {
        projects.value[index] = result
      }
      return result
    }
    return null
  }

  const deleteProject = async (id: string) => {
    const result = await handleApiCall(async () => {
      await axios.delete(`${API_BASE_URL}/admin/projects/${id}`)
      return true
    })
    if (result) {
      projects.value = projects.value.filter(p => p.id !== id)
      return true
    }
    return false
  }

  // Testimonials Actions
  const fetchTestimonials = async () => {
    const result = await handleApiCall(async () => {
      const response = await axios.get(`${API_BASE_URL}/admin/testimonials`)
      return response.data
    })
    if (result) {
      testimonials.value = result
    }
  }

  const createTestimonial = async (testimonialData: Omit<Testimonial, 'id'>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.post(`${API_BASE_URL}/admin/testimonials`, testimonialData)
      return response.data
    })
    if (result) {
      testimonials.value.push(result)
      return result
    }
    return null
  }

  const updateTestimonial = async (id: string, testimonialData: Partial<Testimonial>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.put(`${API_BASE_URL}/admin/testimonials/${id}`, testimonialData)
      return response.data
    })
    if (result) {
      const index = testimonials.value.findIndex(t => t.id === id)
      if (index !== -1) {
        testimonials.value[index] = result
      }
      return result
    }
    return null
  }

  const deleteTestimonial = async (id: string) => {
    const result = await handleApiCall(async () => {
      await axios.delete(`${API_BASE_URL}/admin/testimonials/${id}`)
      return true
    })
    if (result) {
      testimonials.value = testimonials.value.filter(t => t.id !== id)
      return true
    }
    return false
  }

  // Company Actions
  const fetchCompany = async () => {
    const result = await handleApiCall(async () => {
      const response = await axios.get(`${API_BASE_URL}/admin/company`)
      return response.data
    })
    if (result) {
      company.value = result
    }
  }

  const updateCompany = async (companyData: Partial<Company>) => {
    const result = await handleApiCall(async () => {
      const response = await axios.put(`${API_BASE_URL}/admin/company`, companyData)
      return response.data
    })
    if (result) {
      company.value = result
      return result
    }
    return null
  }

  // Contact Requests Actions
  const fetchContactRequests = async () => {
    const result = await handleApiCall(async () => {
      const response = await axios.get(`${API_BASE_URL}/admin/requests`)
      return response.data
    })
    if (result) {
      contactRequests.value = result
    }
  }

  // Clear error
  const clearError = () => {
    error.value = null
  }

  return {
    // State
    hero,
    services,
    projects,
    testimonials,
    company,
    contactRequests,
    loading,
    error,

    // Actions
    fetchHero,
    updateHero,
    fetchServices,
    createService,
    updateService,
    deleteService,
    fetchProjects,
    createProject,
    updateProject,
    deleteProject,
    fetchTestimonials,
    createTestimonial,
    updateTestimonial,
    deleteTestimonial,
    fetchCompany,
    updateCompany,
    fetchContactRequests,
    clearError
  }
})
