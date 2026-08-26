from collections import defaultdict

string="abcabbcddd"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=defaultdict(int)
        max_length=0
        l=0

        for r in range(len(s)):
            seen[s[r]]+=1 #it will check every element in the string and we are sliding right to the string

            while seen[s[r]]>1:
                seen[s[l]]-=1 #sliding left  
                l+=1
            
            max_length=max(max_length,r-l+1)#max_length is resetting every time
        
        return max_length
    
a = Solution()
result = a.lengthOfLongestSubstring("abcabbcddd")

print(f"Result: {result}")