class Solution:
    def largest(self, arr):
        a = arr[0]
        for x in arr:
            if x>a:
                a=x

        return a
    
a = Solution()
print(a.largest([10]))