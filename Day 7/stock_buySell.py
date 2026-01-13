def stock_buySell(prices):
    max_prof = 0
    mini = prices[0]

    for i in range(1,len(prices)):
        cost = prices[i] - mini
        max_prof = max(max_prof,cost)
        mini = min(mini, prices[i])

    return max_prof

prices = [7,1,5,3,6,4]
print(stock_buySell(prices))