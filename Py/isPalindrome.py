class Solution(object):
    def isPalindrome(self, x):
        # convert to string, for negative case, -2 in itself is not a palidrome while treating -2 as a single int this would fail, so converting to a string will ensure that -12-1 is caught
        x = str(x)
        # utilise a two-pointer method to scan from either end to ensure symmetry
        l, r = 0, len(x) - 1
        while l <= r:
            if x[l] != x[r]:
                return False
            r -= 1
            l += 1
        return True
        
        """
        :type x: int
        :rtype: bool
        """
        