def f(x, y):
    total = 0
    for n in range(x, y + 1):
        if n % 6 == 0 and n % 4 != 0:
            total += n
    return total

print(f(1,20))
print(f(10,30))