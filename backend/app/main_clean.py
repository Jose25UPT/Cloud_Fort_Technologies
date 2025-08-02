from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import sqlite3
import os
from datetime import datetime
from pathlib import Path

# Create FastAPI app
app = FastAPI(
    title="CloudFort Contact API",
    version="1.0.0",
    description="Simple contact form API"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:3001", "*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Initialize SQLite database
def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            company TEXT NOT NULL,
            type TEXT NOT NULL,
            budget TEXT NOT NULL,
            referral TEXT NOT NULL,
            message TEXT NOT NULL,
            file_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")

# Initialize database on startup
init_db()

# Create uploads directory
os.makedirs("uploads", exist_ok=True)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "CloudFort Contact API",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "submit_contact": "/api/public/contact/submit",
            "admin_contacts": "/api/admin/contacts",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "database": "sqlite",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/api/public/contact/submit")
async def submit_contact_form(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    company: str = Form(...),
    type: str = Form(...),
    budget: str = Form(...),
    referral: str = Form(...),
    message: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    """Submit contact form"""
    try:
        file_path = None
        
        # Handle file upload if provided
        if file and file.filename:
            # Validate file size (5MB limit)
            if file.size and file.size > 5 * 1024 * 1024:
                raise HTTPException(status_code=413, detail="El archivo es demasiado grande. Máximo 5MB.")
            
            # Validate file type
            allowed_types = [
                'application/pdf',
                'image/png', 
                'image/jpeg',
                'image/jpg',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ]
            if file.content_type not in allowed_types:
                raise HTTPException(status_code=400, detail="Tipo de archivo no permitido. Solo PDF, PNG, JPG y DOCX.")
            
            # Generate unique filename
            timestamp = int(datetime.now().timestamp())
            file_extension = Path(file.filename).suffix if file.filename else ".tmp"
            file_name = f"contact_{timestamp}_{name.replace(' ', '_')}{file_extension}"
            file_path = f"uploads/{file_name}"
            
            # Save file
            with open(file_path, 'wb') as f:
                content = await file.read()
                f.write(content)
        
        # Save to database
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO contacts (name, email, phone, company, type, budget, referral, message, file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, company, type, budget, referral, message, file_path))
        
        contact_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"✅ New contact received from {name} ({email})")
        
        return {
            "success": True,
            "message": "Gracias por tu interés. Te responderemos en menos de 24 horas.",
            "contact_id": contact_id
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error processing contact form: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor. Por favor intenta de nuevo.")

@app.get("/api/admin/contacts")
async def get_contacts():
    """Get all contacts (admin endpoint)"""
    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = cursor.fetchall()
        conn.close()
        
        # Convert to dict format
        contact_list = []
        for contact in contacts:
            contact_list.append({
                "id": contact[0],
                "name": contact[1],
                "email": contact[2],
                "phone": contact[3],
                "company": contact[4],
                "type": contact[5],
                "budget": contact[6],
                "referral": contact[7],
                "message": contact[8],
                "file_path": contact[9],
                "created_at": contact[10]
            })
        
        return {"contacts": contact_list}
        
    except Exception as e:
        print(f"❌ Error retrieving contacts: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener contactos")

@app.get("/api/admin/contacts/{contact_id}")
async def get_contact_details(contact_id: int):
    """Get specific contact details"""
    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        contact = cursor.fetchone()
        conn.close()
        
        if not contact:
            raise HTTPException(status_code=404, detail="Contacto no encontrado")
        
        return {
            "id": contact[0],
            "name": contact[1],
            "email": contact[2],
            "phone": contact[3],
            "company": contact[4],
            "type": contact[5],
            "budget": contact[6],
            "referral": contact[7],
            "message": contact[8],
            "file_path": contact[9],
            "created_at": contact[10]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error retrieving contact: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener contacto")

# Serve uploaded files
@app.get("/uploads/{filename}")
async def get_uploaded_file(filename: str):
    """Serve uploaded files"""
    file_path = f"uploads/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    
    from fastapi.responses import FileResponse
    return FileResponse(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
