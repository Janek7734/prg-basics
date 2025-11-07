age = int(input("Enter the age of the person: "))

if age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is a senior citizen.")