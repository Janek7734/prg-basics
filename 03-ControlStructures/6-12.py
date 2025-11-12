products = int(input("Enter the number of purchased products: "))
price = float(input("Enter the price per product: "))
total_cost = products * price  
if products > 2:
    total_cost = 2 * price + (products - 2) * price * 0.75
    print(f"The total cost of the purchase is: {total_cost}") 
else:
    print(f"The total cost of the purchase is: {total_cost}")