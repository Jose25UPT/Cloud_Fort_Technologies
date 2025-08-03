#!/bin/bash

# Script simple de despliegue para VPS
echo "🚀 Iniciando despliegue simplificado..."

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    echo -e "${GREEN}[INFO] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}"
    exit 1
}

warning() {
    echo -e "${YELLOW}[WARNING] $1${NC}"
}

# Verificar Docker
if ! command -v docker &> /dev/null; then
    error "Docker no está instalado"
fi

if ! command -v docker-compose &> /dev/null; then
    error "Docker Compose no está instalado"
fi

# Detener contenedores existentes
log "Deteniendo contenedores existentes..."
docker-compose -f docker-compose.prod.yml down 2>/dev/null || true

# Limpiar caché de build
log "Limpiando caché de Docker..."
docker builder prune -f

# Construir backend primero
log "Construyendo backend..."
docker-compose -f docker-compose.prod.yml build --no-cache backend

# Construir frontend
log "Construyendo frontend..."
docker-compose -f docker-compose.prod.yml build --no-cache frontend

# Levantar servicios
log "Levantando servicios..."
docker-compose -f docker-compose.prod.yml up -d

# Esperar y verificar
log "Esperando servicios..."
sleep 30

# Mostrar estado
log "Estado de contenedores:"
docker-compose -f docker-compose.prod.yml ps

# Verificar logs
log "Últimos logs:"
docker-compose -f docker-compose.prod.yml logs --tail=20

echo
log "✅ Despliegue completado"
log "🌐 Frontend: http://tu-ip:3000"
log "🔗 Backend: http://tu-ip:8000"
echo
