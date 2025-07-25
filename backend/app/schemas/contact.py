from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
import uuid


class ContactRequestBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Full name")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., min_length=8, max_length=20, description="Phone number")
    company: str = Field(..., min_length=1, max_length=200, description="Company or brand name")
    type: str = Field(..., description="Type of solution needed")
    budget: str = Field(..., description="Estimated budget range")
    referral: str = Field(..., description="How they found us")
    message: str = Field(..., min_length=10, max_length=2000, description="Detailed message")


class ContactRequestCreate(ContactRequestBase):
    pass


class ContactRequestInDB(ContactRequestBase):
    id: uuid.UUID
    timestamp: datetime
    pdf_path: Optional[str] = None
    
    class Config:
        from_attributes = True


class ContactRequestResponse(ContactRequestInDB):
    pass


class ContactFormSubmit(BaseModel):
    """Schema for public contact form submission"""
    name: str = Field(..., min_length=1, max_length=200, description="Full name")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., min_length=8, max_length=20, description="Phone number")
    company: str = Field(..., min_length=1, max_length=200, description="Company or brand name")
    type: str = Field(..., description="Type of solution needed")
    budget: str = Field(..., description="Estimated budget range")
    referral: str = Field(..., description="How they found us")
    message: str = Field(..., min_length=10, max_length=2000, description="Detailed message")
    file: Optional[str] = Field(None, description="Optional file attachment (base64 encoded)")


class ContactFormResponse(BaseModel):
    success: bool
    message: str
    request_id: Optional[uuid.UUID] = None
