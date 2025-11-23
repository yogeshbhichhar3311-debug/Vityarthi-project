import re
def check_password_strength(password):
    if len(password) < 8:
        return "Weak : Password must be at least 8 characters"

    if not any (char.isdigit() for char in password):
        return "weak : Password must include at least one number."

    if not any (char.isupper() for char in password):
        return "weak : Password must include at least one uppercase letter."

    if not any (char.islower() for char in password):
        return "weak : Password must include at least one lowercase letter."

    if not re.search(r'[!@#$%^&+{}(),.:?"|<>]', password):
        return "Medium : Password must include special characters to make your password stronger."

    return "Stong: Your password is secure!"

def password_checker():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit):")

        if password.lower() == 'exit':
            print("Thank you for for using this tool")
            break

        result = check_password_strength(password)
        print(result)

password_checker() 

        
