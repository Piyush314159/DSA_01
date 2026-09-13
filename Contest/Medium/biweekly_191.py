class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        def is_equally_spaced(idxs):
            if len(idxs) < 3:
                return False

            diff = idxs[1] - idxs[0]
            for i in range(2,len(idxs)):
                if idxs[i] - idxs[i-1] != diff:
                    return False
            return True

        positions = {}
        for i, num in enumerate(nums):
            positions.setdefault(num,[]).append(i)

        c = 0
        for num, idxs in positions.items():
            if is_equally_spaced(idxs):
                c += 1
        return c