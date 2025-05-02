# importing 2 in-built module 
import random
import string 

print("\n\n\t\tWelcome to the password generator.\n")
print("=============================================================\n")
print("\t          Let's generate your password \n\n")

print(str(input("Enter your name:- ")))
print("\n")
#then we create a function with 1 parameter and take a one variable, 
# it use ascii_letter,  digits & punctuation then it take a user input 
def generate_password(length):
    ch = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    pwd = ''.join(random.choice(ch) for _ in range(length))
    return pwd

length = int(input("Enter yout password length: "))

# Here in password var, it calls generate_password(length) function
password = generate_password(length)
print("\n Generate password: ", password)

print("\n\t Calculation of your password is completed....\n")

print(str(input("\nGive your feedback:- ")))
print("\n\n\t\tThank you for using the password generator.\n")