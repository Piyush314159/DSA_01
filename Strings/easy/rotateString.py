class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            i %= len(s)                 # we use this to rotate the string unnecessarily many times
            rotated = s[i:] + s[:i]     
            if rotated == goal:
                return True
        return False
    
a = Solution()
print(a.rotateString("abcde", "cdeab"))  # True
print(a.rotateString("abcde", "abced"))  # False