class Solution(object):
    def removeDuplicates(self, nums):
        i = 0 
        j = len(nums)
        while (i < j):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                j -= 1
            else:
                i += 1
            

        
        """
        :type nums: List[int]
        :rtype: int
        """
        