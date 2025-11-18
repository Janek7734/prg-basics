number = input("Enter EAN-13 article number: ")
digits = len(number)
if digits == 13:
    print("Article number is correct.")

    if number[0:3] == "590":
        print("Article manufactured in Poland.")

else:
    print("Incorrect article number.")

