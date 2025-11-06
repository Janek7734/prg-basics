###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Write yout letter: ")
print("Your letter is: ", letter)

str_number = "20303"
number = int(str_number)
print("The number is: ", number)

decimal_number = 304
binary_string = bin(decimal_number)
print("The binary representation of number ", decimal_number, "is ", binary_string)

hexadecimal_number = hex(decimal_number)
print("The hexadecimal representation of number ", decimal_number, "is ", hexadecimal_number)

euro_sign = "€"
unicode_code_point = ord(euro_sign)
print("The Unicode code point of the Euro sign is:", unicode_code_point)

number = -17
absolute_value = abs(number)
print("The absolute value of ",number, "is ", absolute_value)
