"""
Custom tools for Sherlock Hooves to analyze horse racing data.
"""

from langchain.tools import Tool
from typing import List
import random

def get_horse_form(horse_name: str) -> str:
    """
    Get recent form for a horse (placeholder implementation).
    In production, this would query a real racing database.
    """
    # TODO: Replace with actual API call to racing data provider
    positions = random.sample(range(1, 13), 5)
    form = "-".join(map(str, positions))
    
    return f"""
    Recent form for {horse_name}:
    Last 5 races: {form}
    
    Note: This is placeholder data. Connect to a real racing API for actual statistics.
    """

def analyze_track_conditions(track_name: str, condition: str = "good") -> str:
    """
    Analyze how track conditions might affect race outcomes.
    """
    conditions_info = {
        "heavy": "Heavy tracks favor horses with stamina and a strong finishing kick.",
        "soft": "Soft tracks can advantage horses that race close to the pace.",
        "good": "Good tracks generally favor horses with natural speed.",
        "firm": "Firm tracks often produce faster times and suit front-runners."
    }
    
    info = conditions_info.get(condition.lower(), "Track condition not recognized.")
    
    return f"Track: {track_name}\nCondition: {condition}\nAnalysis: {info}"

def get_jockey_stats(jockey_name: str) -> str:
    """
    Get statistics for a jockey (placeholder implementation).
    """
    # TODO: Replace with actual API call
    win_rate = random.randint(15, 25)
    
    return f"""
    Jockey: {jockey_name}
    Win Rate: {win_rate}%
    
    Note: This is placeholder data. Connect to a real racing API for actual statistics.
    """

def racing_calculator(calculation: str) -> str:
    """
    Perform racing-related calculations (odds, returns, etc.).
    """
    try:
        # Simple calculator for betting returns
        # Format: "stake amount at odds"
        # Example: "10 at 5/1" or "20 at 3.5"
        
        parts = calculation.lower().split(" at ")
        if len(parts) == 2:
            stake = float(parts[0])
            odds_str = parts[1].strip()
            
            if "/" in odds_str:
                # Fractional odds
                num, den = odds_str.split("/")
                decimal_odds = (float(num) / float(den)) + 1
            else:
                # Decimal odds
                decimal_odds = float(odds_str)
            
            returns = stake * decimal_odds
            profit = returns - stake
            
            return f"Stake: ${stake:.2f}\nReturns: ${returns:.2f}\nProfit: ${profit:.2f}"
        
        return "Please use format: 'stake at odds' (e.g., '10 at 5/1' or '20 at 3.5')"
    
    except Exception as e:
        return f"Calculation error: {str(e)}"

def get_racing_tools() -> List[Tool]:
    """
    Return all available tools for the Sherlock Hooves agent.
    """
    return [
        Tool(
            name="Horse Form Lookup",
            func=get_horse_form,
            description="Get recent racing form and performance for a specific horse. Input should be the horse's name."
        ),
        Tool(
            name="Track Condition Analyzer",
            func=analyze_track_conditions,
            description="Analyze how track conditions affect race outcomes. Input should be 'track_name, condition' (e.g., 'Churchill Downs, heavy')."
        ),
        Tool(
            name="Jockey Statistics",
            func=get_jockey_stats,
            description="Get performance statistics for a jockey. Input should be the jockey's name."
        ),
        Tool(
            name="Racing Calculator",
            func=racing_calculator,
            description="Calculate betting returns and profits. Input format: 'stake at odds' (e.g., '10 at 5/1')."
        )
    ]
