# LinguaAI - AI Language Learning Tutor

A premium AI-powered language learning application built with Flask, LangGraph, and Groq.

## Features

- **Free Chat Mode**: Natural conversation practice with real-time grammar corrections
- **Roleplay Mode**: Practice real-world scenarios (interviews, travel, restaurants)
- **Quiz Mode**: Test your knowledge with AI-generated quizzes
- **Smart Feedback**: Get instant corrections with explanations
- **Progress Tracking**: Monitor your mistakes and improvement areas
- **Memory**: Conversations are remembered within each session

## Tech Stack

- **Frontend**: Flask + Custom HTML/CSS
- **Backend**: Python
- **AI Agent**: LangGraph (create_react_agent)
- **LLM**: Groq (llama-3.3-70b-versatile)
- **Memory**: MemorySaver for conversation continuity

## Setup

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Up Groq API Key**

Get your free API key from: https://console.groq.com/keys

Then set it as an environment variable:

**Windows:**
```bash
set GROQ_API_KEY=your_api_key_here
```

**Mac/Linux:**
```bash
export GROQ_API_KEY=your_api_key_here
```

Or create a `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

3. **Run the Application**
```bash
python app.py
```

4. **Open in Browser**
```
http://localhost:5000
```

## Usage

### Free Chat Mode
- Have natural conversations
- Get instant grammar corrections
- Receive explanations for mistakes

### Roleplay Mode
- Select from different scenarios
- Practice real-world situations
- Get feedback while staying in character

### Quiz Mode
- Request quizzes on specific topics
- Test your grammar and vocabulary
- Get immediate feedback

## Project Structure

```
├── app.py              # Flask web server
├── agent.py            # LangGraph agent implementation
├── tools.py            # Language learning tools
├── config.py           # LLM configuration
├── templates/
│   └── index.html      # Frontend UI
└── requirements.txt    # Dependencies
```

## How It Works

1. **User Input**: You type a message in any mode
2. **Agent Processing**: LangGraph agent analyzes your message
3. **Tool Execution**: Agent uses tools to analyze grammar, start roleplay, or generate quizzes
4. **Smart Response**: AI provides conversational response + structured feedback
5. **Memory**: Conversation context is maintained throughout the session

## Feedback Format

Every response includes structured feedback:

❌ **Mistake**: What you said incorrectly
✅ **Correction**: The correct way to say it
💡 **Tip**: Explanation and learning point

## License

MIT License
