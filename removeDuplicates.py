
def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        print(f"i = {i}, j = {j}")
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicates([1,1,2,2,3,4,5,6,6,6]))