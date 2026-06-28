class Solution(object):
    def checkIfPangram(self, sentence):
        return True if len(set(sentence)) == 26 else False
        """
        :type sentence: str
        :rtype: bool
        """
        