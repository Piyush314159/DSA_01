class Solution:
    def findMin(self, arr):
        lo, hi = 0, len(arr)-1

        while lo < hi :
            mid = (lo + hi)//2

            if arr[mid] > arr[hi]:
                lo = mid +1
            else:
                hi = mid
        return arr[lo]
                
a = Solution()
print(a.findMin( [4, 2, 3]))

'''
Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array.
'''