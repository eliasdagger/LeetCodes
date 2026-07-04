class Solution(object):
    def isMiddleElementUnique(self, nums):
        # find the middle element
        mid = len(nums) // 2
        val = nums[mid]
        
        # return count of mid num == 1
        return nums.count(val) == 1
            
            