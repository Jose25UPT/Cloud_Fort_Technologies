# CloudFort Technologies

A modern full-stack web application built with Vue.js 3 and FastAPI, designed for scalable deployment on VPS infrastructure.

## 🚀 Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Fast build tool and dev server

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy 2.0** - Async ORM
- **PostgreSQL** - Primary database
- **Redis** - Caching and session storage

### DevOps
- **Docker & Docker Compose** - Containerization
- **Nginx** - Reverse proxy and static file serving
- **Alembic** - Database migrations

## 🏗️ Project Structure

```
cloudfort-technologies/
├── frontend/           # Vue.js application
├── backend/           # FastAPI application
├── nginx/             # Nginx configuration
├── scripts/           # Deployment and utility scripts
└── docker-compose.yml # Docker services orchestration
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git

### Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd cloudfort-technologies
```

2. Copy environment variables:
```bash
cp .env.example .env
```

3. Start the development environment:
```bash
docker-compose up -d
```

4. Access the applications:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 📦 Services

| Service  | Port | Description                    |
|----------|------|--------------------------------|
| Frontend | 3000 | Vue.js development server      |
| Backend  | 8000 | FastAPI application            |
| Postgres | 5432 | PostgreSQL database            |
| Redis    | 6379 | Redis cache                    |
| Nginx    | 80   | Reverse proxy (production)     |

## 🛠️ Development

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Backend Development
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Database Migrations
```bash
# Generate migration
docker-compose exec backend alembic revision --autogenerate -m "Description"

# Apply migrations
docker-compose exec backend alembic upgrade head
```

## 🚀 VPS Deployment

1. Set up your VPS with Docker and Docker Compose
2. Clone the repository
3. Update `.env` with production values
4. Run deployment script:
```bash
./scripts/entrypoint.sh
```

## 📝 License

This project is private and proprietary to CloudFort Technologies.

## 🤝 Contributing

Please read the contributing guidelines before making any changes.
