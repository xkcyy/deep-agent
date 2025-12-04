@echo off

REM Deep Agent Startup Script
REM Starts both frontend and backend services

cd /d "d:\00self-ai\deep-agent"

echo Starting Deep Agent services...
echo.

REM Start backend service in new window
start "Deep Agent Backend" cmd /k "cd deep-agents-backend && uv run langgraph dev"

REM Wait for backend to initialize
echo Waiting for backend to initialize...
timeout /t 3 /nobreak >nul

REM Start frontend service in new window
start "Deep Agent Frontend" cmd /k "cd deep-agents-ui && npm run dev"

REM Wait for frontend to initialize
echo Waiting for frontend to initialize...
timeout /t 3 /nobreak >nul

echo.
echo Deep Agent services started successfully!
echo Frontend: http://localhost:3000
echo Backend: http://127.0.0.1:2024
echo.
echo Press any key to exit this window...
pause >nul