from typing import List, Optional, Dict, Any
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError
from app.core.logging import logger
from app.db.redis import cache_get, cache_set, invalidate_home_cache
from app.models import Hero, Service, Project, Testimonial, Company, ContactRequest
from app.schemas.hero import HeroCreate, HeroUpdate, HeroResponse
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.schemas.testimonial import TestimonialCreate, TestimonialUpdate, TestimonialResponse
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from app.schemas.contact import ContactRequestCreate, ContactRequestResponse
from app.schemas.public import PublicHomeResponse


class ContentService:
    """Service for content management with Redis caching"""
    
    # Hero methods
    async def get_hero(self, db: AsyncSession) -> Optional[HeroResponse]:
        """Get the first hero (assuming single hero)"""
        try:
            result = await db.execute(select(Hero).limit(1))
            hero = result.scalar_one_or_none()
            return HeroResponse.from_orm(hero) if hero else None
        except SQLAlchemyError as e:
            logger.error(f"Error getting hero: {e}")
            return None
    
    async def create_hero(self, db: AsyncSession, hero_data: HeroCreate) -> Optional[HeroResponse]:
        """Create or update hero (single instance)"""
        try:
            # Delete existing hero first (single hero policy)
            await db.execute(delete(Hero))
            
            hero = Hero(**hero_data.dict())
            db.add(hero)
            await db.commit()
            await db.refresh(hero)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return HeroResponse.from_orm(hero)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error creating hero: {e}")
            return None
    
    async def update_hero(self, db: AsyncSession, hero_data: HeroUpdate) -> Optional[HeroResponse]:
        """Update existing hero"""
        try:
            result = await db.execute(select(Hero).limit(1))
            hero = result.scalar_one_or_none()
            
            if not hero:
                return None
            
            for key, value in hero_data.dict(exclude_unset=True).items():
                setattr(hero, key, value)
            
            await db.commit()
            await db.refresh(hero)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return HeroResponse.from_orm(hero)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error updating hero: {e}")
            return None
    
    # Service methods
    async def get_services(self, db: AsyncSession) -> List[ServiceResponse]:
        """Get all services"""
        try:
            result = await db.execute(select(Service))
            services = result.scalars().all()
            return [ServiceResponse.from_orm(service) for service in services]
        except SQLAlchemyError as e:
            logger.error(f"Error getting services: {e}")
            return []
    
    async def get_service(self, db: AsyncSession, service_id: UUID) -> Optional[ServiceResponse]:
        """Get service by ID"""
        try:
            result = await db.execute(select(Service).where(Service.id == service_id))
            service = result.scalar_one_or_none()
            return ServiceResponse.from_orm(service) if service else None
        except SQLAlchemyError as e:
            logger.error(f"Error getting service {service_id}: {e}")
            return None
    
    async def create_service(self, db: AsyncSession, service_data: ServiceCreate) -> Optional[ServiceResponse]:
        """Create new service"""
        try:
            service = Service(**service_data.dict())
            db.add(service)
            await db.commit()
            await db.refresh(service)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return ServiceResponse.from_orm(service)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error creating service: {e}")
            return None
    
    async def update_service(self, db: AsyncSession, service_id: UUID, service_data: ServiceUpdate) -> Optional[ServiceResponse]:
        """Update service"""
        try:
            result = await db.execute(select(Service).where(Service.id == service_id))
            service = result.scalar_one_or_none()
            
            if not service:
                return None
            
            for key, value in service_data.dict(exclude_unset=True).items():
                setattr(service, key, value)
            
            await db.commit()
            await db.refresh(service)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return ServiceResponse.from_orm(service)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error updating service {service_id}: {e}")
            return None
    
    async def delete_service(self, db: AsyncSession, service_id: UUID) -> bool:
        """Delete service"""
        try:
            result = await db.execute(delete(Service).where(Service.id == service_id))
            
            if result.rowcount == 0:
                return False
            
            await db.commit()
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return True
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error deleting service {service_id}: {e}")
            return False
    
    # Project methods
    async def get_projects(self, db: AsyncSession) -> List[ProjectResponse]:
        """Get all projects"""
        try:
            result = await db.execute(select(Project))
            projects = result.scalars().all()
            return [ProjectResponse.from_orm(project) for project in projects]
        except SQLAlchemyError as e:
            logger.error(f"Error getting projects: {e}")
            return []
    
    async def get_project(self, db: AsyncSession, project_id: UUID) -> Optional[ProjectResponse]:
        """Get project by ID"""
        try:
            result = await db.execute(select(Project).where(Project.id == project_id))
            project = result.scalar_one_or_none()
            return ProjectResponse.from_orm(project) if project else None
        except SQLAlchemyError as e:
            logger.error(f"Error getting project {project_id}: {e}")
            return None
    
    async def create_project(self, db: AsyncSession, project_data: ProjectCreate) -> Optional[ProjectResponse]:
        """Create new project"""
        try:
            project = Project(**project_data.dict())
            db.add(project)
            await db.commit()
            await db.refresh(project)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return ProjectResponse.from_orm(project)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error creating project: {e}")
            return None
    
    async def update_project(self, db: AsyncSession, project_id: UUID, project_data: ProjectUpdate) -> Optional[ProjectResponse]:
        """Update project"""
        try:
            result = await db.execute(select(Project).where(Project.id == project_id))
            project = result.scalar_one_or_none()
            
            if not project:
                return None
            
            for key, value in project_data.dict(exclude_unset=True).items():
                setattr(project, key, value)
            
            await db.commit()
            await db.refresh(project)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return ProjectResponse.from_orm(project)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error updating project {project_id}: {e}")
            return None
    
    async def delete_project(self, db: AsyncSession, project_id: UUID) -> bool:
        """Delete project"""
        try:
            result = await db.execute(delete(Project).where(Project.id == project_id))
            
            if result.rowcount == 0:
                return False
            
            await db.commit()
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return True
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error deleting project {project_id}: {e}")
            return False
    
    # Testimonial methods
    async def get_testimonials(self, db: AsyncSession) -> List[TestimonialResponse]:
        """Get all testimonials"""
        try:
            result = await db.execute(select(Testimonial))
            testimonials = result.scalars().all()
            return [TestimonialResponse.from_orm(testimonial) for testimonial in testimonials]
        except SQLAlchemyError as e:
            logger.error(f"Error getting testimonials: {e}")
            return []
    
    async def get_testimonial(self, db: AsyncSession, testimonial_id: UUID) -> Optional[TestimonialResponse]:
        """Get testimonial by ID"""
        try:
            result = await db.execute(select(Testimonial).where(Testimonial.id == testimonial_id))
            testimonial = result.scalar_one_or_none()
            return TestimonialResponse.from_orm(testimonial) if testimonial else None
        except SQLAlchemyError as e:
            logger.error(f"Error getting testimonial {testimonial_id}: {e}")
            return None
    
    async def create_testimonial(self, db: AsyncSession, testimonial_data: TestimonialCreate) -> Optional[TestimonialResponse]:
        """Create new testimonial"""
        try:
            testimonial = Testimonial(**testimonial_data.dict())
            db.add(testimonial)
            await db.commit()
            await db.refresh(testimonial)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return TestimonialResponse.from_orm(testimonial)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error creating testimonial: {e}")
            return None
    
    async def update_testimonial(self, db: AsyncSession, testimonial_id: UUID, testimonial_data: TestimonialUpdate) -> Optional[TestimonialResponse]:
        """Update testimonial"""
        try:
            result = await db.execute(select(Testimonial).where(Testimonial.id == testimonial_id))
            testimonial = result.scalar_one_or_none()
            
            if not testimonial:
                return None
            
            for key, value in testimonial_data.dict(exclude_unset=True).items():
                setattr(testimonial, key, value)
            
            await db.commit()
            await db.refresh(testimonial)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return TestimonialResponse.from_orm(testimonial)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error updating testimonial {testimonial_id}: {e}")
            return None
    
    async def delete_testimonial(self, db: AsyncSession, testimonial_id: UUID) -> bool:
        """Delete testimonial"""
        try:
            result = await db.execute(delete(Testimonial).where(Testimonial.id == testimonial_id))
            
            if result.rowcount == 0:
                return False
            
            await db.commit()
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return True
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error deleting testimonial {testimonial_id}: {e}")
            return False
    
    # Company methods
    async def get_company(self, db: AsyncSession) -> Optional[CompanyResponse]:
        """Get company info (assuming single company)"""
        try:
            result = await db.execute(select(Company).limit(1))
            company = result.scalar_one_or_none()
            return CompanyResponse.from_orm(company) if company else None
        except SQLAlchemyError as e:
            logger.error(f"Error getting company: {e}")
            return None
    
    async def create_company(self, db: AsyncSession, company_data: CompanyCreate) -> Optional[CompanyResponse]:
        """Create or update company (single instance)"""
        try:
            # Delete existing company first (single company policy)
            await db.execute(delete(Company))
            
            company = Company(**company_data.dict())
            db.add(company)
            await db.commit()
            await db.refresh(company)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return CompanyResponse.from_orm(company)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error creating company: {e}")
            return None
    
    async def update_company(self, db: AsyncSession, company_data: CompanyUpdate) -> Optional[CompanyResponse]:
        """Update existing company"""
        try:
            result = await db.execute(select(Company).limit(1))
            company = result.scalar_one_or_none()
            
            if not company:
                return None
            
            for key, value in company_data.dict(exclude_unset=True).items():
                setattr(company, key, value)
            
            await db.commit()
            await db.refresh(company)
            
            # Invalidate cache
            await invalidate_home_cache()
            
            return CompanyResponse.from_orm(company)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error updating company: {e}")
            return None
    
    # Contact Request methods
    async def get_contact_requests(self, db: AsyncSession) -> List[ContactRequestResponse]:
        """Get all contact requests"""
        try:
            result = await db.execute(select(ContactRequest).order_by(ContactRequest.timestamp.desc()))
            requests = result.scalars().all()
            return [ContactRequestResponse.from_orm(request) for request in requests]
        except SQLAlchemyError as e:
            logger.error(f"Error getting contact requests: {e}")
            return []
    
    async def create_contact_request(self, db: AsyncSession, contact_data: ContactRequestCreate, pdf_path: Optional[str] = None) -> Optional[ContactRequestResponse]:
        """Create new contact request"""
        try:
            request_data = contact_data.dict()
            if pdf_path:
                request_data['pdf_path'] = pdf_path
                
            contact_request = ContactRequest(**request_data)
            db.add(contact_request)
            await db.commit()
            await db.refresh(contact_request)
            
            return ContactRequestResponse.from_orm(contact_request)
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f"Error creating contact request: {e}")
            return None
    
    # Public home page
    async def get_public_home_data(self, db: AsyncSession) -> PublicHomeResponse:
        """Get complete home page data with caching"""
        try:
            # Try to get from cache first
            cached_data = await cache_get("home_cache")
            if cached_data:
                logger.info("Home data retrieved from cache")
                return PublicHomeResponse(**cached_data)
            
            # Get fresh data from database
            logger.info("Fetching fresh home data from database")
            hero = await self.get_hero(db)
            services = await self.get_services(db)
            projects = await self.get_projects(db)
            testimonials = await self.get_testimonials(db)
            company = await self.get_company(db)
            
            home_data = PublicHomeResponse(
                hero=hero,
                services=services,
                projects=projects,
                testimonials=testimonials,
                company=company
            )
            
            # Cache the data
            await cache_set("home_cache", home_data.dict())
            
            return home_data
            
        except Exception as e:
            logger.error(f"Error getting public home data: {e}")
            return PublicHomeResponse()


# Global content service instance
content_service = ContentService()
