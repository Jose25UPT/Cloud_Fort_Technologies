from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, EmailStr, validator
import uuid


class CompanyBase(BaseModel):
    telefono: Optional[str] = Field(None, max_length=20)
    email_contacto: Optional[EmailStr] = None
    redes_sociales: Optional[Dict[str, str]] = Field(None, description="Social media links")
    
    @validator('telefono')
    def validate_phone(cls, v):
        if v and not v.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '').isdigit():
            raise ValueError('Invalid phone number format')
        return v
    
    @validator('redes_sociales')
    def validate_social_media(cls, v):
        if v:
            allowed_keys = ['facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'tiktok']
            for key, url in v.items():
                if key.lower() not in allowed_keys:
                    raise ValueError(f'Social media platform {key} not supported')
                if url and not (url.startswith('http://') or url.startswith('https://')):
                    raise ValueError(f'Social media URL for {key} must start with http:// or https://')
        return v


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    telefono: Optional[str] = Field(None, max_length=20)
    email_contacto: Optional[EmailStr] = None
    redes_sociales: Optional[Dict[str, str]] = Field(None)
    
    @validator('telefono')
    def validate_phone(cls, v):
        if v and not v.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '').isdigit():
            raise ValueError('Invalid phone number format')
        return v
    
    @validator('redes_sociales')
    def validate_social_media(cls, v):
        if v:
            allowed_keys = ['facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'tiktok']
            for key, url in v.items():
                if key.lower() not in allowed_keys:
                    raise ValueError(f'Social media platform {key} not supported')
                if url and not (url.startswith('http://') or url.startswith('https://')):
                    raise ValueError(f'Social media URL for {key} must start with http:// or https://')
        return v


class CompanyInDB(CompanyBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True


class CompanyResponse(CompanyInDB):
    pass
