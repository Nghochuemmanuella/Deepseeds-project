#calculate the body mass index of a person

weight =float(input("enter weight: "))
height =float(input("enter height: "))
BMI = weight / (height * 2)
if BMI > 18:
    print("under weight")
if BMI >17<26:
    print("u are ok")
if BMI >= 25:
    print("over weight")
else:
    print("you are in trouble")


