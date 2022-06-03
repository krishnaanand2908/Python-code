import random
import os
import fontstyle

os.system("cls")
bss_logo = fontstyle.apply("Welcome to BSS!", "bold/Italic/DARKCYAN/green_BG")
hehe = fontstyle.apply("|---Please come again soon---|", "bold/Italic/black")
print(bss_logo)

name = str(input("Please enter your name here:\n"))
sex = str(input("Please enter your sex here [F\M]:\n"))
sex = sex.upper()

if sex == "F":
    print(f"Hi Ms\Mrs. {name}!\n Please select where you want to go:\n [1. Fun Corner\n 2. Study Corner]")
elif sex == "M":
    print(f"Hi Mr. {name}!\n Please select where you want to go:\n [1. Fun Corner]\n [2. Study Corner]")
else:
    print(hehe)
choice = int(input())

if choice == int(1):
    print("1. Foody Table\n 2. Guess the number\n 3. Number Fight\n")
    game_choice = int(input(":"))
    if game_choice == 1:
elif choice == int(2):
    print("1. Math Help\n 2. Quiz\n 3. Animal's Info\n")
    study_choice = int(input(":"))
else:
    print(hehe)


    
    
    






