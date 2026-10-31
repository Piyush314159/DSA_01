class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        bound = 0
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                bound += 1
                if bound > 1:
                    return False
        return True

s = Solution()
print(s.check([2,1,3,4]))