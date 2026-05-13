class Solution:
    def removeDuplicates(self, arr):
        seen = set()
        result = []
        for el in arr:
            if el not in seen:
                seen.add(el)
                result.append(el)

        return result
    
a = Solution()
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

