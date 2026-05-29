# input ---> [1, 2, 8, 10, 10, 12, 19], x = 11
# output ---> 4

class Solution:
    def findFloor(self, arr, x):

        lo, hi = 0, len(arr)-1
        res = -1

        while lo <= hi:
            mid = (lo + hi)//2

            if arr[mid]<= x:
                res = mid
                lo = mid+1
            else:
                hi = mid-1
        return res

a = Solution()
print(a.findFloor([1, 2, 8, 10, 10, 12, 19], 11))