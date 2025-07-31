#calculate the body mass index of a person

#def BMI_calculator ():  
     
   # weight =float(input("enter weight: "))
   # height =float(input("enter height: "))
   # BMI = weight / (height * 2)
   # if BMI > 18:
   #   print("under weight")
   # if BMI >17<26:
   #   print("u are ok")
   # if BMI >= 25:
   #   print("over weight")
  #  else:
  #   print("you are in trouble")
    
#def bmi_calculator (h, w):
 #   bmi=w/h*h
 #   print(bmi)
    
#weight=float(input("please enter w"))
#height=float(input("please enter h"))
#bmi_calculator(height, weight)


#function with output
#def create_profile(name, age, occupation, city):
   # """Create a personal profile string."""
    
  #  pass
#profile = create_profile("Ella", 20, "Engineering" ,"mile 6")
#print(profile)
    
#def calculate_grade(score):
 #   """Convert numerical score to letter grade."""

 #   pass

# Test your function
#print(calculate_grade(95))  
#print(calculate_grade(87))  
#print(calculate_grade(83))  


#shopping cart total
#def calculate_total(price, quantity, tax_rate=0.08):
 #   """Calculate total cost including tax."""

 #   pass

#total = calculate_total(29.99, 3)
#print(f"Total cost: ${total:.2f}")


#excercise, calculate the avaerage in a array
def analyze_array(arr, target):
  if not arr:
      average = 0
  else:
      average = sum(arr) / len(arr)
  status = "seen" if target in arr else "unseen"
  
  return average, status

numbers = [3, 4, 5]
n = 5
avg, found_status = analyze_array(numbers, n)
print(f"the average of the list is: {avg}")
print(f"target is {found_status}")