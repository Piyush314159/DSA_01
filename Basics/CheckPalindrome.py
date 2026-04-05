class Solution:
    def isPalindrome(self, x):
        return str(abs(x)) == str(abs(x))[::-1]
    
a = Solution()
print(a.isPalindrome(-121))