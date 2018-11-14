# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        s2=""
        for i in range(len(s)-1,-1,-1):
            s2=s2+s[i]
            
        if s==s2:
            return True
        else:
            return False
        
