class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
        

a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(a.longestCommonPrefix(["dog","racecar","car"]))  # Output: ""