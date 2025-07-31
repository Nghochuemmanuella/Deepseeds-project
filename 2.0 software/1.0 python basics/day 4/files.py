#Record book program
from datetime import datetime
date = datetime.now().strftime("%Y-%m-%d $H:%M")

def add_record(record, date):
  
    with open ("record.txt", "w") as file:
       file.write(f"--Record Book--\n{date}\n{record}")
       
userInput = 0

while(userInput != "exit"):
    if userInput == "exit":
        break
    else:
        print("-- Record Book--")
        print(date)
        userInput = input("what have u learned today: ")
        add_record(userInput, date)
    
    


