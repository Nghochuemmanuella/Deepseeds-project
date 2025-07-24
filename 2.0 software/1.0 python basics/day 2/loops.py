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