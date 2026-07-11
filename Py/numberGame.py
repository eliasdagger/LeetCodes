class Solution(object):
    def numberGame(self, nums):
        arr = []
        # sort nums in reverse in order to access lowest val via pop() method
        nums.sort(reverse=True)
        
        # continue the rules of the game
        while len(nums) != 0:
            alice = nums.pop()
            bob = nums.pop()
            
            arr.appenSd(bob)
            arr.append(alice)
        return arr