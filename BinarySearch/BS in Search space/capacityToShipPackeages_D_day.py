class Solution:
    def leastWeightCapacity(self, arr, D):
        def shippingDays(mid):
            days = 1
            loads = 0
            for weight in arr:
                if loads + weight > mid:
                    days += 1
                    loads = 0
                loads += weight
            return days
        
        lo, hi = max(arr), sum(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            transitTime = shippingDays(mid)
            if transitTime <= D:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
a = Solution()
print(a.leastWeightCapacity([1,2,3,4,5,6,7,8,9,10], 5)) # Output: 15
print(a.leastWeightCapacity([3,2,2,4,1,4], 3)) # Output: 6
print(a.leastWeightCapacity([1,2,3,1,1], 4)) # Output: 3