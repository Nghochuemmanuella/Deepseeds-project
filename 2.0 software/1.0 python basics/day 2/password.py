
    
    #password checker.
    
l= False
u = False
d = False
password=input("Enter your passwod: ")

for letter in password:
    if letter.islower():
        l = True
    elif letter.isupper():
        u = True
    elif letter.isdigit():
        d = True
        
if l and u and d:
    print("strong password")
else:
    print("weak password")
    