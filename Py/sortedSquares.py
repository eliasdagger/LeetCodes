class Solution(object):
    def sortedSquares(self, nums):
        # square entries then sort
        return sorted([x**2 for x in nums])
        