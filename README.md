# 🎤 LinguaAI — Adaptive Language Learning Tutor

> Speak better. Every conversation.

LinguaAI is an AI-powered language learning tutor that helps users improve their speaking skills through real-time conversation, intelligent grammar correction, adaptive quizzes, and progress tracking.

---

## 🚀 Features

### 💬 Conversational Learning

* Chat with an AI tutor in real-time
* Practice natural conversations
* Improve fluency through interaction

---

### 🧠 Grammar Correction

* Detects mistakes instantly
* Provides:

  * ❌ Mistake
  * ✅ Correct sentence
  * 💡 Explanation

---

### 🎭 Roleplay Scenarios

Practice real-world situations:

* Job interviews
* Travel conversations
* Daily communication

---

### 🧪 Adaptive Quiz System

* Mixed question types:

  * MCQ
  * Fill in the blanks
  * Sentence correction
  * Context-based
  * Conversation-based

* Difficulty levels:

  * Easy
  * Medium
  * Hard

---

### 📊 Auto Evaluation & Scoring

* Automatically evaluates answers
* Displays score and feedback
* Helps identify learning gaps

---

### 📈 Progress Tracking

* Tracks:

  * Total messages
  * Mistakes
  * Weak areas
* Provides personalized insights

---

## 🧠 Tech Stack

* **Frontend:** Streamlit (custom UI/UX)
* **Backend:** Python + LangGraph (ReAct Agent)
* **LLM:** Groq (llama-3.3-70b-versatile)
* **Architecture:** Tool-based AI agent with memory

---

## 📁 Project Structure

```
lingua-ai/
├── app.py
├── agent.py
├── tools.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/lingua-ai.git
cd lingua-ai
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Set your Groq API key:

```bash
export GROQ_API_KEY="your_api_key_here"
```

Or update directly in `config.py`.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Usage

* Start conversation:

  > I goed to market yesterday

* Try roleplay:

  > Start job interview roleplay

* Generate quiz:

  > Give me a hard quiz on past tense

---

## 🎯 How It Works

LinguaAI uses a LangGraph-based AI agent that:

* Processes user input
* Calls intelligent tools (quiz, feedback, tracking)
* Maintains memory for personalized learning
* Generates structured responses using Groq LLM

---

## 🏆 Highlights

* Not just a chatbot — a **learning system**
* Real-time feedback loop
* Adaptive difficulty
* Clean, human-centered UI

---

## 🚀 Future Improvements

* 🎤 Voice input & pronunciation feedback
* 📊 Advanced analytics dashboard
* 🎮 Gamification (XP, streaks)
* 🌍 Multi-language support

---

## 👨‍💻 Author

**Arshad**
Developed as part of an AI Workshop, focusing on building adaptive, real-world AI systems for language learning and intelligent user interaction.

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

