class Solution(object):
    def isAnagram(self, s, t):
        # simply, if one string is an anagram of another, they must contained the same chars, if the sorted versions are identical, then they contain all the same chars.
        return sorted(s) == sorted(t)