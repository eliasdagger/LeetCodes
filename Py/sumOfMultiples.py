class Solution(object):
    def sumOfMultiples(self, n):
        c = 0
        # mod to ensure divisible, increment c by i 
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                c += i
                
        return c