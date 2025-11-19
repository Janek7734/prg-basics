###
# Functions to read any data type from the keyboard
#
def input_string(message):
    text = input(message)
    return text

def input_integer(message):
    number = int(input(message))
    return number

def input_real(message):
    real_number = float(input(message))
    return real_number

def input_boolean(message):
    answear = input(message)
    return answear == "y"

