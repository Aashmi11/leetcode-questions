class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        x=0
        for customer in accounts:
            total= sum(customer)
            if total > x:
                x=total
        return x