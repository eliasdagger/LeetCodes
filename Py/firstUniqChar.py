class Solution(object):
    def firstUniqChar(self, s):
        # create a hash map with key(char):value(frequency) --> {'a': 2, 'b': 1, ...}
        c = collections.Counter(s)
        # if frequency of char is one then first unique char so return index
        for idx, char in enumerate(s):
            if c[char] == 1:
                return idx
        return -1