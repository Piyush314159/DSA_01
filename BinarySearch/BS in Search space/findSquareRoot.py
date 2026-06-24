class Solution:
    def floorSqrt(self, n): 

        if n == 0 or n == 1:
            return n
        lo, hi, ans = 1, n, 1
        
        while lo <= hi:
            mid = (lo+hi)//2

            if mid*mid == n:            #only return mid if n is a perfect square
                return mid
            elif mid*mid < n:
                ans = mid               # ans holds the best answer so far, as mid*mid < n
                lo = mid+1
            else:
                hi = mid-1
        return ans
    
a = Solution()
print(a.floorSqrt(4))  # Output: 2
print(a.floorSqrt(8))  # Output: 2
print(a.floorSqrt(9))  # Output: 3
print(a.floorSqrt(15))  # Output: 3
print(a.floorSqrt(16))  # Output: 4
print(a.floorSqrt(25))  # Output: 5
