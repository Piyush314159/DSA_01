class Solution:
    def searchInsertK(self, arr, k):
        lo, hi = 0, len(arr) - 1
        pos = len(arr)  # Default position is the end of the array

        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]>k:
                pos = mid
                hi = mid-1
            else:
                lo = mid+1
        return pos
    
a = Solution()
print(a.searchInsertK([1, 3, 5, 6], 2))