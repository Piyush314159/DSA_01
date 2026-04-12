class Solution:
    def N_times(self,n):
        if n<=0:
            return
        self.N_times(n-1)
        print(n)

a = Solution()
a.N_times(5)