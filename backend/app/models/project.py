import uuid
from sqlalchemy import Column, String, Text, Date, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base


class Project(Base):
    __tablename__ = "projects"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    imagen_url = Column(String(500), nullable=True)
    tags = Column(ARRAY(String), nullable=True)  # Array of string tags
    link = Column(String(500), nullable=True)
    fecha = Column(Date, nullable=True)
    
    def __repr__(self):
        return f"<Project {self.nombre}>"
