
def maxSum(nums, k, mul):
    s = 0
    nums.sort()

    for i in range(-1, -(k+1), -1): 
        s += max(nums[i], nums[i] * mul)
        mul -= 1
    return s
print(maxSum([6,1,2,9], 3, 2))