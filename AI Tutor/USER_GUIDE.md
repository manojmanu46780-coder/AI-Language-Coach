# LinguaAI - Complete User Guide

## How to Start

1. Double-click `start.bat`
2. Wait for "Running on http://127.0.0.1:5000"
3. Open browser: http://localhost:5000

## How to Use Each Mode

### FREE CHAT MODE
Just type naturally and get corrections:

Examples:
- "I go to school yesterday"
- "She don't like pizza"
- "We was playing football"

You'll get:
- \u274c Mistake: What you said wrong
- \u2705 Correction: The right way
- \ud83d\udca1 Explanation: Why and how to improve

### ROLEPLAY MODE
Click "Roleplay" in sidebar, then type what scenario you want:

**Job Interview:**
- "Let's practice a job interview"
- "I want to practice for an interview"
- AI becomes: Hiring manager asking questions

**Restaurant:**
- "Let's practice at a restaurant"
- "I want to order food"
- AI becomes: Waiter taking your order

**Travel/Hotel:**
- "Let's practice checking into a hotel"
- "I want to practice travel English"
- AI becomes: Hotel receptionist

**Casual Conversation:**
- "Let's have a casual chat"
- "Can we talk like friends?"
- AI becomes: Friendly person

The AI will STAY IN CHARACTER and respond naturally while still correcting your grammar.

### QUIZ MODE
Click "Quiz" in sidebar, then ask for a quiz:

Examples:
- "Give me a grammar quiz"
- "I want a quiz about past tense"
- "Test me on vocabulary"
- "Can I have 5 questions?"

You'll get 3-5 numbered questions. Answer them, and the AI will provide detailed feedback.

## Tips

1. **Mode Switching**: Click the mode buttons in the sidebar to switch
2. **New Session**: Click "New Session" to start fresh
3. **Progress**: Watch your stats update (Messages, Mistakes, Weak Area)
4. **Memory**: The AI remembers your conversation in each session

## Examples of Full Conversations

### Roleplay Example:
```
You: "Let's practice a job interview"
AI: "Welcome! I'm the hiring manager. Tell me about yourself."
You: "I work as a developer for 5 years"
AI: "That's great experience! 
     \u274c Mistake: 'I work'
     \u2705 Correction: 'I have worked' or 'I've been working'
     \ud83d\udca1 Explanation: Use present perfect for experiences up to now.
     
     So, what technologies do you specialize in?"
```

### Quiz Example:
```
You: "Give me a grammar quiz"
AI: "Here's your quiz:
     1. I ___ to school yesterday (go/went/gone)
     2. She ___ pizza (don't like/doesn't like)
     3. They ___ playing now (is/are/am)"
     
You: "1. went, 2. doesn't like, 3. are"
AI: "Excellent! All correct! 
     \u2705 Question 1: Correct - 'went' is past tense
     \u2705 Question 2: Correct - 'doesn't' for third person
     \u2705 Question 3: Correct - 'are' for plural"
```

## Troubleshooting

**Problem**: Page shows HTML code
**Solution**: Make sure you're running `start.bat`, not a Streamlit app

**Problem**: AI not responding
**Solution**: Check if Flask server is running in the terminal

**Problem**: Roleplay not working
**Solution**: Make sure you clicked "Roleplay" mode first, then mention the scenario

**Problem**: Quiz not appearing
**Solution**: Make sure you clicked "Quiz" mode first, then explicitly ask for a quiz

Enjoy learning! \ud83c\udf93
