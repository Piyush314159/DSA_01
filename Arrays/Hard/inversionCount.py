'''
Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''

class Solution:
    def inversionCount(self, arr):
        '''
        USING MERGE SORT:
        1. We can modify the merge sort algorithm to count the number of inversions in an array.
        '''
        self.count = 0                      # Initialize a count variable to keep track of the number of inversions
 
        def mergeSort(arr, l, r):

            if l>=r:                        # base case
                return 
            
            mid = (l+r)//2
            mergeSort(arr, l, mid)          # recursive call to sort the left half of the array
            mergeSort(arr, mid+1, r)        # recursive call to sort the right half of the array

            #merge inline
            left = arr[l:mid+1]
            right = arr[mid+1:r+1]

            i = 0                           #left idx
            j = 0                           #right idx
            k = l                           #merge idx

            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                    '''
                    Count inversions:
                    If left[i] > right[j], then all elements from left[i] to left[mid] will be greater than right[j],
                    because the left and right subarrays are sorted. Therefore, we can count the number of inversions
                    by adding the number of remaining elements in the left subarray (which is len(left) - i) to the count.
                    '''
                    self.count += (len(left)-i)
                k+=1
            
            while i<len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            
            while j<len(right):
                arr[k] = right[j]
                j+=1
                k+=1
        mergeSort(arr, 0, len(arr)-1)
        return self.count
    
a = Solution()
print(a.inversionCount([2, 4, 1, 3, 5]))