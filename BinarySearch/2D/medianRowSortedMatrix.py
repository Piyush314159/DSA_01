class Solution:    
    def median(self,mat):
            n = len(mat)
            m = len(mat[0])
            
            lo = min(row[0] for row in mat)
            hi = max(row[-1] for row in mat)
            
            required = (n * m) // 2         # The median is the (required+1)th element in sorted order.
            
            def upper_bound(row, x):
                low, high = 0, len(row)
                while low < high:
                    mid = (low + high) // 2
                    if row[mid] <= x:
                        low = mid + 1
                    else:
                        high = mid
                return low          # index of first element > x = count of elements <= x
            
            while lo < hi:
                mid = (lo + hi) // 2
                
                count = sum(upper_bound(row, mid) for row in mat)
                
                if count <= required:       # median is still to the right
                    lo = mid + 1
                else:                       # mid is at or past the median position
                    hi = mid
            
            return lo

a = Solution()
print(a.median([[1, 3, 5], [2, 6, 9], [3, 6, 9]]))  # Output: 5
print(a.median([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: 5
print(a.median([[1, 2], [3, 4]]))  # Output: 2