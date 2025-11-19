n = int(input("Enter month number: "))

def month(n):
    months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if 1 <= n <= 12:
        print(f"The name of month {n} is {months[n-1]}")
    else:
        print("Incorrect value.")

month(n)