import uuid
from sqlalchemy import Column, String, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


class Company(Base):
    __tablename__ = "company"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telefono = Column(String(20), nullable=True)
    email_contacto = Column(String(200), nullable=True)
    redes_sociales = Column(JSON, nullable=True)  # JSON object for social media links
    
    def __repr__(self):
        return f"<Company {self.email_contacto}>"
