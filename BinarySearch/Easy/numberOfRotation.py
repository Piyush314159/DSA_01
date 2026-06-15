class Solution:
    def findKRotation(self, arr):
        lo, hi = 0, len(arr)-1

        while lo <= hi:
            mid = (lo + hi)//2

            if arr[0] <= arr[-1]:                   # for edge case when the array is not rotated at all, we can directly return 0
                return 0
            
            if arr[mid] > arr[(mid+1) % len(arr)]:  # the next element of mid is the smallest one, so we can directly return mid+1
                return mid+1
            
            elif arr[mid] < arr[lo]:                # the mid is in the right part, so the smallest one must be in the left part
                hi = mid-1

            else:                                   # the mid is in the left part, so the smallest one must be in the right part
                lo = mid+1
            
a = Solution()
print(a.findKRotation([1]))
print(a.findKRotation([1, 2, 3, 4, 5]))
print(a.findKRotation([5, 1, 2, 3, 4]))
print(a.findKRotation([4, 5, 1, 2, 3]))
print(a.findKRotation([3, 4, 5, 1, 2]))
print(a.findKRotation([2, 3, 4, 5, 1]))