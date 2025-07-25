from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
import uuid


class HeroBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    subtitulo: Optional[str] = Field(None, max_length=1000)
    cta_texto: Optional[str] = Field(None, max_length=100)
    cta_url: Optional[str] = Field(None, max_length=500)
    imagen_url: Optional[str] = Field(None, max_length=500)
    
    @validator('cta_url', 'imagen_url')
    def validate_url(cls, v):
        if v and not (v.startswith('http://') or v.startswith('https://') or v.startswith('/')):
            raise ValueError('URL must start with http://, https://, or /')
        return v


class HeroCreate(HeroBase):
    pass


class HeroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    subtitulo: Optional[str] = Field(None, max_length=1000)
    cta_texto: Optional[str] = Field(None, max_length=100)
    cta_url: Optional[str] = Field(None, max_length=500)
    imagen_url: Optional[str] = Field(None, max_length=500)
    
    @validator('cta_url', 'imagen_url')
    def validate_url(cls, v):
        if v and not (v.startswith('http://') or v.startswith('https://') or v.startswith('/')):
            raise ValueError('URL must start with http://, https://, or /')
        return v


class HeroInDB(HeroBase):
    id: uuid.UUID
    updated_at: datetime
    
    class Config:
        from_attributes = True


class HeroResponse(HeroInDB):
    pass
