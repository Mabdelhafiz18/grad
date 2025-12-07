"""
Match Decision Schemas

Pydantic models for match decision data validation and documentation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class SeverityLevel(str, Enum):
    """Enum for foul severity levels"""
    MINOR = "minor"
    MAJOR = "major"
    YELLOW_CARD = "yellow_card"
    RED_CARD = "red_card"


class OffsideEvent(BaseModel):
    """Schema for an offside event"""
    player_id: int = Field(..., description="Player number who was offside")
    timestamp: float = Field(..., description="Time in seconds when offside occurred", ge=0)
    x: float = Field(..., description="X coordinate of offside position", ge=0, le=100)
    y: float = Field(..., description="Y coordinate of offside position", ge=0, le=100)
    is_correct: bool = Field(..., description="Whether the offside call was correct")
    
    class Config:
        json_schema_extra = {
            "example": {
                "player_id": 9,
                "timestamp": 245.3,
                "x": 85.2,
                "y": 45.0,
                "is_correct": True
            }
        }


class FoulEvent(BaseModel):
    """Schema for a foul event"""
    foul_id: int = Field(..., description="Unique identifier for the foul")
    player_committed: int = Field(..., description="Player number who committed the foul")
    player_suffered: int = Field(..., description="Player number who suffered the foul")
    timestamp: float = Field(..., description="Time in seconds when foul occurred", ge=0)
    x: float = Field(..., description="X coordinate of foul location", ge=0, le=100)
    y: float = Field(..., description="Y coordinate of foul location", ge=0, le=100)
    severity: str = Field(..., description="Severity level (minor, major, yellow_card, red_card)")
    is_correct: bool = Field(..., description="Whether the foul call was correct")
    
    class Config:
        json_schema_extra = {
            "example": {
                "foul_id": 1,
                "player_committed": 5,
                "player_suffered": 10,
                "timestamp": 180.5,
                "x": 50.0,
                "y": 30.0,
                "severity": "minor",
                "is_correct": True
            }
        }


class GoalPrediction(BaseModel):
    """Schema for goal prediction (xG) data"""
    shot_x: float = Field(..., description="X coordinate of shot location (0-100)", ge=0, le=100)
    shot_y: float = Field(..., description="Y coordinate of shot location (0-100)", ge=0, le=100)
    xG: float = Field(..., description="Expected goals value (0.0-1.0)", ge=0.0, le=1.0)
    is_goal: bool = Field(..., description="Whether the shot resulted in a goal")
    
    class Config:
        json_schema_extra = {
            "example": {
                "shot_x": 30,
                "shot_y": 70,
                "xG": 0.45,
                "is_goal": False
            }
        }

