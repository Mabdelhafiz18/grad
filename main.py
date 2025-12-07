"""
FastAPI Backend for Football Analytics Web App

This is the main entry point for the FastAPI application.
Run with: uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tactical, decisions, upload

# Initialize FastAPI app
app = FastAPI(
    title="Football Analytics API",
    description="Backend API for Football Analytics Web App with tactical analysis and match decision endpoints",
    version="1.0.0"
)

# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tactical.router, prefix="/api/tactical", tags=["Tactical Analysis"])
app.include_router(decisions.router, prefix="/api/decisions", tags=["Match Decisions"])
app.include_router(upload.router, prefix="/api", tags=["Upload"])


@app.get("/")
async def root():
    """
    Root endpoint - API health check
    
    Returns:
        dict: Welcome message and API information
    """
    return {
        "message": "Welcome to Football Analytics API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Returns:
        dict: API health status
    """
    return {"status": "healthy"}

