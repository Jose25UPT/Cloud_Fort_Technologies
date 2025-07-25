import uuid
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base


class Hero(Base):
    __tablename__ = "heroes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = Column(String(200), nullable=False)
    subtitulo = Column(Text, nullable=True)
    cta_texto = Column(String(100), nullable=True)
    cta_url = Column(String(500), nullable=True)
    imagen_url = Column(String(500), nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Hero {self.titulo}>"
