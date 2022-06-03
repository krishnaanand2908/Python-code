def foody_table():
    num = int(input("Enter the number of people/animals:\n"))
    namelist = []
    foodlist = []

    for i in range(0, num):
        name = input(f"Enter the name here:\n")
        food = input(f"Enter food eaten by {name}:\n")
        namelist.append(name)
        foodlist.append(food)
        
    for i in range(0, num):
        print(f"{namelist[i]} eats {foodlist[i]}")
        
def tables():
    choice2 = int(input("Enter a rational number:\n"))
    print(f"{choice2} x 1 = {choice2 * 1}")
    print(f"{choice2} x 2 = {choice2 * 2}")
    print(f"{choice2} x 3 = {choice2 * 3}")
    print(f"{choice2} x 4 = {choice2 * 4}")
    print(f"{choice2} x 5 = {choice2 * 5}")
    print(f"{choice2} x 6 = {choice2 * 6}")
    print(f"{choice2} x 7 = {choice2 * 7}")
    print(f"{choice2} x 8 = {choice2 * 8}")
    print(f"{choice2} x 9 = {choice2 * 9}")
    print(f"{choice2} x 10 = {choice2 * 10}")
    
def calcy():
    choice3 = int(input("Enter your operation here\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Remainder\n 6. Exponential Powers\n 7. Square\n 8. Cube\n"))
    num1 = float("Enter first number")
    num2 = float("Enter second number")
    if choice3 == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif choice3 == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif choice3 == 3:
        print(num1, "x", num2, "=", num1 * num2)
    elif choice3 == 4:
        print(num1, "÷", num2, "=", num1 / num2)
    elif choice3 == 5:
        try:
            if num1 > num2:
                g = num1
                s = num2
            else:
                g = num2
                s = num1
        except OverflowError:
            print("The calculated value is too large!"*100)
        print("The remainder of", num1, "and", num2, "is", g % s)
    elif choice3 == 6:
        print(num1, "raised to the power of", num2, "=", num1 ** num2)
    elif choice3 == 7:
        print("The square of", num1, "=", num1 ** 2)
        print("The square of", num2, "=", num2 ** 2)
    elif choice3 == 8:
        print("The cube of", num1, "=", num1 ** 3)
        print("The cube of", num2, "=", num2 ** 3)
        
def expo():
    try:
        base = float(input("Enter the base value here:\n"))
        power = float(input("Enter the power value here:\n"))
        print(f"{base} raise to the power of {power} is {base ** power}.")
    except OverflowError:
        print("Unable to print!\n Result too large!\n Sorry!\n")
        

