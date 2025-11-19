def f(amount_to_pay):
    oryginal_amount = amount_to_pay
    amount5 = amount_to_pay // 5
    amount_to_pay = amount_to_pay - amount5 * 5
    amount2 = amount_to_pay // 2
    amount_to_pay = amount_to_pay - amount2 * 2
    amount1 = amount_to_pay

    result = amount5 + amount2 + amount1
    print(f"f({oryginal_amount}) returns {result}")

f(23)