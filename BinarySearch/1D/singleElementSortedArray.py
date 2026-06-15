class Solution:
    def single(self, arr):
        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mid = (lo+hi)//2

            # if mid is odd, we will make it even because the intact pairs are all starts form a even index
            if mid % 2 == 1:
                mid-=1

            if arr[mid] == arr[mid+1]:
                lo = mid+2
            else:
                hi = mid
        return arr[lo]


a = Solution()
print(a.single([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]))

'''
Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
Output: 4
Explanation: 4 is the only element that appears exactly once.
'''