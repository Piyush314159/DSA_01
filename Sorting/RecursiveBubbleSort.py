class Solution:
    def recursiveBubbleSort(self, arr, i, n):

        if n==1:
            return
        
        if i==n-1:
            self.recursiveBubbleSort(arr,0,n-1)
            return

        if arr[i+1]<arr[i]:
            arr[i+1],arr[i] = arr[i],arr[i+1]

        self.recursiveBubbleSort(arr,i+1,n)

        return arr

a = Solution()
arr1 = [5, 3, 2, 8,1]
print(a.recursiveBubbleSort(arr1, 0, len(arr1)))