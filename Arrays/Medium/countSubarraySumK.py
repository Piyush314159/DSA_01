class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        hashmap = {0: 1}  # prefix_sum : number_of_times_seen

        for num in nums:
            prefix += num

            if prefix - k in hashmap:
                count += hashmap[prefix - k]

            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return count

s = Solution()
print(s.subarraySum([[3, 4, 7, 2, -3, 1, 4, 2], 7]))