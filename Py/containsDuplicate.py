class Solution(object):
    def containsDuplicate(self, nums):
        # utilise a set which contains only unique values, if the len of this set is different then the len of nums, nums had inunique values, thus false, else tr
        return len(set(nums)) != len(nums)