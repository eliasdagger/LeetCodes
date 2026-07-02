class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        # count = the sum for each i in hours such that hours[i] >= target, each employee which meets this condition will increment count by 1
        count = sum(1 for i in hours if i >= target)
        return count
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        