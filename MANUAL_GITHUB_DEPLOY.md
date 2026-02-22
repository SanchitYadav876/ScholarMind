# ScholarMind - Manual GitHub Deploy (Step by Step)

## **Step 1: Configure Git (Run once)**

```powershell
git config --global user.email "tuma.email@gmail.com"
git config --global user.name "Sanchi Yadav"
```

Replace `tuma.email@gmail.com` with your actual Gmail.

## **Step 2: Initialize Repository**

```powershell
cd "d:\learing python"
git init
git remote add origin https://github.com/SanchitYadav876/ScholarMind.git
```

## **Step 3: Add All Files**

```powershell
git add -A
```

## **Step 4: Create First Commit**

```powershell
git commit -m "ScholarMind v1.0 - Initial deployment ready"
```

## **Step 5: Create Main Branch and Push**

```powershell
git branch -M main
git push -u origin main
```

**Windows will show login dialog - Enter your GitHub credentials**

---

## **If Push Still Fails:**

### **Check GitHub Connection:**
```powershell
git config --list
git remote -v
```

### **Clear Credentials (Windows):**
1. Control Panel → Credential Manager
2. Windows Credentials
3. Remove any GitHub entries
4. Try git push again (will ask for login)

### **Use GitHub CLI (Easier):**
```powershell
# Install GitHub CLI
winget install GitHub.cli

# Authenticate
gh auth login

# Push
git push -u origin main
```

---

## **Result When Successful:**

```
Enumerating objects: 250, done.
Counting objects: 100%
Writing objects: 100%
remote: Resolving deltas: 100%
To https://github.com/SanchitYadav876/ScholarMind.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Then your code is LIVE on GitHub! ✅
