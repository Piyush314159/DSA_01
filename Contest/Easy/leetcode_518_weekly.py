'''
The problem is to count the number of rotations of a given string that have exactly k adjacent pairs of equal characters.
where n is the length of the string s.
we will take prefix of the s length 0 to (n-1) and pus the prefic to end of the string
and then we will check the adjacent pairs equal or not if equal then we will score them
if the score is equal to k for any rotation, then we will increment the answer by 1
'''

class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            rot_str = s[i:] + s[:i]
            score = 0
            for j in range(n-1):
                if rot_str[j] == rot_str[j+1]:
                    score += 1
            if score == k:
                ans += 1
        return ans


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        d = s + s
        match = []
        for i in range(2*n - 1):
            if d[i] == d[i+1]:
                match.append(1)
            else:
                match.append(0)
        
        # initial window sum for rotation 0
        score = sum(match[0:n-1])
        ans = 0
        if score == k:
            ans += 1
        
        # slide the window for rotations 1 to n-1
        for i in range(1, n):
            score = score - match[i-1] + match[i+n-2]
            if score == k:
                ans += 1
        
        return ans
    