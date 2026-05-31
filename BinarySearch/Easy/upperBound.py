class Solution:
    def upperBound(self, arr, x):
        lo, hi = 0, len(arr)-1
        res = -1

        while lo <= hi:
            mid = (lo + hi)//2
            '''
            we are checking for the condition arr[mid] >= x because we want to find the upper bound of x in the sorted array.
            If arr[mid] is greater than or equal to x, it means that the upper bound of x could be at mid or to the left of mid.
            Therefore, we update res to mid and continue searching in the left half of the array by setting hi to mid - 1.
            If arr[mid] is less than x, it means that the upper bound of x must be to the right of mid,
            so we update lo to mid + 1 to continue searching in the right half of the array.
            '''
            if arr[mid] >= x:
                res = mid
                hi = mid - 1
            else:
                lo = mid+1
        return res
    
a = Solution()
print(a.upperBound([1,4,6,7,8,9,10], 5)) #sorted array