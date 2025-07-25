import axios from 'axios'

export interface ContactFormData {
  name: string
  email: string
  phone: string
  company: string
  type: string
  budget: string
  referral: string
  message: string
  file?: File
}

export interface ContactResponse {
  success: boolean
  message: string
}

class ContactService {
  private readonly baseURL = 'http://localhost:8000'

  async submitContactForm(data: ContactFormData): Promise<ContactResponse> {
    try {
      // Crear FormData para enviar archivos y datos juntos
      const formData = new FormData()
      
      // Agregar todos los campos del formulario
      formData.append('name', data.name)
      formData.append('email', data.email)
      formData.append('phone', data.phone)
      formData.append('company', data.company)
      formData.append('type', data.type)
      formData.append('budget', data.budget)
      formData.append('referral', data.referral)
      formData.append('message', data.message)
      
      // Agregar archivo si existe
      if (data.file) {
        formData.append('file', data.file)
      }

      const response = await axios.post(`${this.baseURL}/api/public/contact/submit`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

      return {
        success: true,
        message: response.data.message || 'Mensaje enviado exitosamente'
      }
    } catch (error) {
      console.error('Error al enviar formulario de contacto:', error)
      
      if (axios.isAxiosError(error)) {
        return {
          success: false,
          message: error.response?.data?.message || 'Error al enviar el mensaje. Por favor intenta de nuevo.'
        }
      }
      
      return {
        success: false,
        message: 'Error inesperado. Por favor intenta de nuevo más tarde.'
      }
    }
  }
}

export const contactService = new ContactService()
