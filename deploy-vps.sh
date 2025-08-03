#!/bin/bash

# Script de despliegue para VPS
# Cloud Fort Technologies

echo "🚀 INICIANDO DESPLIEGUE EN VPS..."

# Variables de configuración
VPS_IP="TU_IP_DEL_VPS"  # Cambia esto por tu IP real
DOMAIN="tu-dominio.com"  # Opcional: si tienes dominio

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para mostrar mensajes
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}"
    exit 1
}

warning() {
    echo -e "${YELLOW}[WARNING] $1${NC}"
}

info() {
    echo -e "${BLUE}[INFO] $1${NC}"
}

# Verificar que Docker está instalado
if ! command -v docker &> /dev/null; then
    error "Docker no está instalado. Por favor instala Docker primero."
fi

if ! command -v docker-compose &> /dev/null; then
    error "Docker Compose no está instalado. Por favor instala Docker Compose primero."
fi

log "Docker y Docker Compose están instalados ✅"

# Verificar permisos de Docker
if ! docker ps &> /dev/null; then
    error "No tienes permisos para ejecutar Docker. Ejecuta: sudo usermod -aG docker \$USER"
fi

# Detener contenedores existentes
log "Deteniendo contenedores existentes..."
docker-compose -f docker-compose.prod.yml down 2>/dev/null || true

# Limpiar imágenes antiguas (opcional)
read -p "¿Quieres limpiar las imágenes anteriores? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    log "Limpiando imágenes anteriores..."
    docker system prune -f
fi

# Construir nuevas imágenes
log "Construyendo imágenes..."
docker-compose -f docker-compose.prod.yml build --no-cache

# Configurar variables de entorno
log "Configurando variables de entorno..."
if [ ! -f .env.prod ]; then
    warning "Archivo .env.prod no encontrado. Creando uno por defecto..."
    cat > .env.prod << EOF
# Configuración para producción
ENVIRONMENT=production
DATABASE_URL=sqlite:///./contacts.db
CORS_ORIGINS=http://${VPS_IP},https://${VPS_IP},http://${DOMAIN},https://${DOMAIN}
VITE_API_URL=http://${VPS_IP}:8000
NODE_ENV=production
EOF
fi

# Verificar puertos disponibles
log "Verificando puertos..."
if netstat -tuln | grep -q ":80 "; then
    warning "Puerto 80 está en uso"
fi
if netstat -tuln | grep -q ":3000 "; then
    warning "Puerto 3000 está en uso"
fi
if netstat -tuln | grep -q ":8000 "; then
    warning "Puerto 8000 está en uso"
fi

# Configurar firewall (si ufw está instalado)
if command -v ufw &> /dev/null; then
    log "Configurando firewall..."
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    sudo ufw allow 3000/tcp
    sudo ufw allow 8000/tcp
    sudo ufw --force enable
fi

# Levantar servicios
log "Levantando servicios..."
docker-compose -f docker-compose.prod.yml up -d

# Esperar a que los servicios estén listos
log "Esperando a que los servicios estén listos..."
sleep 30

# Verificar estado de los servicios
log "Verificando estado de los servicios..."
docker-compose -f docker-compose.prod.yml ps

# Verificar conectividad
log "Verificando conectividad..."
if curl -f http://localhost:8000/health &>/dev/null; then
    log "✅ Backend está respondiendo en puerto 8000"
else
    error "❌ Backend no está respondiendo en puerto 8000"
fi

if curl -f http://localhost:3000 &>/dev/null; then
    log "✅ Frontend está respondiendo en puerto 3000"
else
    error "❌ Frontend no está respondiendo en puerto 3000"
fi

# Mostrar información final
echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "🎉 DESPLIEGUE COMPLETADO EXITOSAMENTE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
info "🌐 Aplicación disponible en:"
info "   • Frontend: http://${VPS_IP}:3000"
info "   • Backend API: http://${VPS_IP}:8000"
info "   • Documentación API: http://${VPS_IP}:8000/docs"
info "   • Admin Login: http://${VPS_IP}:3000/login"
echo
info "📊 Para monitorear los logs:"
info "   docker-compose -f docker-compose.prod.yml logs -f"
echo
info "🔄 Para reiniciar servicios:"
info "   docker-compose -f docker-compose.prod.yml restart"
echo
info "🛑 Para detener servicios:"
info "   docker-compose -f docker-compose.prod.yml down"
echo
warning "⚠️  IMPORTANTE:"
warning "   1. Reemplaza 'TU_IP_DEL_VPS' con tu IP real en este script"
warning "   2. Configura tu dominio si tienes uno"
warning "   3. Considera usar un proxy reverso como Nginx para producción"
warning "   4. Configura SSL/HTTPS para mayor seguridad"
echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
