from fastapi import FastAPI, Form, File, UploadFile, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
import sqlite3
import os
from datetime import datetime, timedelta
from pathlib import Path
import jwt
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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

# Authentication configuration
SECRET_KEY = os.getenv("SECRET_KEY", "CloudFort_Technologies_2025_Ultra_Secure_JWT_Key_For_Admin_Access")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Admin credentials (loaded from environment variables)
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "cloudfort_admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "CloudFort2025AdminSecure")

security = HTTPBearer()

# Pydantic models for authentication
class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

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

# Authentication functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token"""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return username
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_current_user(username: str = Depends(verify_token)):
    """Get current authenticated user"""
    if username != ADMIN_USERNAME:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username

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

# Authentication endpoints
@app.post("/api/auth/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """Login endpoint"""
    if request.username != ADMIN_USERNAME or request.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": request.username}, expires_delta=access_token_expires
    )
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

@app.get("/api/auth/verify")
async def verify_token_endpoint(current_user: str = Depends(get_current_user)):
    """Verify token endpoint"""
    return {"username": current_user, "is_admin": True}

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
async def get_contacts(current_user: str = Depends(get_current_user)):
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
async def get_contact_details(contact_id: int, current_user: str = Depends(get_current_user)):
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
