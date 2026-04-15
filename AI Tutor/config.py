from langchain_groq import ChatGroq
import os

def get_llm():
    """Initialize and return Groq LLM"""
    # Try to get from environment, fallback to hardcoded key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        api_key = "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"
    
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.7,
        max_tokens=1024
    )
