import random 
import string

gen = string.ascii_letters 
raw = string.ascii_lowercase 
ppp = string.ascii_uppercase 
pp2 = string.digits 
pp3 = string.hexdigits 
pp4 = string.whitespace
pp5 = string.punctuation

print("Password Generator By DK")
password_length = int(input("Enter your password's length (7 to 49 characters): "))

if 7 <= password_length <= 49:
    password = ''
    
    for _ in range(password_length):
        category = random.randint(1, 7)
        
        if category == 1:
            password += random.choice(gen)
        elif category == 2:
            password += random.choice(raw)
        elif category == 3:
            password += random.choice(ppp)
        elif category == 4:
            password += random.choice(pp2)
        elif category == 5:
            password += random.choice(pp3)
        elif category == 6:
            password += random.choice(pp4)
        elif category == 7:
            password += random.choice(pp5)

    print("Generated Password:", password)
else:
    print("Please enter a valid password length between 7 and 49 characters.")
