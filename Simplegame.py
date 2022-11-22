import random
import time
import os

# letter=["A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letter=["absolutely","accepted","acclaimed","accomplish" ," accomplishment" ," achievement" ," action" ," active" ," admire" ," adorable" ," adventure" ," affirm " ,
    "ative " ,"affluent " ,"agree" ," agree " ,"ableam " ,"azing" ,"angelic " ,"appealing " ,"approve " ,"aptitude " ,"attractive" ,"awesome",
    "beaming","beautiful","believe","beneficial","bliss","bountiful","bounty","brave","bravo","brilliant","bubbly",
    "calm","celebrated","certain","champ","champion","charming","cheery","choice","classic","classical","clean","commend","composed","congratulation","constant","cool",
    "courageous","creative","cute"]
str2=""

def ran(letter):
    str1=((str)(random.choices(letter)))
    return str1

for result in range(0,10):
    if(result < 4):
        print(f"{'LEVEL-1':^50}")
        str2 = ran(letter)
    elif(result < 7):
        
        print(f"{'LEVEL-2':^50}")
        str2 = ran(letter)
    else:
        print(f"{'LEVEL-3':^50}")
        str2 = ran(letter)
    str2=str2.upper()
    retype=""
    for i in str2:
        if (ord(i) >= 65 and ord(i) <= 90):
            retype += i
    
    for i in range(0,1):
        print(retype),
    time.sleep(2)    
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




