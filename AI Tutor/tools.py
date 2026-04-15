from langchain_core.tools import tool
from typing import Dict, List
import json

@tool
def analyze_sentence(sentence: str) -> str:
    """Analyze a sentence for grammar mistakes and provide corrections.
    
    Args:
        sentence: The user's sentence to analyze
        
    Returns:
        JSON string with mistake, correction, and explanation
    """
    # This tool will be called by the agent to structure grammar feedback
    return json.dumps({
        "action": "analyze",
        "sentence": sentence
    })

@tool
def start_roleplay(scenario: str) -> str:
    """Start a roleplay scenario for language practice.
    
    Args:
        scenario: Type of roleplay (interview, travel, restaurant, casual)
        
    Returns:
        Roleplay context and initial prompt
    """
    scenarios = {
        "interview": "You are a hiring manager conducting a job interview. Ask professional questions.",
        "travel": "You are a hotel receptionist helping a guest check in. Be helpful and friendly.",
        "restaurant": "You are a waiter taking orders at a restaurant. Be polite and attentive.",
        "casual": "You are a friend having a casual conversation. Be relaxed and natural."
    }
    
    context = scenarios.get(scenario.lower(), scenarios["casual"])
    
    return json.dumps({
        "action": "roleplay",
        "scenario": scenario,
        "context": context
    })

@tool
def generate_quiz(topic: str, difficulty: str = "medium") -> str:
    """Generate a language quiz with multiple questions.
    
    Args:
        topic: Quiz topic (grammar, vocabulary, tenses, etc.)
        difficulty: easy, medium, or hard
        
    Returns:
        JSON with quiz questions
    """
    return json.dumps({
        "action": "quiz",
        "topic": topic,
        "difficulty": difficulty,
        "num_questions": 5
    })

@tool
def track_progress(mistake_type: str, user_sentence: str, correct_sentence: str) -> str:
    """Track user's mistakes and learning progress.
    
    Args:
        mistake_type: Type of mistake (grammar, vocabulary, tense, etc.)
        user_sentence: The incorrect sentence
        correct_sentence: The corrected sentence
        
    Returns:
        Progress tracking confirmation
    """
    return json.dumps({
        "action": "track",
        "mistake_type": mistake_type,
        "logged": True
    })

def get_all_tools():
    """Return all available tools for the agent"""
    return [
        analyze_sentence,
        start_roleplay,
        generate_quiz,
        track_progress
    ]
