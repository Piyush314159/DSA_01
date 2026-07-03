class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a, b = {}, {}
        for i in range(len(s)):
            if s[i] in a:
                if a[s[i]] != t[i]:         # each s char always maps to the same t char
                    return False
            else:
                a[s[i]] = t[i]

            if t[i] in b:
                if b[t[i]] != s[i]:         # each t char is claimed by only one s char
                    return False
            else:
                b[t[i]] = s[i]
        return True
    
a = Solution()
print(a.isIsomorphic("egg", "add"))  # True
print(a.isIsomorphic("foo", "bar"))  # False
print(a.isIsomorphic("paper", "title"))  # True
print(a.isIsomorphic("ab", "aa"))  # False