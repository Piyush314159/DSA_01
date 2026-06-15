class Solution:
    def peakElement(self, arr):
        if not arr:
            return -1

        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            right = arr[mid + 1] if mid < len(arr) - 1 else float("-inf")   # setting right side boundary to -inf
            left  = arr[mid - 1] if mid > 0             else float("-inf")  # setting left side boundary to -inf

            if arr[mid] < right:                                            #checking if the slope is rising or not
                lo = mid + 1                                                # if rising peak is in right
            else:
                hi = mid                                                    #else peak is in the left
        return lo

a = Solution()
print(a.peakElement([1, 2, 1, 3, 5, 6, 4])) 