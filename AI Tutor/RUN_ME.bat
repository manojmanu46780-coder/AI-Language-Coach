@echo off
echo Stopping any running servers...
taskkill /F /IM python.exe /T 2>nul
timeout /t 2 /nobreak >nul
cls

echo ========================================
echo    LinguaAI - Language Learning Tutor
echo ========================================
echo.
echo Starting server...
echo.

set GROQ_API_KEY=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

echo Server will start at: http://localhost:5000
echo.
echo After you see "Running on http://127.0.0.1:5000"
echo Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause
