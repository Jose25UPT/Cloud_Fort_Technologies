#!/usr/bin/env python3

import os
import sys
import uvicorn
from dotenv import load_dotenv

# Force reload environment
load_dotenv('.env', override=True)

print("🚀 Starting CloudFort Backend...")
print(f"DATABASE_TYPE: {os.getenv('DATABASE_TYPE')}")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )