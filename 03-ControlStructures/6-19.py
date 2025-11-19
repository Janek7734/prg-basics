first = input("Are you interested in computer science? (y/n): ")
second = input("Do you like playing computer games? (y/n): ")
third = input("Do you have an instagram account? (y/n): ")
first_answer = first == "y"
second_answer = second == "y"
third_answer = third == "y"

print("\nSURVEY RESULTS")
print("Interested in computer science:", "Yes" if first_answer else "No")
print("Playing computer games:", "Yes" if second_answer else "No")
print("Has an Instagram account:", "Yes" if third_answer else "No")