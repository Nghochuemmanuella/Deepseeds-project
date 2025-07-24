#for loop
#1. starting point
#2. condition
#3. increment or decrement
#my_name="hello"
#names=["will", "Leo", "Ella", "kait",  "jjghjjh", "gfgg mbom", "jghhf mbom"]
#print(names[0])
#print(names[1])
#print(names[2])

#for name in names :
  #  print(names)
   # if name.endswith("mbom"):
    #    print(f"we dan catch u: {names}")
   # else:
     #   print(f"welcome to the party : {names}")
        
        #print each name an attribute a number infront of it
  #  count = 1
   # for name in names:
    #    print(f" {count}  {name}")
     #   count += 1
        
        #range method in looping
        
        
        #range (start)-stop fro m 0
   # for i in range(5):
    #    print(i)
        
        
    #for i in range (2, 7):
      #  print(i)
    #for i in range (0, 10, 20):
      #  print(i)
    #for i in range (10, 0, -1):
      #  print(f"countdown: {i}")
    #print("blast off")

       #whiole loop
count = 1
while count <= 5:
    print(f"count is: {count}")
    count += 1
    
    #user input loop
user_input = ""
while user_input != "quit":
    user_input = input("enter 'quit' to exit")
    if user_input != "quit":
        print(f"you entered: {user_input}")
print("Goodbye")
        
     #break - exit the loop comletely
print("finding the first even number: ")
for number in range(1, 10):
 if number % 2 == 0:
    print(f"found even number: {number}") 
    
    
    #continues - skip to next iteration
print ("\nPrinting only odd numbers:")
for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(f"odd number: {number}")
    
    #how to put loops insides of loops()
    
    #multiplication table
print("multiplication Table:")
for i in range(1, 4):
 for j in range(1, 4):
    result = i * j
    print(f"{i} x {j} = {result}")
print()

# Pattern printing
print("Triangle pattern:")
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print() 