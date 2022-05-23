import random
import os


def rps():
    splayer = 0
    sai = 0
    print(f"----Score----\n {name} : {splayer} <---> A.I. : {sai}")
    player = int(input("1 for Stone\n2 for Paper\n3 for Scisors\n"))
    ai = random.randint(1,4)
    
    if player == 1 and ai == 1:
        print("TIE") 
    elif player == 2 and ai == 2:
        print("TIE")  
    elif player == 3 and ai == 3:
        print("TIE")
    elif player == 1 and ai == 2:
        print("You Lost!")
        sai += 1
    elif player == 1 and ai == 3:
        print("You Win")
        splayer += 1
    elif player == 2 and ai == 3:
        print("You Lost!")
        sai += 1
    elif player == 2 and ai == 1:
        print("You Win")
        splayer += 1
    elif player == 3 and ai == 1:
        print("You Lost!")
        sai += 1
    elif player == 3 and ai == 2:
        print("You Win")
        splayer += 1
    else:
        print()   
    
    list1 = [splayer, sai]     
    return list1
        
       
            
        

while True:
    choice = input("Press R to continue or Q to quit:\n")
    choice = choice.upper()
    if choice == "R":
        name = ("Enter your name here:\n")
        if name == "temp":
            rps()
        else:
            rps()
    elif choice == "Q":
        exit()
    else:
        print("ERROE!\n No such choice found!" * 100)
    
        
        