#!/bin/bash

# Database initialization script for CloudFort Technologies
set -e

echo "🚀 Initializing CloudFort Technologies Database..."

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
until docker-compose exec postgres pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 2
done

echo "✅ PostgreSQL is ready!"

# Run database migrations
echo "🔄 Running database migrations..."
docker-compose exec backend alembic upgrade head

echo "✅ Database initialized successfully!"

# Create initial admin user (optional)
# echo "👤 Creating initial admin user..."
# docker-compose exec backend python -c "
# from app.core.security import get_password_hash
# from app.db.session import SessionLocal
# from app.models.user import User
# import asyncio

# async def create_admin():
#     db = SessionLocal()
#     admin_user = User(
#         email='admin@cloudfort.com',
#         hashed_password=get_password_hash('admin123'),
#         is_active=True,
#         is_superuser=True,
#         full_name='Admin User'
#     )
#     db.add(admin_user)
#     await db.commit()
#     print('Admin user created successfully!')

# asyncio.run(create_admin())
# "

echo "🎉 Database setup completed!"
