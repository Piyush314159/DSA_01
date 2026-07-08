class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1      # build frequency dictionary for substring s[i:j+1]
                if j - i >= 2:  # min length 3          # calculate beauty only for substrings of length >= 3
                    total += max(freq.values()) - min(freq.values())
        return total
    
a = Solution()
print(a.beautySum('aabcb'))
