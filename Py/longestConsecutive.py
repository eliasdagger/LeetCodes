class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count start at 0 for empty set case
        c = 0
        # sort in order and remove duplicates
        n = sorted(set(nums))
        for i in range(len(n)):
            c2 = 1
            # start index + 1 from where we left off
            for j in range(i + 1, len(n)):
                # if n[j - 1] is greater than its previous then increment
                if n[j] == n[j - 1] + 1:
                    c2 +=1
                # not consecutive case, break immediately
                else:
                    break
            # if this iters count is greater than max count than rewrite it
            if c2 > c:
                c = c2
        return c