
# Password Strength Checker

password = input("Enter your password: ")

if len(password) < 6:
    print("Weak Password")

elif password.isdigit():
    print("Weak Password - Only numbers")

elif password.isalpha():
    print("Medium Password - Only letters")

elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Strong Password")

else:
    print("Medium Password")


print("Password checking completed!")
