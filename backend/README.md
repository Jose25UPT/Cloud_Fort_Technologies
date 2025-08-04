# VARNOX - Backend

FastAPI + SQLAlchemy 2.0 async + PostgreSQL + Redis backend API.

## 🛠️ Tech Stack

- **FastAPI** - Modern async Python web framework
- **SQLAlchemy 2.0** - Async ORM
- **PostgreSQL** - Primary database
- **Redis** - Caching and sessions
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **JWT** - Authentication
- **Docker** - Containerization

## 📁 Project Structure

```
app/
├── core/           # Core functionality (security, config)
├── api/            # API routes and dependencies
│   ├── routes/     # API route handlers
│   └── deps/       # Route dependencies
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── services/       # Business logic services
├── db/             # Database configuration
├── main.py         # FastAPI application
└── config.py       # Application settings
```

## 🚀 Development

### Prerequisites
- Python 3.11+
- PostgreSQL
- Redis

### Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start the development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Database Migrations
```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Downgrade migration
alembic downgrade -1
```

## 🗄️ Database

### Models
- User authentication and management
- Extensible model architecture
- Async SQLAlchemy 2.0 patterns

### Migrations
- Automatic schema generation with Alembic
- Version controlled database changes
- Support for data migrations

## 🔒 Security

### Authentication
- JWT-based authentication
- Refresh token support
- Role-based access control

### Security Features
- Password hashing with bcrypt
- CORS configuration
- Input validation with Pydantic
- SQL injection protection

## 📡 API Documentation

### Interactive Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

### API Versioning
- Version prefix: `/api/v1`
- Backward compatibility support

## 🔧 Configuration

### Environment Variables
```env
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/db

# Redis
REDIS_URL=redis://:password@localhost:6379

# Security
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
```

## 🐳 Docker

### Development
```bash
docker build -t varnox-backend .
docker run -p 8000:8000 varnox-backend
```

### Production
- Multi-stage build for smaller images
- Non-root user for security
- Health checks included

## 🧪 Testing

### Run Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=app

# Specific test file
pytest tests/test_users.py
```

### Test Structure
- Unit tests for services
- Integration tests for API endpoints
- Database test fixtures

## 📊 Monitoring

### Health Checks
- `/health` endpoint for service monitoring
- Database connectivity checks
- Redis connectivity checks

### Logging
- Structured logging with structlog
- Request/response logging
- Error tracking

## 🔄 Background Tasks

### Celery Integration (Optional)
- Async task processing
- Redis as message broker
- Monitoring with Flower

## 📝 Code Quality

### Tools
- Black: Code formatting
- isort: Import sorting
- flake8: Linting
- mypy: Type checking

### Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
```
