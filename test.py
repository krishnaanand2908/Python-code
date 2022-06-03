def expo1():
    try:
        base = int(input("Enter the base value here:\n"))
        power = int(input("Enter the power here:\n"))
        print(f"{base} raise to the power of {power} is {base ** power}")
    except OverflowError:
        print("Calculated value too large!"*100)
        
expo1()