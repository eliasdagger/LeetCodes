
def searchInsert(nums, target):
    # Set up two pointers for the binary search
    l, r = 0, len(nums) - 1

    while l <= r:
        # Find middle index, l is set to the left boundary then add half the distance to the second boundary r, to find the middle index in a dynamic manner to complement the while loop
        mid = l + ((r - l) // 2)
        print(mid)
        if target > nums[mid]:
            # change l to mid + 1 since we know that mid is not == target, else this would create an infinite loop
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            return mid
    # Binary searches index will finish after the index if right boundary is changed and vice versa  
    return mid + 1 if target > nums[mid] else mid
    
print(searchInsert([1, 3, 5, 6], 2))