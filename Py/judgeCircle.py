class Solution(object):
    def judgeCircle(self, moves):
        # if opposite direction moves are made equally they cancel eachother out thus we are still at the centre. 
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
