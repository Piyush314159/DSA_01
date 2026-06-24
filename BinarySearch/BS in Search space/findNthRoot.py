class Solution:
    def nthRoot(self, n, m):
        if m==0 or m==1:
            return m
        
        def power(x, n):
            result =1
            for _ in range(n):
                result *= x
                if result > m:      # break if result is greater than m
                    break
            return result
        
        lo, hi = 1, m
        while lo<=hi:
            mid = (lo+hi)//2
            val = power(mid, n)
            if val == m:
                return mid
            elif val < m:
                lo = mid+1
            else:
                hi = mid -1
        return -1

a = Solution()
print(a.nthRoot(3, 27))  # Output: 3
print(a.nthRoot(4, 16))  # Output: 2
print(a.nthRoot(5, 32))  # Output: 2
print(a.nthRoot(3, 9))