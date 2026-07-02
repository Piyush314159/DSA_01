class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in '13579':
                return (num[0:i+1])
        return ""

a = Solution()
print(a.largestOddNumber("52"))  # Output: "5"
print(a.largestOddNumber("5231"))  # Output: "0"