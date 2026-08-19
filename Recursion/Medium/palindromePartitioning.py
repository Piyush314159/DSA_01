class solution:
    def partition(self, s):
        res = []

        def palindrome(i, c):

            if i >= len(s):
                res.append(c[:])
                return

            for j in range(i, len(s)):
                if s[ i : j+1] == s[i:j+1][::-1]:
                    c.append(s[i : j+1])
                    palindrome(j+1, c)
                    c.pop()

        palindrome(0, [])

        return res

sol = solution()
print(sol.partition("aab")) 