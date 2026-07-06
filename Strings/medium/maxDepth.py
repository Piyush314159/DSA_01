class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s) == 0:
            return 0
        depth = 0
        maxdepth = 0
        for ch in s:
            if ch == "(":
                depth += 1
                maxdepth = max(maxdepth, depth)
            elif ch == ")":
                depth -= 1
        return maxdepth
a = Solution()
print(a.maxDepth("(1+(2*3)+((8)/4))+1"))