import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add special characters (e.g., !, @, #, $).")

    # Determine overall strength
    if strength <= 2:
        strength_level = "Weak"
    elif strength <= 4:
        strength_level = "Moderate"
    else:
        strength_level = "Strong"

    return strength_level, feedback

# Example usage
password = input("Enter your password: ")
level, suggestions = assess_password_strength(password)
print(f"Password Strength: {level}")
if suggestions:
    print("Suggestions to improve your password:")
    for s in suggestions:
        print(f"- {s}")
