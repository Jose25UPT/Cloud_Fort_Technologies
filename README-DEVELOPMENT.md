# CloudFort Technologies - Guía de Desarrollo

## 🚀 Inicio Rápido

### Prerrequisitos
- Docker Desktop instalado y ejecutándose
- PowerShell (Windows) o Terminal (macOS/Linux)

### Configuración Inicial

1. **Clona o navega al directorio del proyecto**
```bash
cd cloudfort-technologies
```

2. **Configura las variables de entorno**
```bash
# El archivo .env ya existe, pero puedes modificar los valores si es necesario
# Revisa y actualiza las credenciales en .env si lo deseas
```

3. **Inicia el stack de desarrollo**

**En Windows (PowerShell):**
```powershell
.\start-dev.ps1
```

**En macOS/Linux:**
```bash
chmod +x start-dev.sh
./start-dev.sh
```

**Manualmente (cualquier sistema):**
```bash
docker-compose -f docker-compose.dev.yml up --build
```

### 🌐 URLs de Acceso

Una vez que todos los servicios estén ejecutándose:

- **Frontend (Vue.js)**: http://localhost:3000
- **Backend API (FastAPI)**: http://localhost:8000
- **Documentación API**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

### 📁 Estructura del Proyecto

```
cloudfort-technologies/
├── frontend/                 # Aplicación Vue.js + Tailwind CSS
│   ├── src/
│   │   ├── components/      # Componentes Vue
│   │   │   ├── ContactForm.vue  # Nuevo formulario de contacto
│   │   │   └── ...
│   │   ├── services/        # Servicios para APIs
│   │   │   └── contact.ts   # Servicio de contacto
│   │   └── ...
│   ├── Dockerfile.dev       # Dockerfile para desarrollo
│   └── package.json
├── backend/                 # API FastAPI + PostgreSQL
│   ├── app/
│   │   ├── main.py         # Punto de entrada
│   │   ├── routers/        # Rutas de la API
│   │   └── ...
│   └── Dockerfile
├── docker-compose.yml       # Configuración para producción
├── docker-compose.dev.yml   # Configuración para desarrollo
└── start-dev.ps1           # Script de inicio (Windows)
```

### 🔧 Comandos Útiles

**Ver logs de un servicio específico:**
```bash
docker-compose -f docker-compose.dev.yml logs -f frontend
docker-compose -f docker-compose.dev.yml logs -f backend
```

**Reconstruir un servicio específico:**
```bash
docker-compose -f docker-compose.dev.yml up --build frontend
docker-compose -f docker-compose.dev.yml up --build backend
```

**Detener todos los servicios:**
```bash
docker-compose -f docker-compose.dev.yml down
```

**Detener y eliminar volúmenes (reinicio limpio):**
```bash
docker-compose -f docker-compose.dev.yml down -v
```

**Ejecutar comandos dentro de un contenedor:**
```bash
# Frontend
docker-compose -f docker-compose.dev.yml exec frontend npm install
docker-compose -f docker-compose.dev.yml exec frontend npm run lint

# Backend
docker-compose -f docker-compose.dev.yml exec backend python -c "import sys; print(sys.version)"
```

### 📧 Formulario de Contacto

El nuevo formulario de contacto incluye:

✅ **Campos implementados:**
- Nombre completo (requerido)
- Correo electrónico (requerido)
- Teléfono (requerido)
- Empresa/Marca (requerido)
- Tipo de solución (requerido)
- Presupuesto estimado (requerido)
- Cómo nos encontraste (requerido)
- Mensaje detallado (requerido)
- Adjuntar archivo (opcional)

✅ **Características:**
- Validación en tiempo real
- Subida de archivos (PDF, PNG, JPG, DOCX, máx. 5MB)
- Diseño responsivo
- Animaciones elegantes
- Integración con API backend

### 🛠️ Desarrollo

**Hot reload está habilitado:**
- Los cambios en `frontend/src/` se reflejan automáticamente
- Los cambios en `backend/app/` reinician el servidor automáticamente

**Para desarrollo del formulario de contacto:**
1. El componente principal está en `frontend/src/components/ContactForm.vue`
2. El servicio API está en `frontend/src/services/contact.ts`
3. Los estilos usan Tailwind CSS con la configuración personalizada en `tailwind.config.js`

### 🚨 Solución de Problemas

**Error "Docker no está ejecutándose":**
- Asegúrate de que Docker Desktop esté iniciado
- En Windows, verifica que Docker esté en la barra de sistema

**Error de permisos (Linux/macOS):**
```bash
sudo chmod +x start-dev.sh
```

**Puerto ya en uso:**
```bash
# Cambiar puertos en docker-compose.dev.yml si es necesario
# Por ejemplo: "3001:3000" en lugar de "3000:3000"
```

**Problemas con node_modules:**
```bash
# Eliminar volumen y reconstruir
docker-compose -f docker-compose.dev.yml down -v
docker-compose -f docker-compose.dev.yml up --build
```

### 📞 Contacto para Desarrollo

Si tienes problemas con el setup de desarrollo, revisa los logs con:
```bash
docker-compose -f docker-compose.dev.yml logs
```

---
**Happy Coding! 🎉**
