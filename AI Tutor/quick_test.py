import os
os.environ['GROQ_API_KEY'] = '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'

from agent import get_agent

print("Quick test...")
agent = get_agent()

# Test Quiz
print("\nTesting Quiz:")
try:
    response = agent.chat("Give me a quiz", thread_id="test", mode="Quiz")
    print(f"Success! Response: {response['content'][:200]}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

# Test Roleplay
print("\nTesting Roleplay:")
try:
    response = agent.chat("Let's practice interview", thread_id="test2", mode="Roleplay")
    print(f"Success! Response: {response['content'][:200]}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
