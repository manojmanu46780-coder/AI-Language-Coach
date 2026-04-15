from flask import Flask, render_template, request, jsonify, session
import os
import sys
import uuid
from dotenv import load_dotenv

# Fix Unicode output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'linguaai-secret-key-2024'

# Initialize agent
print("Initializing agent...")
from agent import get_agent
agent = get_agent()
print("Agent ready!")

# Store messages per session
sessions_data = {}

@app.route('/')
def index():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        session['mode'] = 'Free Chat'
        sessions_data[session['session_id']] = {
            'messages': [{
                "role": "ai",
                "content": "Hi! I'm your language tutor. Let's practice together.",
                "feedback": None
            }],
            'stats': {'messages': 0, 'mistakes': 0, 'weak_area': 'Grammar'}
        }
    
    session_id = session['session_id']
    messages = sessions_data.get(session_id, {}).get('messages', [])
    stats = sessions_data.get(session_id, {}).get('stats', {})
    mode = session.get('mode', 'Free Chat')
    
    return render_template('index.html', messages=messages, stats=stats, mode=mode)

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.json
        user_message = data.get('message')
        session_id = session.get('session_id')
        mode = session.get('mode', 'Free Chat')
        
        print(f"\n[REQUEST] Mode: {mode}, Message: {user_message}")
        
        if not session_id or session_id not in sessions_data:
            print("[WARNING] Session not found in memory. Re-initializing...")
            if not session_id:
                session_id = str(uuid.uuid4())
                session['session_id'] = session_id
            sessions_data[session_id] = {
                'messages': [{
                    "role": "ai",
                    "content": "Hi! I'm your language tutor. Let's practice together.",
                    "feedback": None
                }],
                'stats': {'messages': 0, 'mistakes': 0, 'weak_area': 'Grammar'}
            }
        
        # Add user message
        sessions_data[session_id]['messages'].append({
            "role": "user",
            "content": user_message,
            "feedback": None
        })
        
        # Get AI responsehttp://127.0.0.1:5000/
        print("[AGENT] Calling agent...")
        response_data = agent.chat(user_message, thread_id=session_id, mode=mode)
        print(f"[AGENT] Got response: {response_data['content'][:100].encode('ascii', errors='replace').decode()}...")
        
        # Add AI message
        sessions_data[session_id]['messages'].append({
            "role": "ai",
            "content": response_data['content'],
            "feedback": response_data.get('feedback')
        })
        
        # Update stats
        sessions_data[session_id]['stats']['messages'] += 1
        if response_data.get('feedback') and response_data['feedback'].get('mistake'):
            sessions_data[session_id]['stats']['mistakes'] += 1
        
        print("[SUCCESS] Response added\n")
        return jsonify({"success": True})
        
    except Exception as e:
        print(f"[ERROR] Exception: {e}")
        import traceback
        traceback.print_exc()
        sid = session.get('session_id')
        if sid and sid in sessions_data:
            sessions_data[sid]['messages'].append({
                "role": "ai",
                "content": "Sorry, I encountered an error. Please try again.",
                "feedback": None
            })
        return jsonify({"success": False, "error": str(e)})

@app.route('/change_mode', methods=['POST'])
def change_mode():
    data = request.json
    mode = data.get('mode', 'Free Chat')
    session['mode'] = mode
    print(f"[MODE] Changed to: {mode}")
    return jsonify({"success": True, "mode": mode})

@app.route('/report')
def report():
    session_id = session.get('session_id')
    if not session_id or session_id not in sessions_data:
        return jsonify({'messages': 0, 'mistakes': 0, 'accuracy': 0, 'weak_area': 'N/A', 'corrections': []})

    data = sessions_data[session_id]
    stats = data.get('stats', {})
    messages = data.get('messages', [])

    corrections = []
    for msg in messages:
        if msg.get('feedback') and msg['feedback'].get('mistake'):
            corrections.append({
                'mistake': msg['feedback'].get('mistake', ''),
                'correction': msg['feedback'].get('correction', ''),
                'tip': msg['feedback'].get('tip', '')
            })

    total = stats.get('messages', 0)
    mistakes = stats.get('mistakes', 0)
    accuracy = round(((total - mistakes) / total) * 100) if total > 0 else 0

    return jsonify({
        'messages': total,
        'mistakes': mistakes,
        'accuracy': accuracy,
        'weak_area': stats.get('weak_area', 'Grammar'),
        'corrections': corrections[-10:]
    })

@app.route('/evaluate_quiz', methods=['POST'])
def evaluate_quiz():
    try:
        data = request.json
        quiz_text = data.get('quiz_text', '')
        user_answers = data.get('answers', {})
        correct_answers = agent.evaluate_quiz(quiz_text, user_answers)
        return jsonify({"success": True, "correct_answers": correct_answers})
    except Exception as e:
        print(f"[ERROR] evaluate_quiz: {e}")
        return jsonify({"success": False, "correct_answers": {}})

@app.route('/new_session', methods=['POST'])
def new_session():
    new_id = str(uuid.uuid4())
    session['session_id'] = new_id
    session['mode'] = 'Free Chat'
    
    sessions_data[new_id] = {
        'messages': [{
            "role": "ai",
            "content": "Hi! I'm your language tutor. Let's practice together.",
            "feedback": None
        }],
        'stats': {'messages': 0, 'mistakes': 0, 'weak_area': 'Grammar'}
    }
    
    print(f"[SESSION] New session created: {new_id}")
    return jsonify({"success": True})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("LinguaAI Server Starting...")
    print("="*60)
    print("Open: http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=True, port=5000, use_reloader=False)
