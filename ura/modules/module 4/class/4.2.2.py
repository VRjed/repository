def final_price(n, discount=1):
    c = n * (1 - (discount/100))
    if discount > 100:
        return 0
    else:
        return c