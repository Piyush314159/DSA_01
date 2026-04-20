class Solution:
    def frequencyOfOccurance(self, arr):
        occ = {}
        for el in arr:
            occ[el] = occ.get(el, 0) + 1

        max_freq = max(occ.values())
        element = max(occ, key=occ.get)

        return element, max_freq


a = Solution()
print(a.frequencyOfOccurance([2, 3, 2, 3, 5]))