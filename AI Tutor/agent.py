from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from config import get_llm
import json

class LanguageTutorAgent:
    def __init__(self):
        self.llm = get_llm()
        self.conversations = {}
        
        self.system_prompt = """You are LinguaAI, an expert language tutor.

**FREE CHAT MODE:**
- Natural conversations with grammar feedback
- Format: ❌ Mistake: [error] ✅ Correction: [fix] 💡 Explanation: [why]

**ROLEPLAY MODE:**
- Detect: interview, job, travel, hotel, restaurant, waiter, casual, friend
- IMMEDIATELY roleplay as: hiring manager, receptionist, waiter, or friend
- Stay in character + provide corrections

**QUIZ MODE:**
- Detect: quiz, test, questions, practice
- IMMEDIATELY generate 5 multiple-choice questions (MCQs). Every question MUST have 4 options (A, B, C, D). Do not use fill-in-the-blanks or open-ended questions.

Here's your quiz:

1. [Question]
   A) [option]
   B) [option]
   C) [option]
   D) [option]

[Repeat format for questions 2-5]

Keep questions SHORT. After answers, give detailed feedback."""
        
    def chat(self, user_message: str, thread_id: str = "default", mode: str = "Free Chat"):
        if thread_id not in self.conversations:
            self.conversations[thread_id] = []
        
        mode_instructions = {
            "Free Chat": "Correct grammar using ❌ ✅ 💡 format.",
            "Roleplay": "START roleplaying immediately as the character.",
            "Quiz": "GENERATE 5 questions NOW in the specified format."
        }
        
        instruction = mode_instructions.get(mode, mode_instructions["Free Chat"])
        
        if mode == "Quiz":
            contextualized_message = f"""[QUIZ MODE]
{instruction}

User: {user_message}

Generate 5 multiple-choice questions. 
EVERY question must be an MCQ with 4 options (A, B, C, D).
Do NOT generate fill-in-the-blanks or any other type of questions."""
        elif mode == "Roleplay":
            contextualized_message = f"""[ROLEPLAY MODE]
{instruction}

User: {user_message}

If scenario mentioned, START roleplaying NOW."""
        else:
            contextualized_message = f"[{mode}] {instruction}\n\nUser: {user_message}"
        
        messages = [SystemMessage(content=self.system_prompt)]
        messages.extend(self.conversations[thread_id])
        messages.append(HumanMessage(content=contextualized_message))
        
        response = self.llm.invoke(messages)
        ai_response = response.content
        
        self.conversations[thread_id].append(HumanMessage(content=user_message))
        self.conversations[thread_id].append(AIMessage(content=ai_response))
        
        if len(self.conversations[thread_id]) > 10:
            self.conversations[thread_id] = self.conversations[thread_id][-10:]
        
        response_data = self._parse_response(ai_response, user_message, mode)
        return response_data
    
    def _parse_response(self, ai_response: str, user_message: str, mode: str = "Free Chat"):
        feedback = None
        content = ai_response
        
        if mode == "Quiz" and any(q in ai_response for q in ["1.", "2.", "3.", "Question"]):
            return {"content": ai_response, "feedback": None}
        
        if "❌" in ai_response or "Mistake:" in ai_response:
            lines = ai_response.split("\n")
            feedback_lines = []
            content_lines = []
            in_feedback = False
            
            for line in lines:
                if any(marker in line for marker in ["❌", "✅", "💡", "Mistake:", "Correction:", "Explanation:"]):
                    in_feedback = True
                    feedback_lines.append(line)
                elif in_feedback and line.strip() and not any(marker in line for marker in ["❌", "✅", "💡"]):
                    feedback_lines.append(line)
                elif not in_feedback:
                    content_lines.append(line)
            
            if feedback_lines:
                content = "\n".join(content_lines).strip()
                feedback_text = "\n".join(feedback_lines).strip()
                feedback = self._structure_feedback(feedback_text)
        
        return {"content": content if content else ai_response, "feedback": feedback}
    
    def _structure_feedback(self, feedback_text: str):
        feedback = {"mistake": None, "correction": None, "tip": None}
        lines = feedback_text.split("\n")
        current_key = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if "❌" in line or "Mistake:" in line:
                current_key = "mistake"
                text = line.replace("❌", "").replace("Mistake:", "").strip()
                if text:
                    feedback["mistake"] = text
            elif "✅" in line or "Correction:" in line:
                current_key = "correction"
                text = line.replace("✅", "").replace("Correction:", "").strip()
                if text:
                    feedback["correction"] = text
            elif "💡" in line or "Explanation:" in line or "Tip:" in line:
                current_key = "tip"
                text = line.replace("💡", "").replace("Explanation:", "").replace("Tip:", "").strip()
                if text:
                    feedback["tip"] = text
            elif current_key and line:
                if feedback[current_key]:
                    feedback[current_key] += " " + line
                else:
                    feedback[current_key] = line
        
        if not any(feedback.values()):
            return None
            
        return feedback
    
    def evaluate_quiz(self, quiz_text: str, user_answers: dict):
        """Given quiz text and user answers {q_index: letter}, return correct answers."""
        answers_str = ", ".join(f"Q{int(k)+1}: {v}" for k, v in user_answers.items())
        prompt = f"""You are a quiz evaluator. Given the following quiz, identify the correct answer (A/B/C/D) for each question.
Return ONLY a JSON object like: {{"0": "A", "1": "C", "2": "B", "3": "D", "4": "A"}}
No explanation, no extra text, just the JSON.

Quiz:
{quiz_text}"""
        messages = [SystemMessage(content="You are a quiz answer key generator. Return only valid JSON."),
                    HumanMessage(content=prompt)]
        response = self.llm.invoke(messages)
        try:
            import re
            json_match = re.search(r'\{[^}]+\}', response.content)
            if json_match:
                return json.loads(json_match.group())
        except Exception:
            pass
        return {}

    def start_new_session(self, thread_id: str):
        if thread_id in self.conversations:
            self.conversations[thread_id] = []
        return {"status": "new_session_started", "thread_id": thread_id}

_agent_instance = None

def get_agent():
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = LanguageTutorAgent()
    return _agent_instance
