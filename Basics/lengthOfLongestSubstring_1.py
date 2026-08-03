string="abcabcddd"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}                           #for storing where we seen the characters
        left = 0                            #for applying sliding window
        max_len = 0                         #for storing
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right          #for storing the char postions
            max_len = max(max_len, right - left + 1)
            print(seen,left,max_len)
        return max_len
                    
        

a=Solution()
print(a.lengthOfLongestSubstring(string))