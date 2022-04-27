num = int(input("Enter a natural number: "))
namelist = []
foodlist = []

for i in range(0, num):
    name = input("Enter name: ")
    food = input(f"Enter food eaten by {name}: ")
    namelist.append(name)
    foodlist.append(food)
    
for i in range(0, num):
    print(f"{namelist[i]}       {foodlist[i]}")