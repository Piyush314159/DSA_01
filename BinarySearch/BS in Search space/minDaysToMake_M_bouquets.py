class Solution:
    def minDays(self, bloomDay, m, k):
        def bouquetCount(mid):
            flowers = 0
            bouquets = 0
            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets
        
        start, end = 1, max(bloomDay)

        while start < end:
            mid = (start + end) // 2
            if bouquetCount(mid) < m:
                start = mid + 1
            else:
                end = mid
        return start if bouquetCount(start) >= m else -1
    
a = Solution()
print(a.minDays([1,10,3,10,2], 3, 1)) # Output: 3
print(a.minDays([1,10,3,10,2], 3, 2)) # Output: -1