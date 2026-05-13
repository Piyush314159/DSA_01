class Solution:
    def isSorted(self, arr) -> bool:
        initial = arr[0]
        res = True
        for el in arr:
            if el < initial:
                res = False
            initial = el
        
        return res
    
a = Solution()
print(a.isSorted([ 4, 5, 7, 8, 14, 15, 16, 17]))