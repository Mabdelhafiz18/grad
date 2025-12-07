"""
Match Decision Routes

This module contains endpoints for match decision analysis:
- Offside detection
- Foul analysis
- Goal prediction (xG)
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import json
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


@router.get("/offside", response_model=List[Dict[str, Any]])
async def get_offside():
    """
    Get offside detection data
    
    Returns a list of offside events detected during the match.
    Each event includes information about the player, position, timestamp,
    and whether the offside was correctly called.
    
    Returns:
        List[Dict]: List of offside events with keys:
            - player_id (int): Player number who was offside
            - timestamp (float): Time in seconds when offside occurred
            - x (float): X coordinate of offside position
            - y (float): Y coordinate of offside position
            - is_correct (bool): Whether the offside call was correct
    
    Example Response:
        [
            {
                "player_id": 9,
                "timestamp": 245.3,
                "x": 85.2,
                "y": 45.0,
                "is_correct": true
            }
        ]
    """
    return load_json_file("offside.json")


@router.get("/fouls", response_model=List[Dict[str, Any]])
async def get_fouls():
    """
    Get foul analysis data
    
    Returns a list of foul events detected during the match.
    Each event includes information about the players involved, location,
    severity, and whether the foul call was correct.
    
    Returns:
        List[Dict]: List of foul events with keys:
            - foul_id (int): Unique identifier for the foul
            - player_committed (int): Player number who committed the foul
            - player_suffered (int): Player number who suffered the foul
            - timestamp (float): Time in seconds when foul occurred
            - x (float): X coordinate of foul location
            - y (float): Y coordinate of foul location
            - severity (str): Severity level (e.g., "minor", "major", "card")
            - is_correct (bool): Whether the foul call was correct
    
    Example Response:
        [
            {
                "foul_id": 1,
                "player_committed": 5,
                "player_suffered": 10,
                "timestamp": 180.5,
                "x": 50.0,
                "y": 30.0,
                "severity": "minor",
                "is_correct": true
            }
        ]
    """
    return load_json_file("fouls.json")


@router.get("/goal-prediction", response_model=Dict[str, Any])
async def get_goal_prediction():
    """
    Get goal prediction (xG) data
    
    Returns expected goals (xG) prediction for a shot event.
    xG is a metric that quantifies the quality of a scoring chance,
    representing the probability that a shot will result in a goal.
    
    Returns:
        Dict: Goal prediction data with keys:
            - shot_x (float): X coordinate of shot location (0-100)
            - shot_y (float): Y coordinate of shot location (0-100)
            - xG (float): Expected goals value (0.0-1.0)
            - is_goal (bool): Whether the shot resulted in a goal
    
    Example Response:
        {
            "shot_x": 30,
            "shot_y": 70,
            "xG": 0.45,
            "is_goal": false
        }
    """
    return load_json_file("goal_prediction.json")

