"""
Tactical Analysis Schemas

Pydantic models for tactical analysis data validation and documentation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class HeatmapPoint(BaseModel):
    """Schema for a single heatmap data point"""
    x: int = Field(..., description="X coordinate on the pitch (0-100)", ge=0, le=100)
    y: int = Field(..., description="Y coordinate on the pitch (0-100)", ge=0, le=100)
    intensity: float = Field(..., description="Intensity value (0.0-1.0)", ge=0.0, le=1.0)
    
    class Config:
        json_schema_extra = {
            "example": {
                "x": 20,
                "y": 50,
                "intensity": 0.7
            }
        }


class PassConnection(BaseModel):
    """Schema for a pass connection between two players"""
    from_player: int = Field(..., alias="from", description="Source player number")
    to_player: int = Field(..., alias="to", description="Target player number")
    count: int = Field(..., description="Number of passes between these players", ge=0)
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "from": 8,
                "to": 10,
                "count": 12
            }
        }


class PassNetwork(BaseModel):
    """Schema for pass network data"""
    passes: List[PassConnection] = Field(..., description="List of pass connections")
    
    class Config:
        json_schema_extra = {
            "example": {
                "passes": [
                    {"from": 8, "to": 10, "count": 12},
                    {"from": 6, "to": 22, "count": 5}
                ]
            }
        }


class TrackingPoint(BaseModel):
    """Schema for a single player tracking data point"""
    player_id: int = Field(..., description="Player number")
    timestamp: float = Field(..., description="Time in seconds", ge=0)
    x: float = Field(..., description="X coordinate on the pitch", ge=0, le=100)
    y: float = Field(..., description="Y coordinate on the pitch", ge=0, le=100)
    speed: Optional[float] = Field(None, description="Player speed in m/s", ge=0)
    
    class Config:
        json_schema_extra = {
            "example": {
                "player_id": 10,
                "timestamp": 120.5,
                "x": 45.2,
                "y": 30.8,
                "speed": 5.2
            }
        }

