import uuid
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


class Testimonial(Base):
    __tablename__ = "testimonials"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_cliente = Column(String(200), nullable=False)
    cargo = Column(String(200), nullable=True)
    opinion = Column(Text, nullable=False)
    imagen_url = Column(String(500), nullable=True)
    
    def __repr__(self):
        return f"<Testimonial {self.nombre_cliente}>"
