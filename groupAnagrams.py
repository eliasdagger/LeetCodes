class Solution(object):
    def groupAnagrams(self, strs):
        ga = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in ga:
                ga[sorted_word] = []
            
            ga[sorted_word].append(word)




        return list(ga.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        