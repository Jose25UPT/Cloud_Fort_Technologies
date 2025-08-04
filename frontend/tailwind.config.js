/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // VARNOX Modern Professional Colors
        'varnox-primary': '#6366F1',      // Índigo vibrante
        'varnox-secondary': '#8B5CF6',    // Púrpura elegante  
        'varnox-accent': '#F59E0B',       // Amarillo dorado
        
        // Tactical Colors (solo para hero y footer)
        'tech-green': '#00FF41',
        'tactical-blue': '#0A4D68',
        'arsenal-grey': '#2D3748',
        'stealth-black': '#0D1117',
        'alert-orange': '#FF6B35',
        'radar-green': '#39FF14',
        'military-olive': '#556B2F',
        
        // Legacy VARNOX Brand Colors
        'pure-black': '#000000',
        'pure-white': '#FFFFFF',
        'space-grey': '#1D1D1F',
        'graphite': '#3A3A3C',
        'silver': '#D1D1D6',
        'electric-blue': '#0A84FF',
      },
      fontFamily: {
        'orbitron': ['Orbitron', 'monospace'],           // Para títulos heroicos
        'poppins': ['Poppins', 'sans-serif'],           // Para encabezados de sección
        'source-sans': ['Source Sans Pro', 'sans-serif'], // Para texto del cuerpo
        'rajdhani': ['Rajdhani', 'sans-serif'],         // Para elementos de acento
        'exo': ['Exo 2', 'sans-serif'],                 // Para títulos de display
        'jetbrains': ['JetBrains Mono', 'monospace'],   // Para código y elementos técnicos
        
        // Legacy fonts
        'urbanist': ['Urbanist', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
        'space-grotesk': ['Space Grotesk', 'sans-serif'],
        'manrope': ['Manrope', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 1s ease-in-out',
        'fade-in-up': 'fadeInUp 1s ease-out',
        'slide-in-right': 'slideInRight 0.8s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(30px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideInRight: {
          '0%': { opacity: '0', transform: 'translateX(30px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
