class Solution:
    def recusrionSum(self,n):
        if n<=0:
            return 0
        
        sum = n+self.recusrionSum(n-1)
        return sum
    
a = Solution()
print(a.recusrionSum(5))