class Solution:
    def recursiveInsertionSort(self,arr,i,n):
        if n==1:
            return
        if i==n:
            return
        key = arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        self.recursiveInsertionSort(arr,i+1,n)

        return arr
    
a = Solution()
arr1 = [5, 3, 2, 8,1]
print(a.recursiveInsertionSort(arr1, 0, len(arr1)))