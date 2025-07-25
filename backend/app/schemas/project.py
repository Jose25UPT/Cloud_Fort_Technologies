from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field, validator
import uuid


class ProjectBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=200)
    descripcion: str = Field(..., min_length=1, max_length=2000)
    imagen_url: Optional[str] = Field(None, max_length=500)
    tags: Optional[List[str]] = Field(None)
    link: Optional[str] = Field(None, max_length=500)
    fecha: Optional[date] = None
    
    @validator('imagen_url', 'link')
    def validate_url(cls, v):
        if v and not (v.startswith('http://') or v.startswith('https://') or v.startswith('/')):
            raise ValueError('URL must start with http://, https://, or /')
        return v
    
    @validator('tags')
    def validate_tags(cls, v):
        if v and len(v) > 10:
            raise ValueError('Maximum 10 tags allowed')
        return v


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=1, max_length=2000)
    imagen_url: Optional[str] = Field(None, max_length=500)
    tags: Optional[List[str]] = Field(None)
    link: Optional[str] = Field(None, max_length=500)
    fecha: Optional[date] = None
    
    @validator('imagen_url', 'link')
    def validate_url(cls, v):
        if v and not (v.startswith('http://') or v.startswith('https://') or v.startswith('/')):
            raise ValueError('URL must start with http://, https://, or /')
        return v
    
    @validator('tags')
    def validate_tags(cls, v):
        if v and len(v) > 10:
            raise ValueError('Maximum 10 tags allowed')
        return v


class ProjectInDB(ProjectBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True


class ProjectResponse(ProjectInDB):
    pass
