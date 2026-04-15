"""
Test script for LinguaAI agent
"""
import os
os.environ['GROQ_API_KEY'] = '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'

from agent import get_agent

print("Testing LinguaAI Agent...")
print("=" * 50)

agent = get_agent()

# Test 1: Free Chat
print("\n1. Testing Free Chat Mode:")
response = agent.chat("I go to school yesterday", thread_id="test1", mode="Free Chat")
print(f"Content: {response['content']}")
print(f"Feedback: {response['feedback']}")

# Test 2: Roleplay
print("\n2. Testing Roleplay Mode:")
response = agent.chat("Let's practice a job interview", thread_id="test2", mode="Roleplay")
print(f"Content: {response['content']}")

# Test 3: Quiz
print("\n3. Testing Quiz Mode:")
response = agent.chat("Give me a grammar quiz", thread_id="test3", mode="Quiz")
print(f"Content: {response['content']}")

print("\n" + "=" * 50)
print("Tests completed!")
