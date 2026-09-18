class Solution:
    def isPowerofTwo(self, n):
        return (n &(n-1)) == 0 

s = Solution()
print(s.isPowerofTwo(16))

def ispower1(n):
    if n < 1:
        return False

    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2 
    return True

print(ispower1(16))