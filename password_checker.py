import re

def check_password_strength(password):
    # Initialize strength score and feedback list
    strength_score = 0
    feedback = []
    
    # Check password length
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long")
    else:
        strength_score += 1
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter")
    else:
        strength_score += 1
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter")
    else:
        strength_score += 1
    
    # Check for numbers
    if not re.search(r'\d', password):
        feedback.append("Password should contain at least one number")
    else:
        strength_score += 1
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")
    else:
        strength_score += 1
    
    # Determine password strength level
    if strength_score <= 2:
        strength_level = "Weak"
    elif strength_score <= 4:
        strength_level = "Moderate"
    else:
        strength_level = "Strong"
    
    return strength_level, feedback

def main():
    print("Welcome to the Password Strength Checker!")
    print("Please enter your password to check its strength.")
    
    while True:
        password = input("\nEnter your password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Thank you for using the Password Strength Checker!")
            break
        
        strength_level, feedback = check_password_strength(password)
        
        print("\nPassword Strength Analysis:")
        print(f"Strength Level: {strength_level}")
        
        if feedback:
            print("\nSuggestions to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("\nGreat! Your password meets all the security criteria.")

if __name__ == "__main__":
    main() 