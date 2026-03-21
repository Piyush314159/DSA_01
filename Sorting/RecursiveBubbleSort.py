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
#
a = Solution()
arr1 = [5, 3, 2, 8,1]
print(a.recursiveBubbleSort(arr1, 0, len(arr1)))
# The recursive bubble sort algorithm works by recursively comparing adjacent elements and swapping them if they are in the wrong order. 
# The process is repeated until the entire list is sorted. The base case for the recursion is when the length of the list is 1, at which point the list is already sorted.   
# The algorithm uses two parameters: i, which is the current index being compared, and n, which is the length of the list.
# The algorithm first checks if n is equal to 1, which means the list is already sorted, and returns. 
# If i is equal to n-1, it means we have reached the end of the list for the current pass, so we call the recursive function again with i