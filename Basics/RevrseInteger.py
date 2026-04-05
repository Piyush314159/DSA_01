class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        y=abs(x)
        
        if y==0:
            return 0
        
        while y>0:
            rev = rev * 10 + y % 10
            y=y//10
        
        result = -rev if x<0 else rev

        if result < -(2**31) or result > ((2**31)-1):
            return 0
        
        return result
    
a = Solution()
print(a.reverse(-123))
        