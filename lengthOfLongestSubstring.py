class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0,0
        res = 0
        while r < len(s):
            if len(set(s[l:r+1])) > len(set(s[l:r])):
                r += 1
                
            else:
                l += 1
            res = max(res, r - l)

        return res