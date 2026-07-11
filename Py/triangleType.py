class Solution(object):
    def triangleType(self, nums):
        # sort nums to examine if it is a valid triangle via the inequality thereom.
        nums.sort()
        if not nums[0] + nums[1] > nums[2]:
            return "none"
        # create a set of nums, duplicates will be filtered thus we know which type of triangle it is depending on the number of unique side lengths
        uniqCh = len(set(nums))
        
        if uniqCh == 3:
            return "scalene"
        elif uniqCh == 2:
            return "isosceles"
        else:
            return "equilateral"
