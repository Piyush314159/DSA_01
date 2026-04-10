class Solution:
    def isPalindrome(self,s):
        reversed = str(abs(s))[::-1]
        return str(abs(s))==reversed
    
a = Solution()
print(a.isPalindrome(-123241))