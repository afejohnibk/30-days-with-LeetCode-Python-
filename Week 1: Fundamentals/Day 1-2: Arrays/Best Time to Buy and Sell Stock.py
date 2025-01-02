"""
 Assuming our price list is [4,6,1,7,2]
 To begin we need to set our profit to 0
 And our buy to the first price
 After which we iterate through the prices from day 2 since we can't sell on the first day
 Then we check if the sell price is greater than the buy price
 If so we keep the profit
 Else our sell will become our new buy price
"""


def maxProfit(prices):
    profit = 0
    buy_stock = prices[0]
    for sell in prices[1:]:
        if sell > buy_stock:
            profit = max(profit, sell - buy_stock)
        else:
            buy_stock = sell
    return profit


prices = [4, 6, 1, 7, 2]
print(maxProfit(prices))
