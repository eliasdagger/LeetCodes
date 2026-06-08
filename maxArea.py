def maxArea(heights: List[int]) -> int:
    area = 0
    f = 0
    r = len(heights) - 1
    while f < r: 
        temp = (r - f) * min(heights[f], heights[r])
        print(f"Front: {heights[f]}cm @ {f} - Rear: {heights[r]}cm @ {r} - Area: {temp}")
        if temp > area: 
            area = temp
        if heights[f] < heights[r]:
            f += 1
        else : 
            r -= 1
    return area


print(maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))