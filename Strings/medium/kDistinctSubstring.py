class Solution:
    def countSubstr(self, s, k):
        
        def atMost(k):
            left = 0
            count = 0
            freq = {}
            
            for right in range(len(s)):
                freq[s[right]] = freq.get(s[right], 0) + 1
                
                while len(freq) > k:        # Shrink the window if there are more than k distinct characters
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                
                count += right - left + 1   # takes substrings ending at right we are counting from right to left, so we add right - left + 1 to count for each right
            
            return count
        
        return atMost(k) - atMost(k - 1)

a = Solution()
print(a.countSubstr("abcba", 2)) 