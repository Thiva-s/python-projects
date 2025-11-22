import random 
import string  
  
print("Welcome to Password Generator!\n")

user = input("Type 'yes' if you are going to create your own password or Type 'No': ").lower()

def randomstring(length):

    small = string.ascii_lowercase
    large = string.ascii_uppercase
    symbols = "!@#$%&*?/"
    num = string.digits

    password = small + large + symbols + num
    
    temp = random.sample(password, length)
    random_pass = "".join(temp)
    return random_pass


if user == 'yes':
    userpass = input("Enter your password: ")
    print("Your password is: ",userpass())
elif user == 'no':
    size = int(input("Enter the length of password you want: "))
    print("Your generated password is: ",randomstring(size))
else:
    print("Invalid input🤬. Please type 'yes' or 'no'.")