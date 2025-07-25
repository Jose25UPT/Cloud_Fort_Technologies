# CloudFort Technologies - Desarrollo
# Script para inicializar el stack de desarrollo con Docker

Write-Host "🚀 Iniciando CloudFort Technologies Stack (Desarrollo)" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan

# Verificar si Docker está corriendo
try {
    docker version *>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Docker no está ejecutándose"
    }
} catch {
    Write-Host "❌ Error: Docker no está disponible o no está ejecutándose" -ForegroundColor Red
    Write-Host "Por favor, inicia Docker Desktop e intenta nuevamente." -ForegroundColor Yellow
    exit 1
}

# Verificar si existe el archivo .env
if (!(Test-Path ".env")) {
    Write-Host "❌ Error: El archivo .env no existe" -ForegroundColor Red
    Write-Host "Por favor, crea el archivo .env basándote en .env.example" -ForegroundColor Yellow
    exit 1
}

# Limpiar contenedores anteriores si existen
Write-Host "🧹 Limpiando contenedores anteriores..." -ForegroundColor Yellow
docker-compose -f docker-compose.dev.yml down -v

# Construir e inicializar los servicios
Write-Host "🔨 Construyendo e iniciando servicios..." -ForegroundColor Blue
docker-compose -f docker-compose.dev.yml up --build

Write-Host "✅ Stack iniciado correctamente!" -ForegroundColor Green
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "PostgreSQL: localhost:5432" -ForegroundColor Cyan
Write-Host "Redis: localhost:6379" -ForegroundColor Cyan
