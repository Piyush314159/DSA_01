'''
For every character as a center, find the longest palindrome expandable from there, and keep the biggest one overall.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left +1 : right]
        best = ""
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            if len(odd)  > len(best): best = odd
            if len(even) > len(best): best = even
        return best
    
a = Solution()
print(a.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(a.longestPalindrome("cbbd"))  # Output: "bb"