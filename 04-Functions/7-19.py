def f(number):
    number = str(number)
    total = 0
    checked = ""   

    for digit in number:
        count = 0                 

        if digit not in checked:
            for d in number:
                if d == digit:
                    count += 1

            if count > 1:
                total += int(digit) * count

            checked += digit

    return total


print(f(1027))     
print(f(230335))   
print(f(513553007))
