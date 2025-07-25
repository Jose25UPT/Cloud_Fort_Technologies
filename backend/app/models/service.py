import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


class Service(Base):
    __tablename__ = "services"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    icono = Column(String(100), nullable=True)  # Can be icon class name or URL
    
    def __repr__(self):
        return f"<Service {self.titulo}>"
