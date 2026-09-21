class Solution:
    def twoOddNum(self, arr):
        xor_all = 0
        for nums in arr:
            xor_all ^= nums

        rightmost_bit = xor_all & (-xor_all)
        group_a = 0
        group_b = 0

        for nums in arr:
            if nums & rightmost_bit :
                group_a ^= nums
            else:
                group_b ^= nums

        return group_a, group_b

s = Solution()
print(s.twoOddNum([2, 3, 7, 9, 11, 2, 3, 11]))
