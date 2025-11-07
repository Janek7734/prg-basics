###
# Sums numbers entered by user
#
total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number

print(f"The total sum of the numbers is: {total_sum}")

# Sums numbers entered by user and calculates their arithmetic mean

total_sum = 0
count = 0  # To count how many numbers were entered

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    
    total_sum += number
    count += 1

# After the loop, calculate the mean if at least one number was entered
if count > 0:
    mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")
