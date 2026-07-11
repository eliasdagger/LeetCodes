class Solution(object):
    def findWordsContaining(self, words, x):
        # if char in word append list index
        res = []
        for idx, s in enumerate(words):
            if x in s:
                res.append(idx)
        return res
        