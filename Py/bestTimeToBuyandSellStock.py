
def maxProfit(prices):
    maxP = 0
    i = 0
    j = 1
    while j < len(prices):
        sum = prices[j] - prices[i]

        if prices[j] < prices[i]:
            i = j
            j += 1
        else:
            j += 1
            maxP = max(maxP, sum)

    return maxP

print(maxProfit([7,1,5,3,6,4]))
        