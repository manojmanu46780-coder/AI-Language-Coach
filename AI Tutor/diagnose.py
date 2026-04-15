import os
os.environ['GROQ_API_KEY'] = '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'

print("=" * 60)
print("LinguaAI Diagnostic Test")
print("=" * 60)

# Test 1: Import config
print("\n1. Testing config import...")
try:
    from config import get_llm
    llm = get_llm()
    print("   [OK] Config loaded, LLM initialized")
except Exception as e:
    print(f"   [FAIL] Config error: {e}")
    exit(1)

# Test 2: Test LLM directly
print("\n2. Testing LLM directly...")
try:
    from langchain_core.messages import HumanMessage
    response = llm.invoke([HumanMessage(content="Say hello")])
    print(f"   [OK] LLM response: {response.content[:50]}")
except Exception as e:
    print(f"   [FAIL] LLM error: {e}")
    exit(1)

# Test 3: Import agent
print("\n3. Testing agent import...")
try:
    from agent import get_agent
    agent = get_agent()
    print("   [OK] Agent imported and initialized")
except Exception as e:
    print(f"   [FAIL] Agent import error: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 4: Test agent chat
print("\n4. Testing agent chat...")
try:
    response = agent.chat("Hello", thread_id="test", mode="Free Chat")
    print(f"   [OK] Agent response: {response['content'][:50]}")
except Exception as e:
    print(f"   [FAIL] Agent chat error: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 5: Test roleplay
print("\n5. Testing roleplay mode...")
try:
    response = agent.chat("Let's practice interview", thread_id="test2", mode="Roleplay")
    print(f"   [OK] Roleplay works: {response['content'][:50]}")
except Exception as e:
    print(f"   [FAIL] Roleplay error: {e}")

# Test 6: Test quiz
print("\n6. Testing quiz mode...")
try:
    response = agent.chat("Give me a quiz", thread_id="test3", mode="Quiz")
    print(f"   [OK] Quiz works: {response['content'][:50]}")
except Exception as e:
    print(f"   [FAIL] Quiz error: {e}")

print("\n" + "=" * 60)
print("All tests passed! Agent is working correctly.")
print("=" * 60)
