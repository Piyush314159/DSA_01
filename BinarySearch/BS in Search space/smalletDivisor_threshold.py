class Solution:
    def smallestDivisor(self, nums, threshold):
        def divSum(mid):
            res = 0
            for num in nums:
                res += (num + mid -1) // mid           #they are asking for the ceilng of every division to add
            return res
        
        start, end = 1, max(nums)

        while start < end:
            mid = (start + end) // 2

            if divSum(mid) <= threshold:
                end = mid
            else:
                start = mid+1

        return start
    
a = Solution()
print(a.smallestDivisor([1,2,5,9], 6)) # Output: 5
print(a.smallestDivisor([2,3,5,7,11], 11)) # Output: 3