pin = "0805"

for my_pin in range(3):
    my_pin = input("Enter the PIN code: ")

    if pin == my_pin:
        print("Your PIN is correct!")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked...")