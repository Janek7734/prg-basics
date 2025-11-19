def f(detector):
    count = 0
    for char in detector:
        if char == "+":
            count += 1
        elif char == "-":
            count -= 1
        else:
            count += 0
        if count >= 3:
            return True
    return False

print(f("+-+++-+---"))