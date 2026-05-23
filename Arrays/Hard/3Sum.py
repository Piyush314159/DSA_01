class Solution:
    def threeSum(self, nums):
        res = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in seen:
                    res.add(tuple(sorted((nums[i], nums[j], third))))
                seen.add(nums[j])
        return [list(t) for t in res]
    
a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))