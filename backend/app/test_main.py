import pytest
from fastapi.testclient import TestClient
from main import app
from app.config import settings

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Cloud Fort Technologies API"
    assert data["version"] == settings.VERSION
    assert data["status"] == "running"


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "version" in data


def test_public_home_endpoint():
    """Test public home endpoint"""
    response = client.get("/api/public/home")
    assert response.status_code == 200
    data = response.json()
    assert "hero" in data
    assert "services" in data
    assert "projects" in data
    assert "testimonials" in data
    assert "company" in data


def test_admin_login():
    """Test admin login"""
    login_data = {
        "email": settings.ADMIN_EMAIL,
        "password": settings.ADMIN_PASSWORD
    }
    response = client.post("/api/auth/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_admin_hero_unauthorized():
    """Test admin hero endpoint without authentication"""
    response = client.get("/api/admin/hero")
    assert response.status_code == 401


def test_admin_services_unauthorized():
    """Test admin services endpoint without authentication"""
    response = client.get("/api/admin/services")
    assert response.status_code == 401


def test_contact_form_submission():
    """Test contact form submission"""
    contact_data = {
        "nombre": "Test User",
        "correo": "test@example.com",
        "empresa": "Test Company",
        "mensaje": "This is a test message for the contact form."
    }
    response = client.post("/api/public/contact", json=contact_data)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "message" in data
    assert "request_id" in data


def test_invalid_contact_form():
    """Test contact form with invalid data"""
    contact_data = {
        "nombre": "",  # Invalid: empty name
        "correo": "invalid-email",  # Invalid: not a valid email
        "mensaje": "Short"  # Invalid: too short
    }
    response = client.post("/api/public/contact", json=contact_data)
    assert response.status_code == 422  # Validation error


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
