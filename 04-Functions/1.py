def f(amount_to_pay):
    amount5 = amount_to_pay // 5
    amount_to_pay = amount_to_pay - amount5 * 5
    amount2 = amount_to_pay // 2
    amount_to_pay = amount_to_pay - amount2 * 2
    amount1 = amount_to_pay

    return amount5 + amount2 + amount1

print(f(23))