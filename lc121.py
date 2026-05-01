
# LC 121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Pattern: One Pass / Greedy
# Time: O(n) 
# Space: O(1)

prices = [7, 1, 5, 3, 6, 4]

# assume day 1 is the cheapest day to buy
buying_price = prices[0]

# if no profit exists, return 0 
max_profit = 0

# start from day 2 (index 1) because day 1 is already our buy day
for i in range(1, len(prices)):

    # if I sell today, what's my profit?
    profit = prices[i] - buying_price

    # is this the best profit we've seen so far?
    max_profit = max(max_profit, profit)

    # is today cheaper than what we bought at?
    # if yes, update our buy day
    if prices[i] < buying_price:
        buying_price = prices[i]

print(max_profit)