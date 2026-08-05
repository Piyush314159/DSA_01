class Solution:
    def generateParenthesis(self, n):
        pList = []
        def helper(current = '', openCount = 0, closeCount = 0):
            if len(current) == 2*n:
                pList.append(current)
                return

            if openCount < n:
                helper(current + '(', openCount + 1, closeCount)

            if closeCount < openCount:
                helper(current + ')', openCount, closeCount + 1)

            return pList

        return helper('', 0, 0)

sol = Solution()
print(sol.generateParenthesis(3))