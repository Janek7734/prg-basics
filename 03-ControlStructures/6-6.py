time = int(input("Enter the number of parking hours: "))

if time <= 0:
    print("Invalid time entered.")
elif time <= 2:
    print("Parking fee is 5 PLN.")
elif time <= 6:
    print("Parking fee is 15 PLN.")
else:
    print("Parking fee is 20 PLN.")
