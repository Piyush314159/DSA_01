class Solution:
    def firstSearch(self, arr, k):

        lo, hi = 0, len(arr)-1
        res = -1

        while lo <= hi:
            mid = (lo+hi)//2            # dividing into two halves

            if arr[mid]==k:
                res = mid
                hi = mid-1              # continuously seraching for any previous occurances of k

            elif arr[mid]<k:
                lo = mid+1              # if k is greater than mid, then k resides in the right so we will move to right by moving lo = mid+1

            else:
                hi = mid-1              # if k is smaller than mid, then k resides in the left so we will move to left by moving hi = mid-1
        
        return res



a = Solution()
print(a.firstSearch([1, 2, 3, 4, 5], 4))