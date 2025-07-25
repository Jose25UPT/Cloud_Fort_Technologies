#!/bin/bash

# CloudFort Technologies Deployment Script
set -e

echo "🚀 CloudFort Technologies - VPS Deployment Script"
echo "=================================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Validate environment file
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please copy .env.example to .env and configure it."
    exit 1
fi

echo "✅ Prerequisites check passed!"

# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker-compose down --remove-orphans

# Pull latest images
echo "📥 Pulling latest images..."
docker-compose pull

# Build custom images
echo "🔨 Building application images..."
docker-compose build --no-cache

# Start services
echo "🚀 Starting services..."
docker-compose up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to start..."
sleep 10

# Check service health
echo "🏥 Checking service health..."
if docker-compose exec backend curl -f http://localhost:8000/health; then
    echo "✅ Backend is healthy"
else
    echo "❌ Backend health check failed"
    docker-compose logs backend
    exit 1
fi

# Initialize database
echo "💾 Initializing database..."
./scripts/init_db.sh

# Show running services
echo "📋 Services Status:"
docker-compose ps

# Show access information
echo ""
echo "🎉 CloudFort Technologies deployed successfully!"
echo "=================================================="
echo "🌐 Frontend: http://localhost (via Nginx)"
echo "🔌 Backend API: http://localhost/api"
echo "📚 API Documentation: http://localhost/api/docs"
echo "🗄️ Database: PostgreSQL running on port 5432"
echo "📦 Redis: Running on port 6379"
echo ""
echo "🔧 Management Commands:"
echo "• View logs: docker-compose logs -f [service]"
echo "• Stop services: docker-compose down"
echo "• Restart services: docker-compose restart"
echo "• Shell access: docker-compose exec [service] /bin/bash"
echo ""
echo "📁 Log locations:"
echo "• Application logs: docker-compose logs"
echo "• Nginx logs: docker-compose logs nginx"
echo ""

# Setup log rotation (optional for production)
if [ "$ENVIRONMENT" = "production" ]; then
    echo "⚙️ Setting up log rotation for production..."
    # Add logrotate configuration here if needed
fi

echo "✅ Deployment completed successfully!"
