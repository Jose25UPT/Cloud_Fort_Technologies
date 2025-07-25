import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export interface LoginCredentials {
  email: string
  password: string
}

export interface AuthUser {
  email: string
  is_active: boolean
  is_admin: boolean
}

export interface LoginResponse {
  access_token: string
  token_type: string
  expires_in: number
}

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(localStorage.getItem('auth_token'))
  const user = ref<AuthUser | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Computed
  const isAuthenticated = computed(() => !!token.value)
  const isAdmin = computed(() => user.value?.is_admin ?? false)

  // Configure axios interceptor
  if (token.value) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
  }

  // API Base URL
  const API_BASE_URL = 'http://localhost:8000'

  // Actions
  async function login(credentials: LoginCredentials): Promise<boolean> {
    try {
      loading.value = true
      error.value = null

      const response = await axios.post<LoginResponse>(
        `${API_BASE_URL}/api/auth/login`,
        credentials
      )

      const data = response.data
      token.value = data.access_token
      
      // Store token in localStorage
      localStorage.setItem('auth_token', data.access_token)
      
      // Set axios default header
      axios.defaults.headers.common['Authorization'] = `Bearer ${data.access_token}`
      
      // Set user data (for admin, we can set basic info)
      user.value = {
        email: credentials.email,
        is_active: true,
        is_admin: true
      }

      return true
    } catch (err: any) {
      console.error('Login error:', err)
      error.value = err.response?.data?.detail || 'Error de autenticación'
      token.value = null
      user.value = null
      localStorage.removeItem('auth_token')
      delete axios.defaults.headers.common['Authorization']
      return false
    } finally {
      loading.value = false
    }
  }

  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('auth_token')
    delete axios.defaults.headers.common['Authorization']
  }

  async function checkAuth(): Promise<boolean> {
    if (!token.value) {
      return false
    }

    try {
      // Try to make an authenticated request to verify token
      await axios.get(`${API_BASE_URL}/api/admin/hero`)
      return true
    } catch (err) {
      // Token is invalid, clear auth
      logout()
      return false
    }
  }

  function clearError() {
    error.value = null
  }

  return {
    // State
    token: readonly(token),
    user: readonly(user),
    loading: readonly(loading),
    error: readonly(error),
    
    // Computed
    isAuthenticated,
    isAdmin,
    
    // Actions
    login,
    logout,
    checkAuth,
    clearError
  }
})
