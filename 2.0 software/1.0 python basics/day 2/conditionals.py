#vote eligability
#age=int(input("Please enter your age"))
#if age > 18:
  #  print("Yes you can vote")
#else:
   # print("please wait for next election")
    
    
    #exercise, take a persons age, check if > 15. if yes, they can play baskate ball team
    
  #  age=int(input("Please enter your age"))
   # if age > 16:
     #   print("Yes u can play in the basket ball team")
  #  else:
       # print("you must be above 16 to play")
        
        #if else elif chain
        
#command=input("enter 'exit' to end program and 'continue' to keep going")
#if command=="exit":
 #   print("exiting cmd")
    
#elif command=="continue":
 #   print("continue enjoying...")
    
#else:
 #   print("wrong command")
    
    
    #multiple elif
#print("_"*50)
#grade=float(input("what is your grade: "))
#if grade>=80:
  #  print("A grade")
#elif grade>=70:
  #  print("B+😍")
#elif grade>=60:
  #  print("B grade")
#elif grade>=50:
   # print("C grade")
#else:
  #  print("resit")
    
    #calculator
    
first_number=float(input("Enter first number: "))
second_number=float(input("entet second number"))
operator=input("enter operator")
results=0

if operator=="+":
    results=first_number + second_number
    print(f"result is : {results}")
elif operator=="-":
    results=first_number - second_number
    print(f"result is : {results}")
elif operator=="/":
    results=first_number / second_number
    print(f"result is : {results}")
elif operator=="*":
   
   
    results==first_number * second_number
    print(f"result is : {results}")
 #  print(f"result is : {results}")
   # results=="cannot go"
   # print(f"result is : {results}")
else:
    print("check your operation signs")
    
    #leap year checker
    
    
Year=int(input("Enter Year: "))
if Year%4!=0 and Year%100!=0 and Year%400!=0:
    print("not a leap year")
else:
    print("leep year")

Year=int(input("Enter Year: "))
if Year%4!=0:
    if Year%100!=0:
        if Year%400!=0:
            print("not a leap year")
else:
    print("leap year")
    