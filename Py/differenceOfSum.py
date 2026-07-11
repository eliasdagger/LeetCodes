class Solution(object):
    def differenceOfSum(self, nums):
        elem = sum(nums)
        dig = 0 
        # nested for loop to access each index of integer within each integer of list nums 
        for idx, integer in enumerate(nums):
            # convert to string in order so we can iterate by index
            num = str(integer)
            for i in range(len(num)):
                dig += int(num[i])
                
        return abs(elem - dig)
        