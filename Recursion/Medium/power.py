class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1

        if n == 1:
            return x

        if n < 0:
            x, n = 1 / x, -n  # x^(-n) = (1/x)^n
        
        return x * self.myPow(x, n-1) 

sol = Solution()
print(sol.myPow(2, -3))