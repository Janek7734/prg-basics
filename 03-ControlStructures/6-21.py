amount = int(input("Enter the amount in PLN: "))
oryginal_amount = amount

amount5 = amount // 5
amount = amount - amount5 * 5
amount2 = amount // 2
amount = amount - amount2 * 2
amount1 = amount

print(f"\nThe amount of PLN {oryginal_amount} in coins: ")
print(f"\n5 PLN coins: {amount5}")
print(f"\n2 PLN coins: {amount2}")
print(f"1 PLN coins: {amount1}")
