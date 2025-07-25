import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base


class ContactRequest(Base):
    __tablename__ = "contact_requests"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(200), nullable=False)
    correo = Column(String(200), nullable=False)
    empresa = Column(String(200), nullable=True)
    mensaje = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    pdf_path = Column(String(500), nullable=True)  # Path to generated PDF
    
    def __repr__(self):
        return f"<ContactRequest {self.nombre} - {self.correo}>"
