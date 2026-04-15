@echo off
echo ========================================
echo LinguaAI - AI Language Learning Tutor
echo ========================================
echo.

REM Check if GROQ_API_KEY is set
if "%GROQ_API_KEY%"=="" (
    echo WARNING: GROQ_API_KEY environment variable is not set!
    echo.
    echo Please set your Groq API key:
    echo   set GROQ_API_KEY=your_api_key_here
    echo.
    echo Get your free API key from: https://console.groq.com/keys
    echo.
    pause
    exit /b 1
)

echo Starting LinguaAI...
echo.
echo Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
