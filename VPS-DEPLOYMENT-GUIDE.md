# 🚀 GUÍA DE DESPLIEGUE EN VPS DEBIAN

## Requisitos Previos

### 1. Instalar Docker en Debian
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release

# Agregar clave GPG de Docker
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Agregar repositorio de Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Reiniciar sesión o ejecutar:
newgrp docker
```

### 2. Configurar Firewall
```bash
# Instalar ufw si no está instalado
sudo apt install -y ufw

# Configurar reglas básicas
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 3000/tcp
sudo ufw allow 8000/tcp

# Activar firewall
sudo ufw --force enable

# Verificar estado
sudo ufw status
```

## Despliegue

### 1. Subir código al VPS
```bash
# Opción 1: Usando Git (recomendado)
git clone https://github.com/Jose25UPT/Cloud_Fort_Technologies.git
cd Cloud_Fort_Technologies

# Opción 2: Usando SCP/SFTP
# Sube el proyecto al VPS en /home/usuario/Cloud_Fort_Technologies
```

### 2. Configurar Variables de Entorno
```bash
# Editar archivo de producción
nano .env.prod

# Reemplazar con tu información real:
# - tu-ip-vps: Tu IP pública del VPS
# - tu-dominio.com: Tu dominio (opcional)
```

### 3. Editar Script de Despliegue
```bash
# Editar script
nano deploy-vps.sh

# Cambiar la línea:
VPS_IP="TU_IP_DEL_VPS"
# Por tu IP real, ejemplo:
VPS_IP="203.0.113.1"

# Hacer ejecutable
chmod +x deploy-vps.sh
```

### 4. Ejecutar Despliegue
```bash
# Ejecutar script de despliegue
./deploy-vps.sh

# O manualmente:
docker-compose -f docker-compose.prod.yml build --no-cache
docker-compose -f docker-compose.prod.yml up -d
```

## Verificación

### 1. Verificar Contenedores
```bash
docker-compose -f docker-compose.prod.yml ps
```

### 2. Verificar Logs
```bash
# Todos los logs
docker-compose -f docker-compose.prod.yml logs -f

# Solo backend
docker-compose -f docker-compose.prod.yml logs -f backend

# Solo frontend  
docker-compose -f docker-compose.prod.yml logs -f frontend
```

### 3. Verificar Conectividad
```bash
# Verificar puertos abiertos
netstat -tuln | grep -E ":(80|443|3000|8000) "

# Probar endpoints
curl http://localhost:8000/health
curl http://localhost:3000
```

## Acceso a la Aplicación

Una vez desplegado, tu aplicación estará disponible en:

- **Frontend**: `http://tu-ip-vps:3000`
- **Backend API**: `http://tu-ip-vps:8000`
- **Documentación API**: `http://tu-ip-vps:8000/docs`
- **Admin Panel**: `http://tu-ip-vps:3000/login`

## Credenciales de Admin

- **Usuario**: `cloudfort_admin`
- **Contraseña**: `CloudFort2025AdminSecure`

## Solución de Problemas Comunes

### Puerto No Accesible desde Fuera
```bash
# Verificar que el firewall permite el tráfico
sudo ufw status

# Verificar que Docker está corriendo
sudo systemctl status docker

# Verificar logs de contenedores
docker-compose -f docker-compose.prod.yml logs
```

### Error de Permisos
```bash
# Agregar usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker

# Verificar permisos
docker ps
```

### Error de Conexión API
```bash
# Verificar configuración CORS en .env.prod
# Asegúrate de que tu IP esté en CORS_ORIGINS

# Verificar conectividad interna
docker exec -it cloudfort-backend curl http://localhost:8000/health
```

## Mantenimiento

### Actualizar Aplicación
```bash
# Detener servicios
docker-compose -f docker-compose.prod.yml down

# Actualizar código
git pull origin main

# Reconstruir y levantar
docker-compose -f docker-compose.prod.yml build --no-cache
docker-compose -f docker-compose.prod.yml up -d
```

### Backup de Base de Datos
```bash
# Hacer backup
docker cp cloudfort-backend:/app/contacts.db ./backup-$(date +%Y%m%d).db

# Restaurar backup
docker cp ./backup-20250802.db cloudfort-backend:/app/contacts.db
docker-compose -f docker-compose.prod.yml restart backend
```

### Monitoreo
```bash
# Ver uso de recursos
docker stats

# Ver logs en tiempo real
docker-compose -f docker-compose.prod.yml logs -f --tail=100
```

## Configuración con Nginx (Opcional)

Para mayor rendimiento y seguridad, puedes configurar Nginx como proxy reverso:

```bash
# Instalar Nginx
sudo apt install -y nginx

# Crear configuración
sudo nano /etc/nginx/sites-available/cloudfort

# [Contenido del archivo de configuración Nginx...]

# Habilitar sitio
sudo ln -s /etc/nginx/sites-available/cloudfort /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## SSL/HTTPS con Let's Encrypt (Opcional)

```bash
# Instalar Certbot
sudo apt install -y certbot python3-certbot-nginx

# Obtener certificado
sudo certbot --nginx -d tu-dominio.com

# Configurar renovación automática
sudo crontab -e
# Agregar: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Contacto y Soporte

Si tienes problemas con el despliegue, revisa:

1. Los logs de Docker Compose
2. La configuración del firewall
3. Las variables de entorno
4. La conectividad de red del VPS

Para más ayuda, contacta al equipo de desarrollo.
