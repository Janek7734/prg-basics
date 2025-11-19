def f(number, even):
    sum_digits = 0
    for digit in str(number):
        i = int(digit)
        if even == True:
            if i % 2 == 0:
                sum_digits += i
            else:
                sum_digits += 0
        else:
            if i % 2 == 1:
                sum_digits += i

    return sum_digits

print(f(3124, True))
print(f(3124, False))