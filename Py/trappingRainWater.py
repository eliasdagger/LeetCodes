def trap(height: List[int]) -> int:
    l = 0
    r = 1
    res = 0
    while r < len(height):
        if l < r:
            l += 1
            r += 1
            continue
        if r
        
        for i in range(l, r):


    pass



print(trap([0,2,0,3,1,0,1,3,2,1]))