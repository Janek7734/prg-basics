def f(expression):
    result = int(expression[0])
    
    for i in range(1, len(expression), 2):
        operator = expression[i]
        number = int(expression[i+1])
        
        if operator == "+":
            result += number
        elif operator == "-":
            result -= number

    return result


print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))

