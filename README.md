# Password Strength & Hash Tool 

A simple Python tool to **assess the strength of passwords** and **generate a secure SHA-256 hash**. It checks password length, uppercase and lowercase letters, numbers, and special characters, giving actionable feedback to improve weak passwords.

---

## Features

- Checks password **length** (weak if <8 characters, strong if ≥12).  
- Detects **lowercase and uppercase letters**.  
- Detects **numbers**.  
- Detects **special characters** like `!@#$%^&*()`.  
- Provides **actionable suggestions** to improve weak passwords.  
- Generates **SHA-256 hash** of your password for secure storage.  
- Password input is **hidden while typing**.  

---

## How to Use

1. **Download or clone** the repository containing `sanih_password_checker.py`.  
2. Make sure **Python 3** is installed on your system.  
3. Open a terminal (Command Prompt, PowerShell, or macOS/Linux Terminal) and navigate to the folder containing the script.  
4. Run the script with:
   ```bash
   python sanih_password_checker.py
