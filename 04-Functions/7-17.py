def f(palindrome):
    palindrome = str(palindrome)
    if palindrome[0:] == palindrome[::-1]:
        return True
    else:
        return False
    
print(f("radar"))
print(f("12-11-21"))
print(f("book"))
