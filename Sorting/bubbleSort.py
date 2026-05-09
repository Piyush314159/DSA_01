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
    #
a = Solution()
print(a.bubbleSort([5, 3, 8, 1, 2]))

# In bubble sort we comapre the elements of a unsorted array with its adjacent element upto the last unsorted element and
#  push the largest element of the unsorted elements at the end of the array, so the end of the unsorted element is being sorted with each iteration.
#  we continue this process untill the whole array is sorted.