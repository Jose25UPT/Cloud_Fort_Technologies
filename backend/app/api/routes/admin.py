from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.content_service import content_service
from app.api.deps.dependencies import get_current_admin
from app.schemas.auth import AdminUser
from app.schemas.hero import HeroResponse, HeroCreate, HeroUpdate
from app.schemas.service import ServiceResponse, ServiceCreate, ServiceUpdate
from app.schemas.project import ProjectResponse, ProjectCreate, ProjectUpdate
from app.schemas.testimonial import TestimonialResponse, TestimonialCreate, TestimonialUpdate
from app.schemas.company import CompanyResponse, CompanyCreate, CompanyUpdate
from app.schemas.contact import ContactRequestResponse
from app.core.logging import logger

router = APIRouter()


# Hero endpoints
@router.get("/hero", response_model=HeroResponse)
async def get_hero(
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get hero section data"""
    hero = await content_service.get_hero(db)
    if not hero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hero section not found"
        )
    return hero


@router.put("/hero", response_model=HeroResponse)
async def update_hero(
    hero_data: HeroUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Update hero section"""
    hero = await content_service.update_hero(db, hero_data)
    if not hero:
        # If no hero exists, create one
        create_data = HeroCreate(**hero_data.dict(exclude_unset=True))
        hero = await content_service.create_hero(db, create_data)
        if not hero:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error creating/updating hero"
            )
    return hero


# Services endpoints
@router.get("/services", response_model=List[ServiceResponse])
async def get_services(
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get all services"""
    return await content_service.get_services(db)


@router.post("/services", response_model=ServiceResponse)
async def create_service(
    service_data: ServiceCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Create new service"""
    service = await content_service.create_service(db, service_data)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating service"
        )
    return service


@router.get("/services/{service_id}", response_model=ServiceResponse)
async def get_service(
    service_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get service by ID"""
    service = await content_service.get_service(db, service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    return service


@router.put("/services/{service_id}", response_model=ServiceResponse)
async def update_service(
    service_id: UUID,
    service_data: ServiceUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Update service"""
    service = await content_service.update_service(db, service_id, service_data)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    return service


@router.delete("/services/{service_id}")
async def delete_service(
    service_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Delete service"""
    deleted = await content_service.delete_service(db, service_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    return {"message": "Service deleted successfully"}


# Projects endpoints
@router.get("/projects", response_model=List[ProjectResponse])
async def get_projects(
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get all projects"""
    return await content_service.get_projects(db)


@router.post("/projects", response_model=ProjectResponse)
async def create_project(
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Create new project"""
    project = await content_service.create_project(db, project_data)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating project"
        )
    return project


@router.get("/projects/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get project by ID"""
    project = await content_service.get_project(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project


@router.put("/projects/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: UUID,
    project_data: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Update project"""
    project = await content_service.update_project(db, project_id, project_data)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return project


@router.delete("/projects/{project_id}")
async def delete_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Delete project"""
    deleted = await content_service.delete_project(db, project_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    return {"message": "Project deleted successfully"}


# Testimonials endpoints
@router.get("/testimonials", response_model=List[TestimonialResponse])
async def get_testimonials(
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get all testimonials"""
    return await content_service.get_testimonials(db)


@router.post("/testimonials", response_model=TestimonialResponse)
async def create_testimonial(
    testimonial_data: TestimonialCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Create new testimonial"""
    testimonial = await content_service.create_testimonial(db, testimonial_data)
    if not testimonial:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating testimonial"
        )
    return testimonial


@router.get("/testimonials/{testimonial_id}", response_model=TestimonialResponse)
async def get_testimonial(
    testimonial_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get testimonial by ID"""
    testimonial = await content_service.get_testimonial(db, testimonial_id)
    if not testimonial:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Testimonial not found"
        )
    return testimonial


@router.put("/testimonials/{testimonial_id}", response_model=TestimonialResponse)
async def update_testimonial(
    testimonial_id: UUID,
    testimonial_data: TestimonialUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Update testimonial"""
    testimonial = await content_service.update_testimonial(db, testimonial_id, testimonial_data)
    if not testimonial:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Testimonial not found"
        )
    return testimonial


@router.delete("/testimonials/{testimonial_id}")
async def delete_testimonial(
    testimonial_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Delete testimonial"""
    deleted = await content_service.delete_testimonial(db, testimonial_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Testimonial not found"
        )
    return {"message": "Testimonial deleted successfully"}


# Company endpoints
@router.get("/company", response_model=CompanyResponse)
async def get_company(
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get company information"""
    company = await content_service.get_company(db)
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company information not found"
        )
    return company


@router.put("/company", response_model=CompanyResponse)
async def update_company(
    company_data: CompanyUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Update company information"""
    company = await content_service.update_company(db, company_data)
    if not company:
        # If no company exists, create one
        create_data = CompanyCreate(**company_data.dict(exclude_unset=True))
        company = await content_service.create_company(db, create_data)
        if not company:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error creating/updating company information"
            )
    return company


# Contact requests endpoints
@router.get("/requests", response_model=List[ContactRequestResponse])
async def get_contact_requests(
    db: AsyncSession = Depends(get_db),
    current_admin: AdminUser = Depends(get_current_admin)
):
    """Get all contact requests"""
    return await content_service.get_contact_requests(db)
