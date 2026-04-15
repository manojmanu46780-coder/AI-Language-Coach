import os
os.environ['GROQ_API_KEY'] = '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'

from agent import get_agent

agent = get_agent()

print("Testing Quiz Output Format:")
print("=" * 60)

response = agent.chat("Give me a grammar quiz", thread_id="test", mode="Quiz")

print("\nRaw Response:")
print(response['content'])
print("\n" + "=" * 60)

# Check if it has the expected format
content = response['content']
if "1." in content and "A)" in content:
    print("\n✓ Quiz format detected!")
else:
    print("\n✗ Quiz format NOT detected")
    print("Response doesn't have numbered questions with options")
