class Solution(object):
    def addDigits(self, num):
        # base case
        if num == 0:
            return 0

        # 
        return 1 + (num - 1) % 9