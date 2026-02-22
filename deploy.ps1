# ScholarMind - Auto Deploy Script
# PowerShell Script - Run as Administrator

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "ScholarMind - Auto Deploy to GitHub" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
$gitCheck = git --version 2>$null
if (!$gitCheck) {
    Write-Host "Error: Git not installed!" -ForegroundColor Red
    Write-Host "Download: https://git-scm.com" -ForegroundColor Yellow
    pause
    exit
}

# Set Git config
Write-Host "Configuring Git..." -ForegroundColor Yellow
git config user.name "Sanchi Yadav" | Out-Null
git config user.email "sanchityadav876@gmail.com" | Out-Null

# Initialize repo if needed
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Green
    git init | Out-Null
    git remote add origin https://github.com/SanchitYadav876/ScholarMind.git | Out-Null
    Write-Host "Repository initialized" -ForegroundColor Green
}

# Create docs folder for GitHub Pages
if (!(Test-Path "docs")) {
    Write-Host "Creating docs folder..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path docs | Out-Null
    
    if (Test-Path "developing AI\templates\index.html") {
        Copy-Item "developing AI\templates\index.html" "docs\" -Force | Out-Null
        Copy-Item "developing AI\templates\dashboard.html" "docs\predictor.html" -Force | Out-Null
        Write-Host "Files copied to docs folder" -ForegroundColor Green
    }
}

# Create .gitignore
Write-Host "Creating .gitignore..." -ForegroundColor Yellow
$gitignore = @"
__pycache__/
*.pyc
.pytest_cache/
node_modules/
.expo/
*.apk
*.aab
dist/
build/
.DS_Store
*.log
"@
$gitignore | Out-File .gitignore -Encoding UTF8

# Stage all files
Write-Host "Staging files..." -ForegroundColor Yellow
git add -A | Out-Null

# Show status
Write-Host ""
Write-Host "Files to commit:" -ForegroundColor Cyan
git status --short

# Commit
Write-Host ""
Write-Host "Enter commit message (press Enter for default):" -ForegroundColor Green
$message = Read-Host "> "
if (!$message) {
    $message = "ScholarMind v1.0 - Deploy ready"
}

Write-Host "Committing..." -ForegroundColor Yellow
git commit -m $message | Out-Null
Write-Host "Committed successfully" -ForegroundColor Green

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow

git branch -M main 2>$null | Out-Null
git push -u origin main 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "============================================" -ForegroundColor Green
    Write-Host "SUCCESS! Pushed to GitHub!" -ForegroundColor Green
    Write-Host "============================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next Steps:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Go to GitHub: https://github.com/SanchitYadav876/ScholarMind" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "2. Enable GitHub Pages:" -ForegroundColor Green
    Write-Host "   Settings -> Pages -> Branch: main, Folder: /docs -> Save" -ForegroundColor Gray
    Write-Host ""
    Write-Host "3. Your website: https://SanchitYadav876.github.io/ScholarMind" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "4. Deploy backend on Render: https://render.com" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "5. Build APK:" -ForegroundColor Green
    Write-Host "   cd mobile-app && eas build --platform android" -ForegroundColor Gray
    Write-Host ""
    Write-Host "============================================" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERROR! Push failed!" -ForegroundColor Red
    Write-Host "Check internet and GitHub credentials" -ForegroundColor Yellow
    Write-Host ""
}

pause
