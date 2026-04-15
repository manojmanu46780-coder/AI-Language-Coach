"""
Test roleplay and quiz functionality
"""
import os
os.environ['GROQ_API_KEY'] = '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'

from agent import get_agent

print("Testing Roleplay and Quiz Modes")
print("=" * 60)

agent = get_agent()

# Test Roleplay - Interview
print("\n1. ROLEPLAY TEST - Job Interview:")
print("-" * 60)
response = agent.chat("Let's practice a job interview", thread_id="roleplay1", mode="Roleplay")
print(f"Response: {response['content'][:300]}...")

# Test Roleplay - Restaurant
print("\n2. ROLEPLAY TEST - Restaurant:")
print("-" * 60)
response = agent.chat("I want to practice ordering at a restaurant", thread_id="roleplay2", mode="Roleplay")
print(f"Response: {response['content'][:300]}...")

# Test Quiz
print("\n3. QUIZ TEST:")
print("-" * 60)
response = agent.chat("Give me a grammar quiz", thread_id="quiz1", mode="Quiz")
print(f"Response: {response['content'][:400]}...")

# Test Quiz with specific topic
print("\n4. QUIZ TEST - Past Tense:")
print("-" * 60)
response = agent.chat("Can I have a quiz about past tense?", thread_id="quiz2", mode="Quiz")
print(f"Response: {response['content'][:400]}...")

print("\n" + "=" * 60)
print("All tests completed!")
