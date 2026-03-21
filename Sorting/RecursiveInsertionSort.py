class Solution:
    def recursiveInsertionSort(arr,i,n):
        if i>=n:
            return
        
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

        Solution.recursiveInsertionSort(arr,i+1,n)
        return arr
a = Solution()
arr1 = [5, 3, 2, 8,1]
print(Solution.recursiveInsertionSort(arr1, 1, len(arr1)))
# The recursive insertion sort algorithm works by recursively sorting the first i-1 elements of the list