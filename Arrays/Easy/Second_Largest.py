class Solution:
    def getSecondLargest(self, arr):
        first = second = -1
        for x in arr:
            if x > first:
                second = first
                first = x
            elif x > second and x != first:
                second = x
        return second
    
a = Solution()
print(a.getSecondLargest([12, 35, 1, 10, 34, 35]))