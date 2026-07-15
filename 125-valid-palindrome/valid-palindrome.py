class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=""
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                x=x+i
        x=x.lower()
        a=x
        x=x[::-1]
        if a==x:
            return True
        else:
            return False
