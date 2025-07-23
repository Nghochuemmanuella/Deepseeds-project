name = "Alice"
age = 30
score = 95.5

print(f"hello,{name} you are {age} years old.")
print (f"your score is {score:.1f}%")
print("hello, {} you are {} years old.".format(name, age))

print("hello, %s you are %d yars old." % (name, age))


# example2
email = "user@example.com"
if "@" in email and "." in email:
    username =email. split("@")[0]
    domain = email.split("@")[1]
    print(f"Username: {username}")
    print(f"domain: {domain}")
else:
    print("invalid email format")
    
    #text and analyses
    
    text = "the quick brown for jumps over a lazy dog"
    print(f"text: {text}")
    print(f"length: {len(text)} character")
    print(f"words: {len(text.split())} words")
    print(f"Uppercase: {text.upper()}")
    print(f"Tittle case: {text.Tittle()}")
    print(f"contains 'fox': {'fox' in text}")
    