import random


def rps():
    player = int(input("1 for Stone\n2 for Paper\n3 for Scisors\n"))
    ai = random.randint(1,4)
    
    while(True):
    
        if player == 1 and ai == 1:
            print("TIE")
            sai = +0
            splayer = +0
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
            
            
        elif player == 2 and ai == 2:
            print("TIE")
            sai = +0
            splayer = +0
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
            
        elif player == 3 and ai == 3:
            print("TIE")
            sai = +0
            splayer = +0
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        
        elif player == 1 and ai == 2:
            print("You Lost!")
            sai = +1
            splayer = +0
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        
        elif player == 1 and ai == 3:
            print("You Win")
            sai = +0
            splayer = +1
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        
        elif player == 2 and ai == 3:
            print("You Lost!")
            sai = +1
            splayer = +0
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        
        elif player == 2 and ai == 1:
            print("You Win")
            sai = +0
            splayer = +1
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        
        elif player == 3 and ai == 1:
            print("You Lost!")
            sai = +1
            splayer = +0
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        
        elif player == 3 and ai == 2:
            print("You Win")
            sai = +0
            splayer = +1
            print(f"----Score----\n {name}:{splayer} <---> A.I. : {sai}")
        splayer = splayer + 0
        sai = sai + 0
        break


name = input("NAME:\n")
rps()