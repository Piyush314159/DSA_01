string="abcabcddd"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring=set()
        str_dict={}
        for i in range(0,len(s)):
            substring={s[i]}
            for j in range(i+1,len(s)):
                if s[j] not in substring:
                    substring.add(s[j])
                else:
                    break
                    
            str_dict[tuple(substring)]=i
        
        if len(str_dict)==0:
            return 0
            
        return max(len(key) for key in str_dict.keys())
                    
        

a=Solution()
print(a.lengthOfLongestSubstring(string))