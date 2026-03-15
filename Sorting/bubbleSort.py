class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(0,n):
            swapped = False
            for j in range(0,n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
a = Solution()
print(a.bubbleSort([5, 3, 8, 1, 2]))