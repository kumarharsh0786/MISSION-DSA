
def minimumLoss(price):
    n = len(price)
    prices_with_year = [(p, i) for i, p in enumerate(price)]
    prices_with_year.sort(key=lambda x: x[0])  
    min_loss = float('inf')
    for i in range(1, n):
        curr_price, curr_year = prices_with_year[i]
        prev_price, prev_year = prices_with_year[i - 1]
        if curr_year < prev_year:
            loss = curr_price - prev_price
            if loss < min_loss:
                min_loss = loss

    return min_loss
