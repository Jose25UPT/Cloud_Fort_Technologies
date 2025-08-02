# 🏢 CloudFort Technologies - Sistema Web Completo

Sistema web empresarial completo con formulario de contacto, bandeja de entrada administrativa avanzada y arquitectura Docker optimizada.

## 🎯 Descripción del Proyecto

CloudFort Technologies es una plataforma web integral que incluye:
- **🌐 Sitio web corporativo** moderno y responsive
- **📨 Bandeja de entrada administrativa** con funcionalidades avanzadas
- **📊 Dashboard de estadísticas** integrado
- **🔐 Sistema de autenticación** JWT
- **📄 Generación de reportes PDF** 
- **📱 Gestión de archivos adjuntos** con visualización
- **🐳 Containerización Docker** para desarrollo y producción

---

## 🏗️ Arquitectura del Sistema

### Frontend (Vue.js 3 + TypeScript)
- **Framework**: Vue.js 3 con Composition API
- **Lenguaje**: TypeScript para type safety
- **Estilos**: Tailwind CSS para diseño responsive
- **Build Tool**: Vite para desarrollo rápido
- **Router**: Vue Router 4 con lazy loading y autenticación
- **Estado**: Pinia para gestión de estado

### Backend (FastAPI + Python)
- **Framework**: FastAPI con Python 3.11
- **Base de Datos**: SQLite para simplicidad y rendimiento
- **Validación**: Pydantic para validación de datos
- **Seguridad**: JWT tokens con expiración automática
- **Archivos**: Gestión completa de uploads con soporte multimedia
- **CORS**: Configurado para desarrollo y producción

### Containerización
- **Docker**: Contenedores optimizados para backend y frontend
- **Docker Compose**: Orquestación simplificada de servicios
- **Networking**: Red interna para comunicación segura
- **Volumes**: Persistencia de datos y archivos multimedia

---

## 📁 Estructura del Proyecto

```
CloudFort_Technologies/
├── 📂 backend/                    # API FastAPI
│   ├── 📄 main.py                # Aplicación principal optimizada
│   ├── 📄 Dockerfile             # Imagen Docker backend
│   ├── 📄 requirements.txt       # Dependencias Python
│   ├── 📄 contacts.db            # Base de datos SQLite
│   └── 📁 uploads/               # Archivos multimedia subidos
│
├── 📂 frontend/                   # Aplicación Vue.js
│   ├── 📁 src/
│   │   ├── 📁 components/        # Componentes reutilizables
│   │   ├── 📁 pages/             # Páginas principales
│   │   │   ├── 📄 Home.vue      # Página principal corporativa
│   │   │   └── 📁 admin/        # Panel administrativo
│   │   │       ├── 📄 AdminDashboard.vue  # Dashboard principal
│   │   │       ├── 📄 AdminLogin.vue      # Login administrativo
│   │   │       └── 📄 TestBandeja.vue     # Bandeja avanzada
│   │   ├── 📁 services/          # Servicios API
│   │   ├── 📁 stores/            # Estado global (Pinia)
│   │   └── 📁 router/            # Configuración de rutas
│   ├── 📄 Dockerfile.dev         # Imagen Docker frontend
│   ├── 📄 package.json          # Dependencias Node.js
│   └── 📄 tsconfig.json         # Configuración TypeScript
│
├── 📄 docker-compose.yml         # Orquestación Docker
└── 📄 .env.dev                  # Variables de entorno
```

---

## 🚀 Instalación y Uso

### Prerequisitos
- **Docker Desktop** (recomendado)
- **PowerShell** 5.1+ (Windows)
- **Git** para clonar el repositorio

### Opción 1: Con Docker (Recomendado)

```powershell
# 1. Clonar el repositorio
git clone <repo-url>
cd CloudFort_Technologies

# 2. Construir las imágenes
docker-compose build --no-cache

# 3. Levantar los servicios
docker-compose up -d

# 4. Verificar estado
docker-compose ps
```

---

## 🌐 URLs de Acceso

| Servicio | URL | Descripción |
|----------|-----|-------------|
| 🌐 **Sitio Principal** | http://localhost:3000 | Página corporativa con formulario de contacto |
| 🔐 **Login Admin** | http://localhost:3000/login | Panel de autenticación administrativo |
| 📊 **Dashboard Admin** | http://localhost:3000/admin | Panel de administración principal |
| 📨 **Bandeja Avanzada** | http://localhost:3000/bandeja_entrada_cloudforttechnologies | Bandeja de entrada con funcionalidades avanzadas |
| 📡 **API Backend** | http://localhost:8000 | API REST FastAPI |
| 📚 **Documentación API** | http://localhost:8000/docs | Documentación interactiva Swagger |

---

## ✨ Funcionalidades Principales

### 🌐 Sitio Web Corporativo
- **Diseño Moderno**: Interfaz responsive con Tailwind CSS
- **Formulario de Contacto**: Envío con validación completa
- **Subida de Archivos**: Soporte para imágenes y documentos
- **Animaciones**: Transiciones suaves y modernas

