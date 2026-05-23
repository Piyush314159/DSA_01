"""
* Computing prefix sums     → O(n)
* Hashmap lookup/insert     → O(1)
* Overall                   → O(n)
* Space                     → O(n)
        """

class Solution:
    def maxLength(self, arr):
        max_len = 0
        curr_sum = 0
        n = len(arr)
        hashmap = {0: -1}

        for i in range(n):
            curr_sum += arr[i]

            if curr_sum in hashmap:
                max_len = max(max_len, i - hashmap[curr_sum])

            if curr_sum not in hashmap:
                hashmap[curr_sum] = i   # sum → index, not index → sum

        return max_len

a = Solution()
print(a.maxLength([10, 5, 2, 7, 1, -10, 7, 8, 10, -10])) 