def f(dice):
    longest_digit = dice[0]
    longest_count = 1
    current_digit = dice[0]
    current_count = 1

    for i in dice[1:]:
        if  i == current_digit:
            current_count += 1
        else:
            if current_count > longest_count:
                longest_count = current_count
                longest_digit = current_digit
            current_digit = i
            current_count = 1

    if current_count > longest_count:
        longest_digit = current_digit

    return int(longest_digit)


print(f("5233165554211"))  
print(f("2133"))           
