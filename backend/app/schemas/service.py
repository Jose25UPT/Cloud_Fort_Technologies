from typing import Optional
from pydantic import BaseModel, Field
import uuid


class ServiceBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    descripcion: str = Field(..., min_length=1, max_length=2000)
    icono: Optional[str] = Field(None, max_length=100)


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=1, max_length=2000)
    icono: Optional[str] = Field(None, max_length=100)


class ServiceInDB(ServiceBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True


class ServiceResponse(ServiceInDB):
    pass
