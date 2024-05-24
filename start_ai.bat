@echo off
title Pirates Online Classic - AI

rem Get the user input:
set /P DISTRICT_NAME=District name (DEFAULT: Abassa): || ^
set DISTRICT_NAME=Abassa
set /P BASE_CHANNEL=Base channel (DEFAULT: 401000000):  || ^
set BASE_CHANNEL=401000000

title Pirates Online Classic - AI (%DISTRICT_NAME%)

rem Choose correct python command to execute the game
ppythona -h >nul 2>&1 && (
    set PYTHON_CMD=pythona
) || (
    set PYTHON_CMD=python
)

echo =============================================
echo Starting Pirates Online Classic District...
echo District Name: %DISTRICT_NAME%
echo Base channel: %BASE_CHANNEL%
echo ============================================

rem Start AI server
:main
%PYTHON_CMD% -m pirates.ai.ServiceStart --base-channel %BASE_CHANNEL% ^
    --district-name "%DISTRICT_NAME%"
pause
goto main
