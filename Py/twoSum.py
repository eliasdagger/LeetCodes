class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        for i in range(len(nums)):
        
            j = i + 1
            while j < len(nums):
                if nums[i] +  nums[j]==target:
                    return [j,i]
                    
                j += 1
            i+=1
        return sumList
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        