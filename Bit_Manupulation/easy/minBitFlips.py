'''
number of 1's in the xor of two number gives us minimum how many bits we have to flip go from one number to another
'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start^goal).count('1')

s = Solution()
print(s.minBitFlips(10700,7))