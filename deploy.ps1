# ScholarMind - Auto Deploy Script
# PowerShell Script - Run as Administrator

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "ScholarMind - Auto Deploy to GitHub" -ForegroundColor Cyan
Write-Host "============================================`n" -ForegroundColor Cyan

# Check if Git is installed
$gitCheck = git --version 2>$null
if (!$gitCheck) {
    Write-Host "Error: Git not installed!" -ForegroundColor Red
    Write-Host "Download: https://git-scm.com" -ForegroundColor Yellow
    exit
}

# Set Git config (first time only)
Write-Host "Configuring Git..." -ForegroundColor Yellow
git config user.name "Sanchi Yadav" | Out-Null
git config user.email "sanchityadav876@gmail.com" | Out-Null

# Initialize repo if needed
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Green
    git init | Out-Null
    git remote add origin https://github.com/SanchitYadav876/ScholarMind.git | Out-Null
    Write-Host "✓ Repository initialized" -ForegroundColor Green
}

# Create docs folder for GitHub Pages
if (!(Test-Path "docs")) {
    Write-Host "Creating docs folder..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path docs | Out-Null
    
    # Copy web assets
    if (Test-Path "web-assets\index.html") {
        Copy-Item "web-assets\index.html" "docs\" -Force | Out-Null
        Copy-Item "web-assets\predictor.html" "docs\" -Force | Out-Null
    }
    
    if (Test-Path "developing AI\templates\index.html") {
        Copy-Item "developing AI\templates\index.html" "docs\" -Force | Out-Null
        Copy-Item "developing AI\templates\dashboard.html" "docs\predictor.html" -Force | Out-Null
    }
    
    Write-Host "✓ Files copied to docs folder" -ForegroundColor Green
}

# Create .gitignore
Write-Host "Creating .gitignore..." -ForegroundColor Yellow
@"
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
.env
.venv
venv/
"@ | Out-File .gitignore -Encoding UTF8

# Stage all files
Write-Host "Staging files..." -ForegroundColor Yellow
git add -A | Out-Null

# Show status
Write-Host "`nFiles to commit:" -ForegroundColor Cyan
git status --short

# Commit
Write-Host "`nEnter commit message (press Enter for default): " -ForegroundColor Green -NoNewline
$message = Read-Host
if (!$message) {
    $message = "ScholarMind v1.0 - Deploy ready with 3D UI and Render backend"
}

Write-Host "Committing..." -ForegroundColor Yellow
git commit -m $message | Out-Null
Write-Host "✓ Committed" -ForegroundColor Green

# Push to GitHub
Write-Host "`nPushing to GitHub..." -ForegroundColor Yellow
Write-Host "Note: You may be asked for GitHub credentials`n" -ForegroundColor Gray

git branch -M main 2>$null | Out-Null
git push -u origin main

$pushSuccess = $?

if ($pushSuccess) {
    Write-Host "`n============================================" -ForegroundColor Green
    Write-Host "✓ Successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "============================================`n" -ForegroundColor Green
    
    Write-Host "Next Steps:" -ForegroundColor Cyan
    Write-Host "1. Go to: " -ForegroundColor Green -NoNewline
    Write-Host "https://github.com/SanchitYadav876/ScholarMind" -ForegroundColor Yellow
    Write-Host "`n2. Enable GitHub Pages:" -ForegroundColor Green
    Write-Host "   Settings → Pages → Source: docs folder → Save" -ForegroundColor Yellow
    
    Write-Host "`n3. Your website will be live at:" -ForegroundColor Green
    Write-Host "   https://SanchitYadav876.github.io/ScholarMind" -ForegroundColor Cyan
    
    Write-Host "`n4. Deploy Backend to Render:" -ForegroundColor Green
    Write-Host "   https://render.com → New Web Service → Connect GitHub" -ForegroundColor Yellow
    
    Write-Host "`n5. Build Mobile APK:" -ForegroundColor Green
    Write-Host "   cd mobile-app" -ForegroundColor Gray
    Write-Host "   eas build --platform android" -ForegroundColor Gray
    
    Write-Host "`n============================================`n" -ForegroundColor Green
} else {
    Write-Host "`nError pushing to GitHub!" -ForegroundColor Red
    Write-Host "Check your internet connection and GitHub credentials" -ForegroundColor Yellow
}

Read-Host "Press Enter to exit"
