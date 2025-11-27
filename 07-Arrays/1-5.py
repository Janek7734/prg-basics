arr = [1, 2, 3, 4, 5]

while True:
    print("\nCurrent array:", arr)
    
    print("0. Exit")
    print("1. Subtraction (-)")
    print("2. Addition (+)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Show array")

    operation = int(input("Choose operation: "))

    if operation == 0:
        print("Goodbye!")
        break

    if operation == 5:
        print("Array:", arr)
        continue

    number = int(input("Which number do you want to change? (1–5) "))

    if number < 1 or number > 5:
        print("Invalid index!")
        continue

    value = arr[number - 1]   

    if operation == 1:
        subtract = int(input("How much do you want to subtract? "))
        arr[number - 1] = value - subtract

    elif operation == 2:
        add = int(input("How much do you want to add? "))
        arr[number - 1] = value + add

    elif operation == 3:
        multiplication = int(input("By how much do you want to multiply? "))
        arr[number - 1] = value * multiplication

    elif operation == 4:
        division = int(input("By how much do you want to divide? "))
        if division == 0:
            print("Error: division by zero!")
            continue
        arr[number - 1] = value / division

    else:
        print("Error: wrong option!")

