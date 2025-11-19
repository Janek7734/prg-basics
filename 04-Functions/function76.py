def hide(card_number):
    if len(card_number) == 16:
        return card_number[:2] + "**********" + card_number[12:]
    else:
        return "Invalid card number."
