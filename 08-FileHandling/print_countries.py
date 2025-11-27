with open('countries.txt', 'r') as file:
    for index, line in enumerate(file, start=1):  
        print(f"{index}.{line}")  