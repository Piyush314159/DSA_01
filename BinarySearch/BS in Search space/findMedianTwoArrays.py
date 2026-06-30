class Solution:
    def medianOf2(self, a, b):
        median = int((len(a) + len(b)) / 2)

        lo, hi = max(0, median-len(b)), min(median, len(a))

        while lo <= hi:
            i = (lo+hi)//2
            j = median-i

            a_left  = a[i-1] if i > 0 else float('-inf')
            a_right = a[i]   if i < len(a) else float('inf')
            b_left  = b[j-1] if j > 0 else float('-inf')
            b_right = b[j]   if j < len(b) else float('inf')

            if a_left >= b_right:            # toomedian too many from a
                hi = i- 1
            elif b_left >= a_right:          # toomedian too many from b
                lo = i+1
            else:                           # valid partition
                return(min(a_right, b_right))

a = Solution()
print(a.medianOf2([2, 3, 6, 7, 9], [1, 4, 8, 10])) #answer is 6