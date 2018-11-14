# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321

class Solution(object):
    def reverse(self, x):
        g=pow(2,31)
        b=0
        """
        :type x: int
        :rtype: int
        """
        
        
        i=abs(x)*10
        while i>0:
            b=b*10
            b=b+i%10
            i=i//10
        
        if b>g-1 :
            b=0        
        
        if x<0:
            return -b
        else:
            return b   