### 📨 Sistema de Contactos Avanzado
- **Bandeja de Entrada Inteligente**: Visualización completa de solicitudes
- **Filtros y Búsqueda**: Búsqueda por nombre, email, empresa, tipo
- **Gestión de Archivos**: Visualización de imágenes con modal expandible
- **Descarga Individual**: PDF completo de cada solicitud
- **Descarga Masiva**: Reporte consolidado de todas las solicitudes

### 📊 Dashboard de Estadísticas
- **Métricas en Tiempo Real**: Visitas diarias, semanales, conversiones
- **Análisis Geográfico**: Estadísticas por países de origen
- **Gráficos Interactivos**: Visualización de datos con barras de progreso
- **Estado del Sistema**: Información de salud del servidor y base de datos

### 🔐 Sistema de Autenticación
- **JWT Tokens**: Autenticación segura con expiración automática
- **Protección de Rutas**: Guard de navegación automático
- **Sesiones Persistentes**: Mantenimiento de sesión entre recargas
- **Logout Automático**: Por expiración o manual

### 📄 Generación de Reportes
- **PDF Individual**: Reporte completo de cada contacto con formato profesional
- **PDF Masivo**: Consolidado de todas las solicitudes con estadísticas
- **Formato Profesional**: Diseño corporativo con logo y fechas
- **Información Completa**: Todos los datos del contacto y archivos adjuntos

---

## 🛠️ Desarrollo

### Comandos Útiles

```powershell
# Ver logs en tiempo real
docker-compose logs -f

# Reconstruir solo el frontend
docker-compose build frontend

# Reconstruir solo el backend  
docker-compose build backend

# Parar servicios
docker-compose down

# Limpiar volúmenes
docker-compose down -v
```

---

## 🔧 Configuración

### Variables de Entorno (.env.dev)

```env
# Configuración del Backend
BACKEND_PORT=8000
DATABASE_URL=sqlite:///./contacts.db
JWT_SECRET_KEY=your-secret-key-here
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# Configuración del Frontend
FRONTEND_PORT=3000
VITE_API_URL=http://localhost:8000
```

### Credenciales de Administrador

```
Usuario: admin
Contraseña: cloudfort2024
```

---

## 📈 Funcionalidades Avanzadas Implementadas

### 🎯 Bandeja de Entrada Avanzada
- **Ruta Segura**: `/bandeja_entrada_cloudforttechnologies` (difícil de adivinar)
- **Navegación por Pestañas**: Bandeja de entrada + Dashboard integrado
- **Visualización Completa**: Información detallada de cada solicitud
- **Gestión de Archivos**: Visualización y descarga de imágenes adjuntas
- **Modal de Imagen**: Visualización en tamaño completo
- **Acciones Rápidas**: Responder por email, marcar como procesado

### 📊 Dashboard Integrado
- **Estadísticas Simuladas**: Visitas diarias, semanales, países
- **Métricas de Conversión**: Tasa de conversión de visitantes a contactos
- **Información del Sistema**: Estado del servidor, base de datos, última actualización
- **Gráficos Visuales**: Barras de progreso para datos comparativos

### 📄 Sistema de Reportes PDF
- **Generación HTML**: Reportes profesionales en formato HTML descargable
- **Plantilla Corporativa**: Diseño con logo y colores de la marca
- **Información Completa**: Todos los datos del contacto organizados
- **Descargas Masivas**: Reporte consolidado de múltiples solicitudes

---

## 🔍 Solución de Problemas

### Problemas Comunes

1. **Contenedores no inician**
   ```powershell
   docker-compose down
   docker-compose build --no-cache
   docker-compose up -d
   ```

2. **Errores de TypeScript**
   ```powershell
   cd frontend
   npm run type-check
   ```

3. **Base de datos corrupta**
   ```powershell
   docker-compose down -v
   docker-compose up -d
   ```

4. **Puertos ocupados**
   - Verificar que los puertos 3000 y 8000 estén libres
   - Cambiar puertos en docker-compose.yml si es necesario

---

## 🚀 Próximas Mejoras

- [ ] **Sistema de Notificaciones**: Alerts en tiempo real para nuevas solicitudes
- [ ] **Dashboard Analytics Real**: Integración con Google Analytics
- [ ] **Sistema de Respuestas**: Templates de email para respuestas automáticas
- [ ] **Backup Automático**: Sistema de respaldo de base de datos
- [ ] **API REST Completa**: CRUD completo para gestión de contactos
- [ ] **Roles de Usuario**: Sistema de permisos administrativos

---

## 📞 Soporte

Para soporte técnico o consultas sobre el proyecto:

- **Email**: soporte@cloudforttechnologies.com
- **Documentación**: http://localhost:8000/docs (cuando esté ejecutándose)
- **Issues**: GitHub Issues del repositorio

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**CloudFort Technologies** - Soluciones tecnológicas empresariales de alta calidad.
