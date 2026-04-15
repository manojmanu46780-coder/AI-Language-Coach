"""
Setup verification script for LinguaAI
Run this to check if everything is configured correctly
"""

import sys
import os

def check_dependencies():
    """Check if all required packages are installed"""
    required = ['flask', 'langchain', 'langchain_groq', 'langgraph']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"[OK] {package} installed")
        except ImportError:
            print(f"[FAIL] {package} NOT installed")
            missing.append(package)
    
    return len(missing) == 0

def check_api_key():
    """Check if GROQ_API_KEY is set"""
    api_key = os.getenv("GROQ_API_KEY")
    if api_key and api_key != "your_groq_api_key_here":
        print(f"[OK] GROQ_API_KEY is set")
        return True
    else:
        print(f"[FAIL] GROQ_API_KEY is NOT set")
        print(f"  Set it with: set GROQ_API_KEY=your_key")
        return False

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'agent.py',
        'tools.py',
        'config.py',
        'templates/index.html'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"[OK] {file} exists")
        else:
            print(f"[FAIL] {file} NOT found")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 50)
    print("LinguaAI Setup Verification")
    print("=" * 50)
    print()
    
    print("Checking dependencies...")
    deps_ok = check_dependencies()
    print()
    
    print("Checking API key...")
    api_ok = check_api_key()
    print()
    
    print("Checking files...")
    files_ok = check_files()
    print()
    
    print("=" * 50)
    if deps_ok and api_ok and files_ok:
        print("[SUCCESS] All checks passed! You're ready to run the app.")
        print()
        print("Run: python app.py")
        print("Then open: http://localhost:5000")
    else:
        print("[WARNING] Some checks failed. Please fix the issues above.")
        if not deps_ok:
            print()
            print("Install dependencies: pip install -r requirements.txt")
        if not api_ok:
            print()
            print("Get API key: https://console.groq.com/keys")
            print("Set it: set GROQ_API_KEY=your_key")
    print("=" * 50)

if __name__ == "__main__":
    main()
