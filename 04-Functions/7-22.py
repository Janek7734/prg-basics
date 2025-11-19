def f(name):
    words = name.split()
    result = " "
    for i in words:
        result += i[0]
    return result
    
print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))

