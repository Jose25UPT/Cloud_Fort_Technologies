import os
import aiofiles
import aiosmtplib
from datetime import datetime
from typing import Optional
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from app.config import settings
from app.core.logging import logger
from app.schemas.contact import ContactRequestCreate


class EmailService:
    def __init__(self):
        self.smtp_host = settings.SMTP_HOST
        self.smtp_port = settings.SMTP_PORT
        self.smtp_user = settings.SMTP_USER
        self.smtp_password = settings.SMTP_PASSWORD
        self.smtp_tls = settings.SMTP_TLS
        self.admin_email = settings.ADMIN_EMAIL
    
    async def send_email(
        self,
        to_email: str,
        subject: str,
        body: str,
        is_html: bool = False,
        attachment_path: Optional[str] = None
    ) -> bool:
        """Send email with optional attachment"""
        try:
            # Development mode - just log the email instead of sending
            if not self.smtp_password or self.smtp_password == "your_app_password_here":
                logger.info(f"📧 [DEV MODE] Email would be sent to: {to_email}")
                logger.info(f"📧 [DEV MODE] Subject: {subject}")
                logger.info(f"📧 [DEV MODE] Body: {body[:200]}...")
                if attachment_path:
                    logger.info(f"📧 [DEV MODE] Attachment: {attachment_path}")
                return True
            
            # Production mode - actually send email
            # Create message
            message = MIMEMultipart()
            message["From"] = self.smtp_user
            message["To"] = to_email
            message["Subject"] = subject
            
            # Add body
            if is_html:
                message.attach(MIMEText(body, "html"))
            else:
                message.attach(MIMEText(body, "plain"))
            
            # Add attachment if provided
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                filename = os.path.basename(attachment_path)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                message.attach(part)
            
            # Send email
            async with aiosmtplib.SMTP(
                hostname=self.smtp_host,
                port=self.smtp_port,
                use_tls=self.smtp_tls
            ) as server:
                if self.smtp_user and self.smtp_password:
                    await server.login(self.smtp_user, self.smtp_password)
                
                await server.send_message(message)
            
            logger.info(f"Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {e}")
            return False
    
    async def generate_contact_pdf(
        self,
        contact_data: ContactRequestCreate,
        output_dir: str = "uploads/pdfs"
    ) -> Optional[str]:
        """Generate PDF from contact form data"""
        try:
            # Create output directory if it doesn't exist
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"contact_request_{timestamp}.pdf"
            filepath = os.path.join(output_dir, filename)
            
            # Create PDF document
            doc = SimpleDocTemplate(filepath, pagesize=A4)
            styles = getSampleStyleSheet()
            
            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=20,
                spaceAfter=30,
                textColor=colors.HexColor('#2C3E50')
            )
            
            label_style = ParagraphStyle(
                'Label',
                parent=styles['Normal'],
                fontSize=12,
                textColor=colors.HexColor('#34495E'),
                fontName='Helvetica-Bold',
                spaceBefore=10,
                spaceAfter=5
            )
            
            value_style = ParagraphStyle(
                'Value',
                parent=styles['Normal'],
                fontSize=11,
                textColor=colors.HexColor('#2C3E50'),
                leftIndent=20,
                spaceAfter=15
            )
            
            # Build PDF content
            story = []
            
            # Title
            story.append(Paragraph("Cloud Fort Technologies - Solicitud de Contacto", title_style))
            story.append(Spacer(1, 20))
            
            # Contact information
            story.append(Paragraph("Información del Cliente", styles['Heading2']))
            story.append(Spacer(1, 10))
            
            story.append(Paragraph("Nombre:", label_style))
            story.append(Paragraph(contact_data.name, value_style))
            
            story.append(Paragraph("Correo Electrónico:", label_style))
            story.append(Paragraph(str(contact_data.email), value_style))
            
            if contact_data.company:
                story.append(Paragraph("Empresa:", label_style))
                story.append(Paragraph(contact_data.company, value_style))
            
            story.append(Paragraph("Teléfono:", label_style))
            story.append(Paragraph(contact_data.phone, value_style))
            
            story.append(Paragraph("Tipo de Servicio:", label_style))
            story.append(Paragraph(contact_data.type, value_style))
            
            story.append(Paragraph("Presupuesto:", label_style))
            story.append(Paragraph(contact_data.budget, value_style))
            
            story.append(Paragraph("Mensaje:", label_style))
            story.append(Paragraph(contact_data.message, value_style))
            
            # Footer with timestamp
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
                styles['Normal']
            ))
            
            # Build PDF
            doc.build(story)
            
            logger.info(f"PDF generated: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Failed to generate PDF: {e}")
            return None
    
    async def send_contact_notification(
        self,
        contact_data: ContactRequestCreate,
        pdf_path: Optional[str] = None
    ) -> bool:
        """Send contact form notification to admin"""
        try:
            subject = f"Nueva Solicitud de Contacto - {contact_data.name}"
            
            body = f"""
            Has recibido una nueva solicitud de contacto desde el sitio web de Cloud Fort Technologies.
            
            Detalles del contacto:
            - Nombre: {contact_data.name}
            - Correo: {contact_data.email}
            - Teléfono: {contact_data.phone}
            - Empresa: {contact_data.company}
            - Tipo de Servicio: {contact_data.type}
            - Presupuesto: {contact_data.budget}
            - Referencia: {contact_data.referral}
            
            Mensaje:
            {contact_data.message}
            
            Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
            
            ---
            Cloud Fort Technologies
            Sistema de Gestión de Contactos
            """
            
            return await self.send_email(
                to_email=self.admin_email,
                subject=subject,
                body=body,
                attachment_path=pdf_path
            )
            
        except Exception as e:
            logger.error(f"Failed to send contact notification: {e}")
            return False


# Global email service instance
email_service = EmailService()
