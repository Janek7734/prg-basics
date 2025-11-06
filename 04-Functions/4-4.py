###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number_str = str(abs(number))
    total_sum = 0
    for digit_char in number_str:
        total_sum += int(digit_char)
    return total_sum

any_number = int(input('Enter an integer number: '))
result = sum_digits(any_number)
print("The sum of the digits in the number", any_number, "is:", result)
