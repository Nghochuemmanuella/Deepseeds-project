#for loop
#1. starting point
#2. condition
#3. increment or decrement
my_name="hello"
names=["will", "Leo", "Ella", "kait",  "jjghjjh", "gfgg mbom", "jghhf mbom"]
print(names[0])
print(names[1])
print(names[2])

for name in names :
    print(names)
    if name.endswith("mbom"):
        print(f"we dan catch u: {names}")
    else:
        print(f"welcome to the party : {names}")
        
        #print each name an attribute a number infront of it
  #  count = 1
   # for name in names:
    #    print(f" {count}  {name}")
     #   count += 1
        
        #range method in looping
        
        
        #range (start)-stop fro m 0
    for i in range(5):
        print(i)
        
        
    for i in range (2, 7):
        print(i)
    for i in range (0, 10, 20):
        print(i)
    for i in range (10, 0, -1):
        print(f"countdown: {i}")
    print("blast off")

       
        