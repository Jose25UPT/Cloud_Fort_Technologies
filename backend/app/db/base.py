from sqlalchemy.ext.declarative import declarative_base

# Base class for all database models
Base = declarative_base()

# Import all models here so Alembic can detect them
# from app.models.user import User
# from app.models.item import Item
