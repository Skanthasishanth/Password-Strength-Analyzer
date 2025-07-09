import re

def check_password_strength(password):
    strength = "STRONG ✅"
    issues = []

    if len(password) < 8:
        issues.append("- Too short (minimum 8 characters)")

    if not re.search(r"[A-Z]", password):
        issues.append("- Missing uppercase letter")

    if not re.search(r"[a-z]", password):
        issues.append("- Missing lowercase letter")

    if not re.search(r"\d", password):
        issues.append("- Missing digit")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("- Missing special character")

    common_passwords = ['123456', 'password', 'admin', 'qwerty', 'letmein']
    if password.lower() in common_passwords:
        issues.append("- Common/guessable password")

    if issues:
        strength = "WEAK ❌"

    return strength, issues

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result, reasons = check_password_strength(user_password)
    print(f"\nStrength: {result}")
    if reasons:
        print("Reasons:")
        for reason in reasons:
            print(reason)