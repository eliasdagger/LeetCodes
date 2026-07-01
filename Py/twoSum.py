class Solution(object):
    def twoSum(self, nums, target):
        # nested loop strategy allows us to skip index to ensure indices are not duplicates
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[j] + nums[i] == target:
                    return [j,i]
        # if loop breaks without appending values, there is no solution thus we will return empty res
        return []