"""
You are gievn an array "prices" where "prices[i]" is the price of a given stock on the ith day
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit return 0


Profit = rightPointer (day sold) - leftPointer (day bought)
input: Prices = [7, 1,  5, 3, 6, 4]
output: 5
Explanation: buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5

Example 2:
Input = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


from typing import List


def maxProfit(prices: List[int]):
    left = 0
    right = 1
    profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = max(profit, prices[right] - prices[left])
        else:
            # left pointer will equal right pointer value because we found the new lowest value in the prices
            # list
            left = right
        # regardless of conditions, we need the right pointer to continue to iterate through the list
        right += 1
    return profit


array = [7, 6, 4, 3, 1]
maxProfit(array)
