import random
import time
import os

letter=["A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
str2=""

for result in range(0,10):
    if(result < 4):
        str2 = ((str)(random.choices(letter,k=3)))
    elif(result < 7):
        str2 = ((str)(random.choices(letter,k=6)))
    else:
        str2 = ((str)(random.choices(letter,k=8)))
    retype=""
    for i in str2:
        if (ord(i) >= 65 and ord(i) <= 90):
            retype += i
    
    for i in range(0,1):
        print(retype),
    time.sleep(4)    
    os.system("cls")
    Player=input("Enter above letters as it is : ")
    os.system("cls")
    print("Next Word Coming......")
    time.sleep(1)  
    os.system("cls")
    Player=Player.upper()
    if Player == retype:
        for retype in retype:
            del retype
    else: 
        print("Wrong Answer") 
        time.sleep(2)
        os.system("cls")
        break
print("RESULT : ",result)




