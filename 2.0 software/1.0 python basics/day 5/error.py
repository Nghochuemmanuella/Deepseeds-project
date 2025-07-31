def style():
    print("_"*40)

def number_error():
    ""
try:
    style()   
    user_input=int(input("please enter your phone number"))
    print(f"user imput is {user_input}")
except ValueError:
    print("please make sure u are imputing a number")
    
    
def division_error():
    ""
    try:
        style()
        first_number=int(input("enter first number: "))
        second_number=int(input("enter second number: "))
        return first_number/second_number
    except ZeroDivisionError:
        print("please enter a number that is different from zero")


          

def dictionary_error(data,):
        try:
            date=int(input(""))
            color=data["red"]
        except KeyError:
            print("you accesing a key that does not exist")
            
data={
    "name":"Ella", "age": 20,
    }
    
dictionary_error()
    
    
division_error()
    
    
number_error()