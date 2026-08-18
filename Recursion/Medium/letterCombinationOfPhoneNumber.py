class Solution:
    def letterCombinations(self, digits: str):

        if not digits:
            return []
        
        result = []

        phone_map = {
            "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
            "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz",
        }

        def backtrack(i,c):                         # i: index of digits, c: current combination
            if i >= len(digits):
                result.append(c)
                return

            for letter in phone_map[digits[i]]:
                backtrack(i + 1, c + letter)        #it sends the c to the next digit chars to make combination

        backtrack(0, "")
        return result

sol = Solution()
print(sol.letterCombinations("235"))