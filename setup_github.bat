@echo off
REM ScholarMind Setup Script for Windows

echo.
echo ============================================
echo ScholarMind - Complete Setup
echo ============================================
echo.

REM Check if git is installed
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Git not installed. Please install from https://git-scm.com
    pause
    exit /b 1
)

REM Initialize git repo if not already
if not exist ".git" (
    echo Initializing Git repository...
    git init
    git remote add origin https://github.com/SanchitYadav876/ScholarMind.git
)

REM Create .gitignore
echo Creating .gitignore...
(
    echo __pycache__/
    echo *.pyc
    echo .pytest_cache/
    echo node_modules/
    echo .expo/
    echo *.apk
    echo *.aab
    echo dist/
    echo build/
    echo .DS_Store
) > .gitignore

REM Create docs folder for GitHub Pages
if not exist "docs" (
    echo Creating docs folder for GitHub Pages...
    mkdir docs
    copy "developing AI\templates\index.html" docs\
    copy "developing AI\templates\dashboard.html" docs\
)

REM Stage all files
echo Staging files...
git add -A

REM Commit
echo.
set /p message="Enter commit message (default: 'Initial commit - ScholarMind v1.0'): "
if "%message%"=="" set message=Initial commit - ScholarMind v1.0
git commit -m "%message%"

REM Push to GitHub
echo.
echo Pushing to GitHub...
echo Note: You may be prompted to enter GitHub credentials
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ============================================
    echo Successfully pushed to GitHub!
    echo ============================================
    echo.
    echo Next steps:
    echo 1. Go to: https://github.com/SanchitYadav876/ScholarMind
    echo 2. In Settings, enable GitHub Pages
    echo 3. Choose source: docs folder
    echo 4. Your web app will be live at:
    echo    https://SanchitYadav876.github.io/ScholarMind
    echo.
    echo 5. Deploy backend to Render at: https://render.com
    echo 6. Build APK: cd mobile-app ^&^& eas build --platform android
    echo.
) else (
    echo.
    echo Error pushing to GitHub. Check your credentials.
    echo.
)

pause
