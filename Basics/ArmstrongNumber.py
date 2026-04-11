class Solution:
    def armstrongNumber (self, n):
        sum=0
        p = len(str(n))

        for digit in str(n):
            sum += int(digit) ** p

        return sum==n
    
a = Solution()
print(a.armstrongNumber(9474))