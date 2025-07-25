from typing import Optional
from pydantic import BaseModel, Field, validator
import uuid


class TestimonialBase(BaseModel):
    nombre_cliente: str = Field(..., min_length=1, max_length=200)
    cargo: Optional[str] = Field(None, max_length=200)
    opinion: str = Field(..., min_length=1, max_length=2000)
    imagen_url: Optional[str] = Field(None, max_length=500)
    
    @validator('imagen_url')
    def validate_url(cls, v):
        if v and not (v.startswith('http://') or v.startswith('https://') or v.startswith('/')):
            raise ValueError('URL must start with http://, https://, or /')
        return v


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialUpdate(BaseModel):
    nombre_cliente: Optional[str] = Field(None, min_length=1, max_length=200)
    cargo: Optional[str] = Field(None, max_length=200)
    opinion: Optional[str] = Field(None, min_length=1, max_length=2000)
    imagen_url: Optional[str] = Field(None, max_length=500)
    
    @validator('imagen_url')
    def validate_url(cls, v):
        if v and not (v.startswith('http://') or v.startswith('https://') or v.startswith('/')):
            raise ValueError('URL must start with http://, https://, or /')
        return v


class TestimonialInDB(TestimonialBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True


class TestimonialResponse(TestimonialInDB):
    pass
