class Solution(object):
    def countDigits(self, num):
        # create a string rep of the number to gain the ability to iterate through the int 
        div = str(num)
        c = 0

        # for each index of div, if num is divisible increment count
        for i in range(len(div)):
            if num % int(div[i]) == 0:
                c += 1
        return c
