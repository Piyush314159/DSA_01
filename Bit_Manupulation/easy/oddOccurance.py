'''
-> x ^ x = 0
-> x ^ 0 = x
we did xor of all el in list which occurs odd numbers of time it willl survive
'''

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for nums in nums:
            result ^= nums
        return result

s = Solution()
print(s.singleNumber([4,5,3,4,3,5,3,3,5]))