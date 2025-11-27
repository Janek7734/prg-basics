def f(card_number):
    if len(card_number) == 16:
        return card_number[0:2] + "**********" + card_number[12:]
    else:
        return "Invalid card number!"
    
print(f("5290312400019022"))