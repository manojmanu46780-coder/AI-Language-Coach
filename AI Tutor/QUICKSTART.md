# 🚀 QUICK START GUIDE

## Step 1: Get Your Groq API Key (FREE)

1. Go to: https://console.groq.com/keys
2. Sign up (it's free!)
3. Create a new API key
4. Copy the key

## Step 2: Set Your API Key

Open Command Prompt and run:

```bash
set GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual key.

## Step 3: Run the App

```bash
python app.py
```

Or simply double-click: `run.bat`

## Step 4: Open in Browser

Go to: http://localhost:5000

---

## 🎯 How to Use

### Free Chat Mode
- Type naturally: "I go to school yesterday"
- Get instant corrections with explanations

### Roleplay Mode
- Click "Roleplay" in sidebar
- Say: "Let's practice a job interview"
- AI will roleplay and correct your language

### Quiz Mode
- Click "Quiz" in sidebar
- Say: "Give me a grammar quiz"
- Answer questions and get feedback

---

## 💡 Tips

- The AI remembers your conversation in each session
- Click "New Session" to start fresh
- Progress stats update automatically
- All corrections include explanations

---

## 🐛 Troubleshooting

**Problem**: "GROQ_API_KEY not set"
**Solution**: Run `set GROQ_API_KEY=your_key` before starting

**Problem**: "Module not found"
**Solution**: Run `pip install -r requirements.txt`

**Problem**: Port 5000 already in use
**Solution**: Change port in app.py: `app.run(debug=True, port=5001)`

---

Enjoy learning! 🎓
