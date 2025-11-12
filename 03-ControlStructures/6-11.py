previous_price = float(input("Enter the previous price of the item: "))
current_price = float(input("Enter the current price of the item: "))   
if current_price < previous_price:
    discount = previous_price - current_price
    discount_percentage = (discount / previous_price) * 100
    print(f"Vurrent product price: {current_price}")
    print(f"Previous product price: {previous_price}")
    print(f"Buy the product!!")
    print(f"Product price reduced by {discount_percentage}%")
else:
    print("No discount available.")