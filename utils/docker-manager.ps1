# Script para manejar el entorno Docker de CloudFort
# Asegúrate de que Docker Desktop esté ejecutándose antes de usar este script

param(
    [Parameter(Mandatory=$true, Position=0)]
    [ValidateSet("start", "stop", "restart", "build", "logs", "status")]
    [string]$Action
)

$PROJECT_DIR = "c:\Users\LENOVO\Desktop\Cloud_Fort_Technologies"
$ENV_FILE = ".env.dev"

Set-Location $PROJECT_DIR

switch ($Action) {
    "start" {
        Write-Host "🚀 Iniciando servicios Docker..." -ForegroundColor Green
        docker-compose --env-file $ENV_FILE up -d
        Write-Host "✅ Servicios iniciados:" -ForegroundColor Green
        Write-Host "   - Frontend: http://localhost:3000" -ForegroundColor Cyan
        Write-Host "   - Backend: http://localhost:8000" -ForegroundColor Cyan
        Write-Host "   - Admin Panel: http://localhost:3000/admin" -ForegroundColor Cyan
    }
    "stop" {
        Write-Host "🛑 Deteniendo servicios Docker..." -ForegroundColor Yellow
        docker-compose --env-file $ENV_FILE down
        Write-Host "✅ Servicios detenidos" -ForegroundColor Green
    }
    "restart" {
        Write-Host "🔄 Reiniciando servicios Docker..." -ForegroundColor Yellow
        docker-compose --env-file $ENV_FILE down
        docker-compose --env-file $ENV_FILE up -d
        Write-Host "✅ Servicios reiniciados" -ForegroundColor Green
    }
    "build" {
        Write-Host "🔨 Construyendo imágenes Docker..." -ForegroundColor Blue
        docker-compose --env-file $ENV_FILE build --no-cache
        Write-Host "✅ Imágenes construidas" -ForegroundColor Green
    }
    "logs" {
        Write-Host "📋 Mostrando logs de los servicios..." -ForegroundColor Cyan
        docker-compose --env-file $ENV_FILE logs -f
    }
    "status" {
        Write-Host "📊 Estado de los servicios:" -ForegroundColor Cyan
        docker-compose --env-file $ENV_FILE ps
    }
}
