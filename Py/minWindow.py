


def minWindows(s: str, t: str) -> str:
    # base case: if s is shorter than t, its impossible for substring to exist
    if len(s) < len(t):
        return ""

    res = {}
    count1 = {}
    # Sliding window technique, set two pointers left and right
    l, r = 0, 0

    # create a hash table of chars in t mapped to their frequency (handles duplicates). 
    for c in t:
        count1[c] = 1 + count1.get(c, 0)

    need, have = len(count1), 0

    while r < len(s):
        if s[l] not in count1:
            l += 1
            r += 1
            continue

        if 



    

    

    

    

    
    
    while r < len(s):

print(minWindow())