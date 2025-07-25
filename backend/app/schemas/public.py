from typing import List, Optional
from pydantic import BaseModel
from .hero import HeroResponse
from .service import ServiceResponse
from .project import ProjectResponse
from .testimonial import TestimonialResponse
from .company import CompanyResponse


class PublicHomeResponse(BaseModel):
    """Complete public home page data"""
    hero: Optional[HeroResponse] = None
    services: List[ServiceResponse] = []
    projects: List[ProjectResponse] = []
    testimonials: List[TestimonialResponse] = []
    company: Optional[CompanyResponse] = None
    
    class Config:
        from_attributes = True


class ApiResponse(BaseModel):
    """Generic API response wrapper"""
    success: bool
    message: str
    data: Optional[dict] = None
