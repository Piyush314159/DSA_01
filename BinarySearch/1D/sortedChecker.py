class Solution:
    def isSorted(self, arr) -> bool:

        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False

        return True
    
a = Solution()
print(a.isSorted([90, 80, 100, 70, 40, 30]))