"""
Tactical Analysis Routes

This module contains endpoints for tactical analysis features:
- Heatmap visualization
- Pass network analysis
- Player tracking data
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import json
import os
from pathlib import Path

router = APIRouter()

# Get the base directory (parent of routes folder)
BASE_DIR = Path(__file__).parent.parent
DUMMY_DATA_DIR = BASE_DIR / "dummy_data"


def load_json_file(filename: str) -> Any:
    """
    Helper function to load JSON data from dummy_data directory
    
    Args:
        filename: Name of the JSON file to load
        
    Returns:
        Parsed JSON data
        
    Raises:
        HTTPException: If file is not found or cannot be parsed
    """
    file_path = DUMMY_DATA_DIR / filename
    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Data file {filename} not found"
        )
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail=f"Error parsing {filename}"
        )


@router.get("/heatmap", response_model=List[Dict[str, Any]])
async def get_heatmap():
    """
    Get heatmap data for player position visualization
    
    Returns a list of heatmap points with x, y coordinates and intensity values.
    This data can be used to visualize where players spend most of their time on the pitch.
    
    Returns:
        List[Dict]: List of heatmap points with keys:
            - x (int): X coordinate on the pitch (0-100)
            - y (int): Y coordinate on the pitch (0-100)
            - intensity (float): Intensity value (0.0-1.0)
    
    Example Response:
        [
            {"x": 20, "y": 50, "intensity": 0.7},
            {"x": 40, "y": 30, "intensity": 0.3}
        ]
    """
    return load_json_file("heatmap.json")


@router.get("/pass-network", response_model=Dict[str, Any])
async def get_pass_network():
    """
    Get pass network data showing passing patterns between players
    
    Returns pass network data that visualizes the passing connections
    between players. Each pass connection includes the source player,
    target player, and the number of passes.
    
    Returns:
        Dict: Pass network data with keys:
            - passes (List[Dict]): List of pass connections with:
                - from (int): Source player number
                - to (int): Target player number
                - count (int): Number of passes between these players
    
    Example Response:
        {
            "passes": [
                {"from": 8, "to": 10, "count": 12},
                {"from": 6, "to": 22, "count": 5}
            ]
        }
    """
    return load_json_file("pass_network.json")


@router.get("/tracking", response_model=List[Dict[str, Any]])
async def get_tracking():
    """
    Get player tracking data for movement analysis
    
    Returns tracking data showing player positions and movements over time.
    This data can be used for analyzing player movement patterns, speed,
    and positioning throughout the match.
    
    Returns:
        List[Dict]: List of tracking data points with player information,
        timestamps, positions, and movement metrics
    
    Example Response:
        [
            {
                "player_id": 10,
                "timestamp": 120.5,
                "x": 45.2,
                "y": 30.8,
                "speed": 5.2
            }
        ]
    """
    return load_json_file("tracking.json")

