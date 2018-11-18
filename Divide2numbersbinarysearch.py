class Solution(object):
    def divide(self, dividend, divisor):
        res=0
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend == 0:
            return 0
        flag = -1
        if (dividend<0 and divisor<0) or (dividend>0 and divisor>0):
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:            
            if flag == 1:
                if dividend > 2**31-1:
                    return 2**31-1
                return dividend
            if flag == -1:
                if dividend < -2**31:
                    return -2**31
                return dividend*flag
        res = 0
        while dividend >= divisor:
            count = 1
            mid = divisor
            while dividend >= mid:
                dividend = dividend - mid
                res += count
                count = count << 1
                mid = mid << 1
        return flag*res
            
        
