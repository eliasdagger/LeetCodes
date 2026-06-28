# Did not complete
def maxSubarraySum(nums, k):
    total = 0
    l, r = 0, 0
    if max(nums) < 0:
            total += -(-max(nums) // k)
    else:
        while r < len(nums) - 1:   
            print(f"l = {l} r = {r}")  
            if nums[r + 1] >= 0:
                total = max(total, sum(nums[l:r]) * k)

                r += 1
                print(f"total = {total} ss = {nums[l:r]}")       
            else:
                l += 1
                r += 1
    return total

print(maxSubarraySum([1,-2,3,4,-5], 2))

