class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        
        def studentRequired(mid):
            student = 1                     # the student is already allocated the first book, so we start with 1
            pages = 0
            for i in range(len(arr)):
                if arr[i] > mid:
                    return float("inf")
                if pages + arr[i] > mid:    # if pages exceed the mid, we need to allocate the next student
                    student += 1
                    pages = 0
                pages += arr[i]
            return student
        
        lo, hi = max(arr), sum(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            students = studentRequired(mid)
            if students <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
a = Solution()
print(a.findPages([12, 34, 67, 90], 2))
print(a.findPages([15, 17, 20], 5))