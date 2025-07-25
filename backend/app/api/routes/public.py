from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.content_service import content_service
from app.services.email_service import email_service
from app.schemas.public import PublicHomeResponse
from app.schemas.contact import ContactFormSubmit, ContactFormResponse
from app.core.logging import logger

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint for Docker"""
    return {"status": "healthy", "service": "cloudfort-backend"}


@router.get("/home", response_model=PublicHomeResponse)
async def get_public_home_data(db: AsyncSession = Depends(get_db)):
    """Get complete public home page data (hero, services, projects, testimonials, company)"""
    try:
        home_data = await content_service.get_public_home_data(db)
        return home_data
    except Exception as e:
        logger.error(f"Error getting public home data: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving home page data"
        )


@router.post("/contact/submit", response_model=ContactFormResponse)
async def submit_contact_form_with_file(
    name: str = Form(..., min_length=1, max_length=200),
    email: str = Form(...),
    phone: str = Form(..., min_length=8, max_length=20),
    company: str = Form(..., min_length=1, max_length=200),
    type: str = Form(...),
    budget: str = Form(...),
    referral: str = Form(...),
    message: str = Form(..., min_length=10, max_length=2000),
    file: Optional[UploadFile] = File(None),
    db: AsyncSession = Depends(get_db)
):
    """Submit contact form with optional file attachment"""
    try:
        # Validate file if provided
        if file:
            # Check file size (5MB limit)
            if file.size and file.size > 5 * 1024 * 1024:
                raise HTTPException(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    detail="File size exceeds 5MB limit"
                )
            
            # Check file type
            allowed_types = [
                'application/pdf',
                'image/png', 
                'image/jpeg',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ]
            if file.content_type not in allowed_types:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="File type not allowed. Only PDF, PNG, JPG, and DOCX files are accepted."
                )
        
        # Create contact data object
        contact_data = ContactFormSubmit(
            name=name,
            email=email,
            phone=phone,
            company=company,
            type=type,
            budget=budget,
            referral=referral,
            message=message
        )
        
        # Save uploaded file if provided
        file_path = None
        if file:
            import os
            import aiofiles
            from pathlib import Path
            
            # Create uploads directory
            upload_dir = Path("uploads")
            upload_dir.mkdir(exist_ok=True)
            
            # Generate unique filename
            import time
            timestamp = int(time.time())
            file_extension = Path(file.filename).suffix if file.filename else ".tmp"
            file_path = upload_dir / f"contact_{timestamp}_{name.replace(' ', '_')}{file_extension}"
            
            # Save file
            async with aiofiles.open(file_path, 'wb') as f:
                content = await file.read()
                await f.write(content)
        
        # Generate PDF
        pdf_path = await email_service.generate_contact_pdf(contact_data)
        if not pdf_path:
            logger.warning("Failed to generate PDF for contact form")
        
        # Save to database
        contact_request = await content_service.create_contact_request(
            db, contact_data, pdf_path
        )
        
        if not contact_request:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error saving contact request"
            )
        
        # Send email notification to admin
        email_sent = await email_service.send_contact_notification(
            contact_data, pdf_path
        )
        
        if not email_sent:
            logger.warning(f"Failed to send email notification for contact request {contact_request.id}")
        
        return ContactFormResponse(
            success=True,
            message="Gracias por tu interés. Te responderemos pronto.",
            request_id=contact_request.id
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing contact form: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing contact form"
        )


@router.post("/contact", response_model=ContactFormResponse)
async def submit_contact_form(
    contact_data: ContactFormSubmit,
    db: AsyncSession = Depends(get_db)
):
    """Submit contact form (legacy endpoint without file support)"""
    try:
        # Generate PDF
        pdf_path = await email_service.generate_contact_pdf(contact_data)
        if not pdf_path:
            logger.warning("Failed to generate PDF for contact form")
        
        # Save to database
        contact_request = await content_service.create_contact_request(
            db, contact_data, pdf_path
        )
        
        if not contact_request:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error saving contact request"
            )
        
        # Send email notification to admin
        email_sent = await email_service.send_contact_notification(
            contact_data, pdf_path
        )
        
        if not email_sent:
            logger.warning(f"Failed to send email notification for contact request {contact_request.id}")
        
        return ContactFormResponse(
            success=True,
            message="Su solicitud ha sido enviada exitosamente. Nos pondremos en contacto pronto.",
            request_id=contact_request.id
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing contact form: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing contact form"
        )
