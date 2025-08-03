#!/bin/bash

# 🚀 SCRIPT DE DESPLIEGUE CLOUD FORT TECHNOLOGIES
# Versión optimizada para VPS

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 CLOUD FORT TECHNOLOGIES - DESPLIEGUE EN VPS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

log() {
    echo -e "${GREEN}[$(date +'%H:%M:%S')] ✅ $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] ❌ $1${NC}"
    exit 1
}

warning() {
    echo -e "${YELLOW}[WARNING] ⚠️  $1${NC}"
}

info() {
    echo -e "${BLUE}[INFO] ℹ️  $1${NC}"
}

step() {
    echo -e "${PURPLE}[STEP] 🔄 $1${NC}"
}

# Verificaciones iniciales
step "Verificando requisitos del sistema..."

if ! command -v docker &> /dev/null; then
    error "Docker no está instalado. Instálalo primero con: curl -fsSL https://get.docker.com | sh"
fi

if ! command -v docker-compose &> /dev/null; then
    error "Docker Compose no está instalado."
fi

if ! docker ps &> /dev/null; then
    error "Sin permisos para Docker. Ejecuta: sudo usermod -aG docker \$USER && newgrp docker"
fi

log "Requisitos verificados correctamente"

# Obtener IP del servidor
SERVER_IP=$(curl -s ifconfig.me 2>/dev/null || curl -s ipinfo.io/ip 2>/dev/null || echo "UNKNOWN")
info "IP del servidor detectada: $SERVER_IP"

# Limpiar contenedores existentes
step "Limpiando instalación anterior..."
docker-compose -f docker-compose.prod.yml down --volumes --remove-orphans 2>/dev/null || true
docker system prune -f 2>/dev/null || true

log "Sistema limpiado"

# Construir imágenes
step "Construyendo imágenes de Docker..."

echo "📦 Construyendo backend..."
if ! docker-compose -f docker-compose.prod.yml build --no-cache backend; then
    error "Error construyendo backend"
fi

echo "🎨 Construyendo frontend..."
if ! docker-compose -f docker-compose.prod.yml build --no-cache frontend; then
    error "Error construyendo frontend"
fi

log "Imágenes construidas exitosamente"

# Levantar servicios
step "Iniciando servicios..."
if ! docker-compose -f docker-compose.prod.yml up -d; then
    error "Error iniciando servicios"
fi

log "Servicios iniciados"

# Esperar a que estén listos
step "Esperando que los servicios estén listos..."
sleep 30

# Verificar estado
step "Verificando estado de los servicios..."
docker-compose -f docker-compose.prod.yml ps

# Verificar conectividad
step "Verificando conectividad..."

# Backend
if curl -f http://localhost:8000/health &>/dev/null; then
    log "Backend responde correctamente en puerto 8000"
else
    warning "Backend no responde en puerto 8000"
    echo "Logs del backend:"
    docker-compose -f docker-compose.prod.yml logs --tail=10 backend
fi

# Frontend
if curl -f http://localhost:3000 &>/dev/null; then
    log "Frontend responde correctamente en puerto 3000"
else
    warning "Frontend no responde en puerto 3000"
    echo "Logs del frontend:"
    docker-compose -f docker-compose.prod.yml logs --tail=10 frontend
fi

# Verificar puertos abiertos
step "Verificando puertos..."
info "Puertos en uso:"
netstat -tuln | grep -E ":(3000|8000) " || echo "Puertos no detectados localmente"

# Resultado final
echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "🎉 DESPLIEGUE COMPLETADO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
info "🌐 URLs DE ACCESO:"
info "   • Frontend:     http://$SERVER_IP:3000"
info "   • Backend API:  http://$SERVER_IP:8000"
info "   • Documentación: http://$SERVER_IP:8000/docs"
info "   • Admin Panel:  http://$SERVER_IP:3000/login"
echo
info "🔐 CREDENCIALES DE ADMIN:"
info "   • Usuario:    cloudfort_admin"
info "   • Contraseña: CloudFort2025AdminSecure"
echo
info "📊 COMANDOS ÚTILES:"
info "   • Ver logs:      docker-compose -f docker-compose.prod.yml logs -f"
info "   • Reiniciar:     docker-compose -f docker-compose.prod.yml restart"
info "   • Detener:       docker-compose -f docker-compose.prod.yml down"
info "   • Ver estado:    docker-compose -f docker-compose.prod.yml ps"
echo
warning "⚠️  CONFIGURACIÓN DEL FIREWALL:"
warning "   Si no puedes acceder desde fuera, asegúrate de abrir los puertos:"
warning "   • sudo ufw allow 3000/tcp"
warning "   • sudo ufw allow 8000/tcp"
echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "✨ Cloud Fort Technologies está ahora disponible en tu VPS!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
