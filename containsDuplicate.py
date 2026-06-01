class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create a set of nums, removing duplicates
        dict = set(nums)
        # if there was a duplicate then dict would be less than nums
        if len(dict) < len(nums):
            return True
        return False
        