class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def helper(n):
            if n == 0:
                return 1
            if n == 1:
                return 5  # 0, 2, 4, 6, 8
            if n == 2:
                return 20  # (5 choices for even) * (4 choices for odd)

            half_n = n // 2
            if n % 2 == 0:
                return (helper(half_n) ** 2) % (10**9 + 7)
            else:
                return (helper(half_n) * helper(half_n + 1)) % (10**9 + 7)

        return helper(n) % (10**9 + 7)

sol = Solution()
# Test cases
print(sol.countGoodNumbers(1))  # Output: 5
print(sol.countGoodNumbers(2))  # Output: 20
print(sol.countGoodNumbers(100))  # Output: 100