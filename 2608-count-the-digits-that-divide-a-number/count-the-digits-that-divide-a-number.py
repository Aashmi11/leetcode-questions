class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp=num
        ans=0
        while temp>0:
            r = temp%10
            if num%r==0:
                ans+=1
            temp//=10
        return ans