class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        table = {}
        c = 0

        for el in nums:
            if el in table:
                table[el] += 1
            else:
                table[el] = 1

        for num,count in table.items():
            if count == 3:
                lst = []
                for i in range(n):
                    if nums[i] == num:
                        lst.append(i)

                if (lst[1] - lst[0]) == (lst[2] -lst[1]):
                    c += 1
        return c