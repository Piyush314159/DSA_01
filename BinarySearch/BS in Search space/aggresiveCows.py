class Solution:
    def maxDistance(self, arr, k):
        arr.sort()
        def placedCows(mid):
            dist = 0
            cow = 1
            for i in range(len(arr)-1):
                dist += arr[i+1] - arr[i]
                if dist >= mid:
                    cow += 1
                    dist = 0
            return cow
        
        start, end = 1, max(arr) - min(arr)         # minimum distance can't be zero, meaning less

        while start < end:
            mid = (start + end + 1) // 2            # +1 to avoid infinite----> floor division with start = mid trap
            cows = placedCows(mid)
            if cows >= k:
                start = mid 
            else:
                end = mid - 1 
        return start 
    
a = Solution()
print(a.maxDistance([0,3,4,7,10,9], 4))