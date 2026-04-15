@echo off
echo Stopping old server...
taskkill /F /IM python.exe /T 2>nul
timeout /t 2 /nobreak >nul
echo.
echo Starting LinguaAI...
echo.
set GROQ_API_KEY=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
python app.py
