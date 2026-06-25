class Solution:
    def kokoEat(self, arr, k):
        
        def totalHour(mid):
            """
        - Binary search on speed s in [1, max(arr)]; find minimum s where total hours <= k.
        - Hours per pile = ceil(pile/s) because leftover bananas still cost a full hour.
        - ceil without math: (pile + s - 1) // s — adds s-1 to nudge remainders up without skipping a floor.
        """
            hour = 0
            for pile in arr:
                hour += (pile + mid -1)//mid
            return hour
        
        lo, hi = 1, max(arr)
        while lo < hi:
            mid = (lo + hi)//2
            time = totalHour(mid)
            if time <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

a = Solution()
print(a.kokoEat([3,6,7,11], 8)) # Output: 4